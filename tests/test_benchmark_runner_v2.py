import unittest
from benchmark.run_agent_benchmark import CASES
from benchmark.scorecard import aggregate, CaseScore
class TestBenchmarkRunner(unittest.TestCase):
 def test_case_catalog(self): self.assertGreaterEqual(len(CASES),5)
 def test_scorecard_contract(self):
  s=aggregate([CaseScore('A',1,1,1,1,1,1,1)])
  self.assertEqual(s['verified_fix_rate'],1.0)
if __name__=='__main__': unittest.main()
