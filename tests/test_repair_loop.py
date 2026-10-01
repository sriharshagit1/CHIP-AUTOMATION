import unittest
from chippilot.repair_loop import RepairLoop

class TestRepairLoop(unittest.TestCase):
    def test_rejects_unverified_then_accepts_verified(self):
        result=RepairLoop(3).evaluate([
            {'patch_id':'bad','checks':{'compile':True,'target':False,'regression':False}},
            {'patch_id':'good','checks':{'compile':True,'target':True,'regression':True}}
        ])
        self.assertEqual(result['status'],'VERIFIED')
        self.assertEqual(result['accepted_patch']['patch_id'],'good')
    def test_stops_at_budget(self):
        result=RepairLoop(2).evaluate([{'patch_id':'a','checks':{}},{'patch_id':'b','checks':{}},{'patch_id':'c','checks':{'compile':True,'target':True,'regression':True}}])
        self.assertEqual(result['status'],'NOT_VERIFIED')
        self.assertEqual(len(result['attempts']),2)
if __name__=='__main__':
    unittest.main()
