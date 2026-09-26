import unittest
from benchmark.blind_eval import public_cases, score_predictions
class TestBlindEval(unittest.TestCase):
 def test_public_view_hides_patch(self):
  for c in public_cases(): self.assertNotIn('new',c); self.assertNotIn('old',c)
 def test_scoring(self):
  s=score_predictions({'WIDTH-001':{'old':'nibble = data;','new':'nibble = data[3:0];'}})
  self.assertEqual(s['patch_exact_rate'],1.0)
if __name__=='__main__': unittest.main()
