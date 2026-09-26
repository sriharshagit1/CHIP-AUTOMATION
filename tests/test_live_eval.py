import unittest
from benchmark.live_eval import aggregate
class TestLiveEval(unittest.TestCase):
 def test_aggregate(self):
  s=aggregate([{'agent_status':'PATCH_PROPOSED','verification':{'status':'VERIFIED'}},{'agent_status':'PROTOCOL_ERROR','verification':{'status':'NOT_RUN'}}])
  self.assertEqual(s['cases'],2); self.assertEqual(s['verified_fix_rate'],.5); self.assertEqual(s['protocol_error_rate'],.5)
if __name__=='__main__': unittest.main()
