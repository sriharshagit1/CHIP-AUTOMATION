import unittest
from chippilot.causal_evidence import score_candidate
class TestCausalEvidence(unittest.TestCase):
    def test_hypothesis_only(self):
        x=score_candidate({'file':'a.sv','module':'m','category':'FSM','earliest_observed':True},{},['a.sv'],['m'],['FSM'])
        self.assertEqual(x['heuristic_score'],8)
        self.assertEqual(x['status'],'HYPOTHESIS_ONLY')
if __name__=='__main__': unittest.main()
