import unittest
from chippilot.runtime_tools import RuntimeTools
class TestRuntimeTools(unittest.TestCase):
 def test_read_allowed_file(self):
  r=RuntimeTools().read_rtl('width_mismatch.sv'); self.assertIn('module',r['content'])
 def test_path_escape(self):
  with self.assertRaises(PermissionError): RuntimeTools().read_rtl('../README.md')
if __name__=='__main__': unittest.main()
