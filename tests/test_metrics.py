import unittest
from benchmark.metrics import summarize
class TestMetrics(unittest.TestCase):
    def test_recovery_metric(self):
        rows=[{'status':'VERIFIED','attempts':[{'verification':{'status':'FAIL'}},{'verification':{'status':'VERIFIED'}}]}]
        s=summarize(rows); self.assertEqual(s['first_pass_verified_rate'],0); self.assertEqual(s['verified_after_repair_rate'],1); self.assertEqual(s['mean_attempts'],2)
if __name__=='__main__': unittest.main()
