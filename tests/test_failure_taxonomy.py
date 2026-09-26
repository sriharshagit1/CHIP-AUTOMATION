import unittest
from benchmark.failure_taxonomy import classify
class TestFailureTaxonomy(unittest.TestCase):
 def test_verified(self): self.assertEqual(classify({'agent_status':'PATCH_PROPOSED','verification':{'status':'VERIFIED'},'patch':{}}),'VERIFIED')
 def test_protocol(self): self.assertEqual(classify({'agent_status':'PROTOCOL_ERROR','verification':{'status':'NOT_RUN'}}),'PROTOCOL_ERROR')
 def test_no_patch(self): self.assertEqual(classify({'agent_status':'PATCH_PROPOSED','verification':{'status':'NOT_RUN'}}),'NO_PATCH')
if __name__=='__main__': unittest.main()
