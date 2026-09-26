import unittest
from chippilot.repair_context import build_feedback
class TestRepairContext(unittest.TestCase):
 def test_feedback_contains_verification_and_rtl(self):
  x=build_feedback('WIDTH-001',{'status':'FAIL','stage':'simulation','stdout':'expected AB observed 0B'})
  self.assertEqual(x['verification']['stage'],'simulation'); self.assertIn('module',x['rtl_context'])
if __name__=='__main__': unittest.main()
