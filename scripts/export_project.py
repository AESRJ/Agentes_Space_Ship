"""Export a reviewable context package to a new directory, never deploy a game."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

from project_memory import ROOT, context_files, git_context, safe_document


def export(output, root=ROOT):
    output = Path(output).resolve()
    if output.exists():
        raise ValueError('El destino debe ser nuevo; no se sobrescriben archivos.')
    paths = [p for p in context_files(root) if p.name != 'AGENTS.md']
    for path in paths:
        safe_document(path, root)
    output.mkdir(parents=True)
    hashes = {}
    for path in paths:
        relative = path.relative_to(root)
        dest = output / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)
        hashes[relative.as_posix()] = hashlib.sha256(dest.read_bytes()).hexdigest()
    manifest = {'origin': 'AESRJ/Agentes_Space_Ship', 'git': git_context(root),
                'purpose': 'Contexto para revisar antes de implementar; no es despliegue ni aprobación de propuestas.',
                'files_sha256': hashes}
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
    (output / 'README.md').write_text('# Traspaso de Space Ship\n\nRevisar docs/scope.md y las decisiones abiertas antes de implementar. '
        'El contexto procede del repositorio de agentes; consultar manifest.json para la revisión exacta. '
        'Configurar las instrucciones del motor en el repositorio destino, sin copiar las reglas que prohíben código de juego en el repositorio de agentes.\n', encoding='utf-8')
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(export(args.output), ensure_ascii=False, indent=2))
