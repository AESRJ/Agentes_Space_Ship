"""Write only this project's machine-specific MCP configuration."""
import argparse
import json
from pathlib import Path
import sys

MARKER = '# Managed by Space Ship setup; project-local configuration.'


def configure(root: Path, python: Path):
    # Keep a venv's Python symlink path: resolving it loses the environment and its CLI.
    root, python = root.resolve(), python.absolute()
    if not python.is_file():
        raise ValueError('No existe el ejecutable Python indicado.')
    config = root / '.codex/config.toml'
    if config.exists() and not config.read_text(encoding='utf-8').startswith(MARKER):
        raise ValueError('Existe configuración personal del proyecto. Integra el MCP manualmente; no se sobrescribió.')
    binary = python.parent / ('notebooklm.exe' if python.suffix == '.exe' else 'notebooklm')
    if not binary.is_file():
        raise ValueError('Falta NotebookLM junto al Python seleccionado; instala requirements.txt.')
    quote = lambda path: json.dumps(str(path).replace('\\', '/'), ensure_ascii=False)
    body = (MARKER + '\n\n[mcp_servers.space_ship_memory]\n'
            f'command = {quote(python)}\n'
            f'args = [{quote(root / "integrations/notebooklm/server.py")}]\n'
            'startup_timeout_sec = 30\ntool_timeout_sec = 300\n\n'
            '[mcp_servers.space_ship_memory.env]\n'
            f'NOTEBOOKLM_BIN = {quote(binary)}\nPYTHONUTF8 = "1"\nPYTHONIOENCODING = "utf-8"\n')
    config.parent.mkdir(exist_ok=True)
    config.write_text(body, encoding='utf-8')
    return config


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--python', default=sys.executable)
    args = parser.parse_args()
    print(configure(Path(__file__).resolve().parents[1], Path(args.python)))
