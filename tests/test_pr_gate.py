import unittest
from chippilot.pr_gate import build_pr_summary
class TestPRGate(unittest.TestCase):
    def test_human_control(self):
        x=build_pr_summary({'executive_summary':{'final_status':'VERIFIED'},'verification':{'status':'VERIFIED'}})
        self.assertTrue(x['human_review_required'])
        self.assertFalse(x['merge_allowed_by_agent'])
if __name__=='__main__': unittest.main()
