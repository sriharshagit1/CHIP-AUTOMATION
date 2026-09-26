import unittest
from chippilot.blast_radius import analyze_blast_radius
from chippilot.regression_plan import build_regression_plan
class TestBlastRadius(unittest.TestCase):
    def test_plan(self):
        b=analyze_blast_radius('module top; sub u(); endmodule','top.sv',['sub.sv'])
        p=build_regression_plan(b,['sub.sv/test','other/test'])
        self.assertTrue(p['full_regression_required'])
if __name__=='__main__': unittest.main()
