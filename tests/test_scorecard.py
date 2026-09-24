import unittest
from benchmark.scorecard import CaseScore, aggregate
class TestScorecard(unittest.TestCase):
 def test_aggregate(self):
  xs=[CaseScore('A',1,1,1,1,1,1,2),CaseScore('B',1,0,0,1,0,0,4)]
  s=aggregate(xs)
  self.assertEqual(s['cases'],2); self.assertEqual(s['verified_fix_rate'],.5); self.assertEqual(s['mean_time_seconds'],3)
if __name__=='__main__': unittest.main()
