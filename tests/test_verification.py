import unittest
from chippilot.verification import VerificationGate

class TestVerificationGate(unittest.TestCase):
    def test_verified(self):
        self.assertEqual(VerificationGate().evaluate({'compile':True,'target':True,'regression':True})['status'],'VERIFIED')
    def test_incomplete(self):
        r=VerificationGate().evaluate({'compile':True,'target':False,'regression':True})
        self.assertEqual(r['status'],'NOT_VERIFIED'); self.assertEqual(r['missing'],['target'])
if __name__=='__main__': unittest.main()
