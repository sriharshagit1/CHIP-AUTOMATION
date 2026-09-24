import tempfile, unittest
from pathlib import Path
from chippilot.memory import FailureMemory, FailureRecord
from chippilot.retrieval import FailureRetriever
class TestRetrieval(unittest.TestCase):
 def test_similar_failure(self):
  with tempfile.TemporaryDirectory() as d:
   m=FailureMemory(str(Path(d)/'memory.json'))
   m.add(FailureRecord('104','fsm_transition','packet_controller','DONE IDLE','premature IDLE','PROCESS to DONE','VERIFIED'))
   r=FailureRetriever(m).find_similar('packet_controller.sv:6 ERROR expected DONE observed IDLE')
   self.assertTrue(r['matches']); self.assertEqual(r['matches'][0]['failure_id'],'104')
if __name__=='__main__': unittest.main()
