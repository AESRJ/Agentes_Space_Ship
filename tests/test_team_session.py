import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import team_session as team


class TeamSessionTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        (self.root / 'team').mkdir()
        # Registro de prueba explícito: no depende de quién esté activo hoy en el registro real.
        self.write_roster()
        (self.root / '.gitignore').write_text(team.SESSION + '\n', encoding='utf-8')
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Original User')
        self.git('config', 'user.email', 'original@example.test')
        self.git('add', '.')
        self.git('commit', '-m', 'Historical bootstrap')
        self.base = self.git('rev-parse', 'HEAD')

    ROSTER = {'gael': 'active', 'adrian': 'inactive', 'kevin': 'active',
              'isra': 'active', 'jorge': 'active', 'sojo': 'active'}

    def write_roster(self, **overrides):
        statuses = dict(self.ROSTER, **overrides)
        entries = [{'id': i, 'name': i.capitalize(), 'github': None, 'status': st} for i, st in statuses.items()]
        (self.root / 'team/members.json').write_text(
            json.dumps({'schema_version': 1, 'members': entries}), encoding='utf-8')

    def git(self, *args):
        return team.git(*args, root=self.root)

    def stage(self):
        (self.root / 'note.md').write_text('result\n', encoding='utf-8')
        self.git('add', 'note.md')

    def begin(self, member='gael'):
        return team.start(member, 'tarea-001', f'{member}@example.test', self.root)

    def test_commit_tags_and_author_survive_wrong_environment(self):
        self.begin()
        self.stage()
        with patch.dict('os.environ', {'GIT_AUTHOR_NAME': 'Wrong', 'GIT_AUTHOR_EMAIL': 'wrong@example.test'}):
            team.commit('investigación', root=self.root)
        self.assertEqual(self.git('show', '-s', '--format=%an <%ae>'), 'Gael <gael@example.test>')
        self.assertEqual(self.git('config', 'user.name'), 'Original User')
        self.assertIn('1 commits', team.check(self.base, root=self.root))
        self.assertEqual(self.git('show', '-s', '--format=%s'), '[gael] investigación')

    def test_cannot_commit_without_session_or_on_another_branch(self):
        self.stage()
        with self.assertRaises(ValueError):
            team.commit('missing identity', root=self.root)
        self.git('reset')
        (self.root / 'note.md').unlink()
        self.begin()
        self.git('switch', 'main')
        self.stage()
        with self.assertRaises(ValueError):
            team.commit('wrong branch', root=self.root)

    def test_rejects_pending_person_dirty_tree_and_invalid_task(self):
        self.write_roster(sojo='pending')
        with self.assertRaises(ValueError):
            self.begin('sojo')
        self.write_roster()
        with self.assertRaises(ValueError):
            team.start('gael', '../unsafe', 'gael@example.test', self.root)
        self.stage()
        with self.assertRaises(ValueError):
            self.begin()
        self.assertEqual(self.git('branch', '--show-current'), 'main')

    def test_new_session_switches_author_and_without_ai_is_explicit(self):
        self.begin()
        self.begin('jorge')
        self.stage()
        team.commit('sin IA', ai_assisted=False, root=self.root)
        self.assertEqual(self.git('show', '-s', '--format=%an'), 'Jorge')
        self.assertIn('AI-Assisted: false', self.git('show', '-s', '--format=%B'))
        team.check(self.base, root=self.root)

    def test_check_rejects_untagged_and_unknown_identity(self):
        self.stage()
        self.git('commit', '-m', 'untagged')
        with self.assertRaises(ValueError):
            team.check(self.base, root=self.root)
        self.git('commit', '--amend', '-m', '[unknown] changes\n\nTeam-Member: unknown\nAI-Assisted: true')
        with self.assertRaises(ValueError):
            team.check(self.base, root=self.root)

    def test_session_is_ignored_and_refuses_accidental_publication(self):
        self.begin()
        self.assertEqual(self.git('status', '--porcelain'), '')
        self.git('add', '-f', team.SESSION)
        with self.assertRaises(ValueError):
            team.commit('leak session', root=self.root)

    def test_resume_identifies_existing_dirty_work_only_on_matching_branch(self):
        self.begin('gael')
        self.stage()
        team.start('gael', 'tarea-001', 'gael@example.test', self.root, resume=True)
        self.assertEqual(team.session(self.root)[0]['member_id'], 'gael')
        with self.assertRaises(ValueError):
            team.start('jorge', 'tarea-001', 'jorge@example.test', self.root, resume=True)
        self.assertTrue(self.git('diff', '--cached', '--name-only'))

    def test_checkpoint_includes_member_without_local_email(self):
        import project_memory as memory
        self.begin('jorge')
        with patch.object(memory, 'sync_document', return_value={'status': 'pending'}):
            record = memory.checkpoint('test-identity-001', 'avance', 'evidencia', 'seguir', root=self.root)
        content = (self.root / record['file']).read_text(encoding='utf-8')
        self.assertIn('Integrante: jorge', content)
        self.assertNotIn('jorge@example.test', content)

    def test_checkpoint_rejects_stale_session_before_writing(self):
        import project_memory as memory
        self.begin('jorge')
        self.git('switch', 'main')
        with self.assertRaises(ValueError):
            memory.checkpoint('test-stale-001', 'avance', 'evidencia', 'seguir', root=self.root)
        self.assertFalse((self.root / 'docs/sessions/test-stale-001.md').exists())

    def test_no_staged_changes_and_duplicate_trailers_are_rejected(self):
        self.begin()
        with self.assertRaises(ValueError):
            team.commit('empty', root=self.root)
        self.stage()
        self.git('commit', '-m', '[gael] duplicate\n\nTeam-Member: gael\nTeam-Member: jorge\nAI-Assisted: true')
        with self.assertRaises(ValueError):
            team.check(self.base, root=self.root)


    def test_registry_accepts_inactive_and_rejects_unknown_status(self):
        roster = team.members(self.root)
        self.assertEqual(roster['adrian']['status'], 'inactive')
        self.write_roster(adrian='retired')
        with self.assertRaises(ValueError):
            team.members(self.root)

    def test_inactive_member_cannot_start_session_or_sign_commits(self):
        with self.assertRaises(ValueError):
            self.begin('adrian')
        self.assertEqual(self.git('branch', '--show-current'), 'main')
        self.stage()
        self.git('commit', '-m', '[adrian] cambio nuevo\n\nTeam-Member: adrian\nAI-Assisted: true')
        with self.assertRaises(ValueError):
            team.check(self.base, root=self.root)

    def test_active_sojo_starts_session_and_commits_with_own_identity(self):
        info = self.begin('sojo')
        self.assertEqual(info['branch'], 'sojo/tarea-001')
        self.stage()
        team.commit('incorporación', root=self.root)
        self.assertEqual(self.git('show', '-s', '--format=%an <%ae>'), 'Sojo <sojo@example.test>')
        self.assertEqual(self.git('show', '-s', '--format=%s'), '[sojo] incorporación')
        self.assertIn('1 commits', team.check(self.base, root=self.root))

    def test_real_registry_is_valid(self):
        roster = team.members()
        self.assertEqual(len(roster), 6)
        self.assertTrue(all(m['status'] in ('active', 'pending', 'inactive') for m in roster.values()))


if __name__ == '__main__':
    unittest.main()
