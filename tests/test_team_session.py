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
        shutil.copyfile(team.ROOT / 'team/members.json', self.root / 'team/members.json')
        (self.root / '.gitignore').write_text(team.SESSION + '\n', encoding='utf-8')
        self.git('init', '-b', 'main')
        self.git('config', 'user.name', 'Original User')
        self.git('config', 'user.email', 'original@example.test')
        self.git('add', '.')
        self.git('commit', '-m', 'Historical bootstrap')
        self.base = self.git('rev-parse', 'HEAD')

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
        with self.assertRaises(ValueError):
            self.begin('sojo')
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


if __name__ == '__main__':
    unittest.main()
