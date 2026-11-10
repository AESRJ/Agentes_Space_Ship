"""Validate shared configuration without credentials or network access."""
import json
from pathlib import Path
import tomllib
import uuid

ROOT = Path(__file__).resolve().parents[1]


def validate():
    expected = {'coordinacion', 'investigacion', 'diseno', 'implementacion', 'pruebas', 'memoria'}
    found = set()
    for path in (ROOT / '.codex/agents').glob('*.toml'):
        agent = tomllib.loads(path.read_text(encoding='utf-8'))
        for key in ('name', 'description', 'developer_instructions'):
            assert isinstance(agent.get(key), str) and agent[key].strip(), f'{path}: falta {key}'
        assert agent['name'] not in found, 'Perfil duplicado'
        found.add(agent['name'])
    assert found == expected, f'Perfiles inesperados: {found}'
    uuid.UUID(json.loads((ROOT / 'memory/notebook.json').read_text(encoding='utf-8'))['notebook_id'])
    for name in ('AGENTS.md', 'docs/vision.md', 'docs/scope.md', 'docs/state.md',
                 '.agents/skills/space-memory/SKILL.md', 'integrations/notebooklm/LICENSE.knowingdoing'):
        assert (ROOT / name).is_file(), f'Falta {name}'
    config = ROOT / '.codex/config.toml'
    if config.exists():
        tomllib.loads(config.read_text(encoding='utf-8'))
    print('OK: seis perfiles, contexto, cuaderno y configuración TOML.')


if __name__ == '__main__':
    validate()
