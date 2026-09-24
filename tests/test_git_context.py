import unittest
from chippilot.git_context import recent_commits, changed_files

class TestGitContext(unittest.TestCase):
    def test_recent_commits(self):
        r=recent_commits('.')
        self.assertEqual(r['returncode'],0)
        self.assertTrue(r['stdout'])
    def test_changed_files(self):
        r=changed_files('.')
        self.assertEqual(r['returncode'],0)

if __name__=='__main__': unittest.main()
