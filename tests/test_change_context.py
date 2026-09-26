import unittest
from chippilot.change_context import extract_changed_files, build_change_context
class TestChangeContext(unittest.TestCase):
    def test_changed_files(self):
        self.assertEqual(extract_changed_files('diff\n+++ b/rtl/foo.sv\n+++ b/tb/foo_tb.sv'),['rtl/foo.sv','tb/foo_tb.sv'])
    def test_hypothesis_warning(self):
        self.assertIn('hypotheses',build_change_context([], '')['instruction'])
if __name__=='__main__': unittest.main()
