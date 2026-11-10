import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import project_memory as memory
from configure_codex import configure
from export_project import export


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        (self.root / 'memory').mkdir()
        (self.root / 'docs/sessions').mkdir(parents=True)
        (self.root / 'memory/notebook.json').write_text(json.dumps({
            'notebook_id': '62c97db5-1c82-41bd-a443-2f1f98675ada'}), encoding='utf-8')

    def test_checkpoint_survives_offline_and_retries_same_id(self):
        with patch.object(memory, 'cli', side_effect=RuntimeError('offline')):
            result = memory.checkpoint('test-001', 'avance', 'archivo', 'continuar', root=self.root)
            self.assertEqual(result['status'], 'pending')
            path = self.root / result['file']
            original = path.read_bytes()
            again = memory.checkpoint('test-001', 'avance', 'archivo', 'continuar', root=self.root)
            self.assertEqual(again['status'], 'pending')
            self.assertEqual(path.read_bytes(), original)
            with self.assertRaises(ValueError):
                memory.checkpoint('test-001', 'otro avance', 'archivo', 'continuar', root=self.root)

    def test_rejects_traversal(self):
        with self.assertRaises(ValueError):
            memory.checkpoint('../outside', 's', 'e', 'n', root=self.root)
        with self.assertRaises(ValueError):
            memory.safe_document(self.root / '../outside.md', self.root)
        secret = self.root / 'secret.md'
        secret.write_text('not for upload')
        with self.assertRaises(ValueError):
            memory.safe_document(secret, self.root)

    def test_rejects_symlink_to_external_file(self):
        external = self.root / 'secret.md'
        external.write_text('private')
        link = self.root / 'docs/link.md'
        try:
            link.symlink_to(external)
        except OSError:
            self.skipTest('Symlinks not permitted on this Windows runner')
        with self.assertRaises(ValueError):
            memory.safe_document(link, self.root)

    def test_deduplicates_after_uncertain_upload_and_pins_notebook(self):
        source = {'id': 'source-1', 'title': None}
        calls = []
        def remote(*args, **kwargs):
            calls.append(args)
            self.assertIn('62c97db5-1c82-41bd-a443-2f1f98675ada', args)
            if args[:2] == ('source', 'list'):
                return {'sources': [source] if source['title'] else []}
            if args[:2] == ('source', 'add'):
                # Real NotebookLM file upload can ignore the requested title.
                source['title'] = Path(args[2]).name
                return {'source': source}
            if args[:2] == ('source', 'wait'):
                return {'status': 'ready'}
            raise AssertionError(args)
        with patch.object(memory, 'cli', side_effect=remote):
            first = memory.upload_text('same content', 'REGISTRO', self.root)
            second = memory.upload_text('same content', 'REGISTRO', self.root)
        self.assertEqual(first['source_id'], second['source_id'])
        self.assertEqual(sum(c[:2] == ('source', 'add') for c in calls), 1)

    def test_reuses_legacy_filename_source(self):
        import hashlib
        digest = hashlib.sha256(b'abc').hexdigest()
        with patch.object(memory, 'cli', side_effect=[{'sources': [
                {'id': 'legacy', 'title': digest + '.txt'}]}, {'status': 'ready'}]) as mocked:
            receipt = memory.upload_text('abc', 'CONTEXTO', self.root)
        self.assertEqual(receipt['source_id'], 'legacy')
        self.assertFalse(any(c.args[:2] == ('source', 'add') for c in mocked.call_args_list))

    def test_processing_timeout_is_not_success(self):
        with patch.object(memory, 'cli', side_effect=[{'sources': []}, {'source': {'id': 's'}}, RuntimeError('timeout')]):
            result = memory.checkpoint('test-002', 's', 'e', 'n', root=self.root)
        self.assertEqual(result['status'], 'pending')
        self.assertFalse(list((self.root / '.memory').glob('*.receipt.json')))

    def test_duplicate_remote_sources_require_review(self):
        import hashlib
        title = 'SPACE-SHIP REGISTRO ' + hashlib.sha256(b'abc').hexdigest()
        with patch.object(memory, 'cli', return_value={'sources': [
                {'id': '1', 'title': title}, {'id': '2', 'title': title}]}):
            with self.assertRaises(RuntimeError):
                memory.upload_text('abc', 'REGISTRO', self.root)

    def test_cli_nonzero_and_malformed_json_fail(self):
        for result in (subprocess.CompletedProcess([], 1, '', 'secret details'),
                       subprocess.CompletedProcess([], 0, 'invalid json', ''),
                       subprocess.CompletedProcess([], 0, '{"error":"failed"}', '')):
            with patch.dict(os.environ, {'NOTEBOOKLM_BIN': '/fake/notebooklm'}), \
                    patch.object(memory.subprocess, 'run', return_value=result):
                with self.assertRaises(RuntimeError):
                    memory.cli('source', 'list', '--json')

    def test_ask_pins_notebook_and_preserves_conversation(self):
        with patch.object(memory, 'cli', return_value={'answer': 'ok'}) as mocked:
            memory.ask('pregunta', root=self.root)
        args = mocked.call_args.args
        self.assertIn('-n', args)
        self.assertNotIn('--new', args)
        self.assertNotIn('--save-as-note', args)

    def test_export_preserves_sources_and_excludes_auth(self):
        (self.root / 'docs/vision.md').write_text('idea', encoding='utf-8')
        (self.root / 'docs/sessions/private-session.md').write_text('session', encoding='utf-8')
        (self.root / 'AGENTS.md').write_text('repo-specific', encoding='utf-8')
        (self.root / 'storage_state.json').write_text('secret')
        target = self.root / 'export'
        result = export(target, root=self.root)
        self.assertEqual(set(result['files_sha256']), {'docs/vision.md'})
        self.assertFalse((target / 'storage_state.json').exists())
        self.assertFalse((target / 'AGENTS.md').exists())
        with self.assertRaises(ValueError):
            export(target, root=self.root)

    def test_config_idempotence_and_preservation(self):
        binary_dir = self.root / 'environment with spaces'
        binary_dir.mkdir()
        python = binary_dir / 'python.exe'
        python.touch()
        (binary_dir / 'notebooklm.exe').touch()
        path = configure(self.root, python)
        original = path.read_bytes()
        configure(self.root, python)
        self.assertEqual(path.read_bytes(), original)
        import tomllib
        config = tomllib.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(config['mcp_servers']['space_ship_memory']['command'], python.as_posix())
        path.write_text('# personal configuration', encoding='utf-8')
        with self.assertRaises(ValueError):
            configure(self.root, python)
        self.assertEqual(path.read_text(), '# personal configuration')

    def test_config_keeps_virtualenv_python_symlink(self):
        environment = self.root / 'venv/bin'
        environment.mkdir(parents=True)
        python = environment / 'python'
        try:
            python.symlink_to(sys.executable)
        except OSError:
            self.skipTest('Symlinks not permitted')
        (environment / 'notebooklm').touch()
        import tomllib
        config = tomllib.loads(configure(self.root, python).read_text(encoding='utf-8'))
        self.assertEqual(config['mcp_servers']['space_ship_memory']['command'], python.as_posix())


class McpTests(unittest.IsolatedAsyncioTestCase):
    async def test_tools_are_registered_with_expected_contract(self):
        source = Path(__file__).resolve().parents[1] / 'integrations/notebooklm/server.py'
        spec = importlib.util.spec_from_file_location('space_ship_server', source)
        server = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(server)
        tools = await server.mcp.list_tools()
        self.assertEqual({t.name for t in tools}, {
            'memory_status', 'memory_ask', 'memory_checkpoint', 'memory_sync', 'memory_publish_context'})
        tool = next(t for t in tools if t.name == 'memory_checkpoint')
        self.assertEqual(set(tool.inputSchema['required']), {'record_id', 'summary', 'evidence', 'next_steps'})


if __name__ == '__main__':
    unittest.main()
