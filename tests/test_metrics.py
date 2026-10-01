import unittest
from benchmark.metrics import summarize

class TestMetrics(unittest.TestCase):
    def test_summary(self):
        s=summarize([{'status':'VERIFIED','steps':2,'seconds':1.0},{'status':'FAILED','steps':4,'seconds':3.0}])
        self.assertEqual(s['cases'],2); self.assertEqual(s['completion_rate'],0.5); self.assertEqual(s['mean_steps'],3)
if __name__=='__main__': unittest.main()
