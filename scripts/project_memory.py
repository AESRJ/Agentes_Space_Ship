"""Durable, project-scoped NotebookLM memory. No implicit active notebook."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

from filelock import FileLock

ROOT = Path(__file__).resolve().parents[1]


def notebook_config(root=ROOT):
    config = json.loads((root / 'memory/notebook.json').read_text(encoding='utf-8'))
    import uuid
    uuid.UUID(config['notebook_id'])
    return config


def cli(*args, timeout=240):
    binary = os.environ.get('NOTEBOOKLM_BIN') or shutil.which('notebooklm')
    if not binary:
        candidate = Path(sys.executable).parent / ('notebooklm.exe' if os.name == 'nt' else 'notebooklm')
        if candidate.exists():
            binary = str(candidate)
    if not binary:
        raise RuntimeError('NotebookLM CLI no instalado; ejecuta Setup-Windows.ps1 o instala requirements.txt.')
    env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
    result = subprocess.run([binary, *args], capture_output=True, text=True,
                            encoding='utf-8', errors='replace', timeout=timeout, env=env)
    if result.returncode:
        raise RuntimeError(f'NotebookLM terminó con código {result.returncode}. '
                           'Comprueba login, permisos del cuaderno y límites del servicio; no se confirmó la operación.')
    try:
        value = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError('NotebookLM no devolvió JSON válido; no se confirmó la operación.') from exc
    if isinstance(value, dict) and (value.get('error') or value.get('success') is False):
        raise RuntimeError('NotebookLM devolvió un error; no se confirmó la operación.')
    return value


def git_context(root=ROOT):
    def get(*args):
        try:
            p = subprocess.run(['git', '-C', str(root), *args], capture_output=True,
                               text=True, encoding='utf-8', errors='replace', timeout=10)
            return p.stdout.strip() if p.returncode == 0 else None
        except (OSError, subprocess.TimeoutExpired):
            return None
    return {'base_commit': get('rev-parse', 'HEAD'), 'branch': get('branch', '--show-current'),
            'working_tree_dirty': bool(get('status', '--porcelain'))}


def context_files(root=ROOT):
    paths = [root / 'AGENTS.md']
    paths += sorted((root / 'docs').rglob('*.md'))
    # Sessions are independent sources. The initial proposal is an historical draft.
    return [p for p in paths if p.is_file() and not p.is_symlink()
            and 'sessions' not in p.relative_to(root).parts
            and p.name not in ('TEMPLATE.md', 'propuesta-inicial.md')]


def safe_document(path, root=ROOT):
    path = Path(path)
    if not path.is_absolute():
        path = root / path
    resolved = path.resolve()
    try:
        relative = resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError('El documento debe estar dentro del repositorio.') from exc
    if not path.is_file() or path.is_symlink() or resolved != path.absolute():
        raise ValueError('Se requiere un archivo regular, sin enlaces simbólicos.')
    if relative.parts[0] != 'docs' or path.suffix != '.md':
        raise ValueError('Solo se publican documentos Markdown de docs/.')
    return path


def upload_text(content, kind, root=ROOT):
    notebook = notebook_config(root)['notebook_id']
    digest = hashlib.sha256(content.encode('utf-8')).hexdigest()
    title = f'SPACE-SHIP {kind} {digest}'
    local = root / '.memory'
    local.mkdir(exist_ok=True)
    with FileLock(str(local / 'sync.lock'), timeout=30):
        # Query the server on retries: an upload may have succeeded before a timeout.
        listing = cli('source', 'list', '-n', notebook, '--json')
        sources = listing.get('sources')
        if not isinstance(sources, list):
            raise RuntimeError('Formato de lista de fuentes desconocido.')
        # File ingestion may keep the filename instead of honoring --title.
        # Accept both and the legacy digest filename produced by the first version.
        aliases = {title, f'{title}.txt', f'{digest}.txt'}
        matches = [s for s in sources if s.get('title') in aliases]
        if len(matches) > 1:
            raise RuntimeError('Hay fuentes duplicadas; revisar con el integrador sin borrar automáticamente.')
        source_id = matches[0].get('id') if matches else None
        if not source_id:
            # Temporary UTF-8 file keeps large content out of Windows argv limits.
            payload = local / f'{title}.txt'
            payload.write_text(content, encoding='utf-8')
            added = cli('source', 'add', str(payload), '-n', notebook,
                        '--type', 'file', '--title', title, '--json')
            source_id = added.get('source', added).get('id')
        if not source_id:
            raise RuntimeError('No se recibió un identificador de fuente; verificar antes de reintentar.')
        cli('source', 'wait', source_id, '-n', notebook, '--timeout', '45', '--json', timeout=55)
        receipt = {'status': 'synced', 'notebook_id': notebook, 'source_id': source_id,
                   'sha256': digest, 'title': title, 'synced_at': datetime.now(timezone.utc).isoformat()}
        (local / f'{digest}.receipt.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')
        return receipt


def sync_document(path, root=ROOT):
    path = safe_document(path, root)
    content = f'Archivo: {path.relative_to(root).as_posix()}\n\n' + path.read_text(encoding='utf-8')
    try:
        return upload_text(content, 'REGISTRO', root)
    except (RuntimeError, OSError, subprocess.TimeoutExpired, TimeoutError) as exc:
        return {'status': 'pending', 'file': str(path.relative_to(root)), 'error': str(exc)}


def checkpoint(record_id, summary, evidence, next_steps, kind='avance', status='propuesto', root=ROOT):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{2,100}', record_id):
        raise ValueError('ID: 3–101 caracteres en minúsculas, números y guiones.')
    if kind not in ('avance', 'decision', 'bloqueo', 'investigacion', 'diseno', 'pruebas'):
        raise ValueError('Tipo de registro desconocido.')
    if status not in ('propuesto', 'aceptado', 'implementado', 'verificado', 'bloqueado'):
        raise ValueError('Estado de contenido desconocido.')
    if not all(value.strip() for value in (summary, evidence, next_steps)):
        raise ValueError('Resumen, evidencia y siguientes pasos son obligatorios.')
    path = root / 'docs/sessions' / f'{record_id}.md'
    path.parent.mkdir(parents=True, exist_ok=True)
    # Retry compares stable content; preserve original timestamp and revision metadata.
    body = (f'Tipo: {kind}\nEstado del contenido: {status}\n\n## Resumen\n{summary}\n\n'
            f'## Evidencia\n{evidence}\n\n## Siguientes pasos\n{next_steps}\n')
    if path.exists():
        existing = path.read_text(encoding='utf-8')
        if not existing.endswith(body):
            raise ValueError('ID ya usado con otro contenido. Crea un registro nuevo; no sobrescribas historia.')
    else:
        header = (f'# Registro {record_id}\n\nFecha UTC: {datetime.now(timezone.utc).isoformat()}\n'
                  f'Contexto Git al guardar: {json.dumps(git_context(root), ensure_ascii=False)}\n\n')
        # Exclusive create prevents same-ID races from overwriting another session.
        with path.open('x', encoding='utf-8') as stream:
            stream.write(header + body)
    return {'file': str(path.relative_to(root)), **sync_document(path, root)}


def sync_all(root=ROOT):
    results = [sync_document(p, root) for p in sorted((root / 'docs/sessions').glob('*.md'))]
    return {'status': 'pending' if any(r['status'] != 'synced' for r in results) else 'synced',
            'records': results}


def publish_context(root=ROOT):
    context = git_context(root)
    sections = ['# Contexto Space Ship', 'Instantánea de documentos; no implica aprobación ni integración.',
                'Versión Git: ' + json.dumps(context, ensure_ascii=False),
                'Los registros de sesión son fuentes separadas. Ante discrepancias, verificar la revisión en Git.']
    for path in context_files(root):
        if path.name != 'AGENTS.md':
            safe_document(path, root)
        sections += [f'\n---\n## {path.relative_to(root).as_posix()}\n', path.read_text(encoding='utf-8')]
    return upload_text('\n'.join(sections), 'CONTEXTO', root)


def status(root=ROOT):
    config = notebook_config(root)
    return {'notebook': config, 'git': git_context(root),
            'sources': cli('source', 'list', '-n', config['notebook_id'], '--json')}


def ask(question, root=ROOT):
    return cli('ask', question, '-n', notebook_config(root)['notebook_id'], '--json', timeout=180)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['status', 'sync', 'publish', 'ask'])
    parser.add_argument('question', nargs='?')
    args = parser.parse_args()
    if args.action == 'ask' and not args.question:
        parser.error('ask requiere una pregunta')
    action = {'status': status, 'sync': sync_all, 'publish': publish_context,
              'ask': lambda: ask(args.question)}[args.action]
    try:
        result = action()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result.get('status') == 'pending' else 0
    except Exception as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
