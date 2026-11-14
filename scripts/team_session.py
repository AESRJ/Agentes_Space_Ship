"""Identidad local por sesión y commits con atribución explícita, sin dependencias."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SESSION = '.space-session.json'


def git(*args, root=ROOT, env=None):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True,
                            text=True, encoding='utf-8', env=env)
    if result.returncode:
        raise ValueError(result.stderr.strip() or result.stdout.strip() or 'Git falló.')
    return result.stdout.strip()


def members(root=ROOT):
    entries = json.loads((root / 'team/members.json').read_text(encoding='utf-8'))['members']
    if len(entries) != 6 or len({m['id'] for m in entries}) != 6:
        raise ValueError('El registro requiere seis IDs únicos.')
    for member in entries:
        if not re.fullmatch(r'[a-z][a-z0-9-]*', member['id']):
            raise ValueError('ID de integrante inválido.')
        if member['status'] not in ('active', 'pending'):
            raise ValueError('Estado de integrante inválido.')
        if member['status'] == 'active' and not member['name']:
            raise ValueError('Un integrante activo necesita nombre.')
    return {m['id']: m for m in entries}


def active_member(member_id, root=ROOT):
    member = members(root).get(member_id)
    if not member or member['status'] != 'active':
        raise ValueError('Selecciona un integrante activo de team/members.json.')
    return member


def start(member_id, task, email, root=ROOT, resume=False):
    member = active_member(member_id, root)
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', task):
        raise ValueError('Tarea: usa minúsculas, números y guiones, sin espacios.')
    if not re.fullmatch(r'[^\s<>@]+@[^\s<>@]+', email):
        raise ValueError('Indica el correo de commits de tu propia cuenta GitHub.')
    # Each worktree keeps its own session; never change global/local Git identity.
    branch = f'{member_id}/{task}'
    current = git('branch', '--show-current', root=root)
    if resume and current != branch:
        raise ValueError('--resume requiere estar en la rama del integrante y tarea indicados.')
    if git('status', '--porcelain', root=root) and not resume:
        raise ValueError('Guarda tus cambios antes de iniciar otra sesión; para reanudar la misma rama usa --resume.')
    if current != branch:
        git('switch', '-c', branch, root=root)
    state = {'member_id': member_id, 'branch': branch, 'task': task,
             'email': email, 'started_at': datetime.now(timezone.utc).isoformat()}
    (root / SESSION).write_text(json.dumps(state, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return {'member_id': member_id, 'name': member['name'], 'branch': branch, 'task': task}


def session(root=ROOT):
    path = root / SESSION
    if not path.is_file():
        raise ValueError('Sin identidad de sesión. Ejecuta team_session.py start primero.')
    state = json.loads(path.read_text(encoding='utf-8'))
    member = active_member(state['member_id'], root)
    expected = f"{member['id']}/{state['task']}"
    if state['branch'] != expected or git('branch', '--show-current', root=root) != expected:
        raise ValueError('La rama no coincide con la sesión; inicia la identidad de esa tarea.')
    return state, member


def commit(message, ai_assisted=True, root=ROOT):
    state, member = session(root)
    if not message.strip() or '\n' in message or '\r' in message:
        raise ValueError('El mensaje debe ser una línea no vacía.')
    if not git('diff', '--cached', '--name-only', root=root):
        raise ValueError('Selecciona los cambios con git add antes del commit.')
    if SESSION in git('diff', '--cached', '--name-only', root=root).splitlines():
        raise ValueError('No publiques el archivo local de identidad.')
    # Avoid inherited author overrides attributing the commit to someone else.
    env = dict(os.environ, GIT_AUTHOR_NAME=member['name'], GIT_AUTHOR_EMAIL=state['email'],
               GIT_COMMITTER_NAME=member['name'], GIT_COMMITTER_EMAIL=state['email'])
    return git('commit', '-m', f"[{member['id']}] {message.strip()}",
               '--trailer', f"Team-Member: {member['id']}",
               '--trailer', f"AI-Assisted: {'true' if ai_assisted else 'false'}", root=root, env=env)


def check(base, head='HEAD', root=ROOT):
    """Validate new non-merge commits, leaving historical commits unchanged."""
    commits = git('rev-list', '--no-merges', f'{base}..{head}', root=root).splitlines()
    for sha in commits:
        message = git('show', '-s', '--format=%B', sha, root=root)
        trailers = git('show', '-s', '--format=%(trailers:key=Team-Member,valueonly)', sha, root=root).splitlines()
        if len(trailers) != 1:
            raise ValueError(f'{sha[:8]}: requiere exactamente un trailer Team-Member.')
        member = active_member(trailers[0].strip(), root)
        if not message.startswith(f"[{member['id']}] "):
            raise ValueError(f'{sha[:8]}: falta etiqueta de integrante en el título.')
        ai = git('show', '-s', '--format=%(trailers:key=AI-Assisted,valueonly)', sha, root=root)
        if ai not in ('true', 'false'):
            raise ValueError(f'{sha[:8]}: falta AI-Assisted: true/false.')
    return f'OK: {len(commits)} commits etiquetados. Etiquetas declarativas; no verifican identidad.'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('members')
    begin = sub.add_parser('start')
    begin.add_argument('--member', required=True)
    begin.add_argument('--task', required=True)
    begin.add_argument('--email', required=True)
    begin.add_argument('--resume', action='store_true', help='Identificar trabajo existente en la misma rama sin modificar archivos.')
    sub.add_parser('status')
    save = sub.add_parser('commit')
    save.add_argument('-m', '--message', required=True)
    save.add_argument('--without-ai', action='store_true')
    verify = sub.add_parser('check')
    verify.add_argument('--base', required=True)
    verify.add_argument('--head', default='HEAD')
    args = parser.parse_args()
    try:
        if args.command == 'members':
            print(json.dumps(list(members().values()), ensure_ascii=False, indent=2))
        elif args.command == 'start':
            print(json.dumps(start(args.member, args.task, args.email, resume=args.resume), ensure_ascii=False, indent=2))
        elif args.command == 'status':
            state, member = session()
            print(json.dumps({k: v for k, v in state.items() if k != 'email'}, indent=2))
        elif args.command == 'commit':
            print(commit(args.message, not args.without_ai))
        else:
            print(check(args.base, args.head))
    except (ValueError, KeyError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')


if __name__ == '__main__':
    main()
