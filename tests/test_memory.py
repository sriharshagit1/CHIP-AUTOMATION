import tempfile, unittest
from pathlib import Path
from chippilot.memory import FailureMemory, FailureRecord

class TestMemory(unittest.TestCase):
    def test_store_and_search(self):
        with tempfile.TemporaryDirectory() as d:
            m=FailureMemory(str(Path(d)/'memory.json'))
            m.add(FailureRecord('104','fsm','packet_controller','expected DONE observed IDLE','premature IDLE','PROCESS to DONE','VERIFIED','abc'))
            hits=m.search('packet_controller DONE IDLE')
            self.assertEqual(len(hits),1)
            self.assertEqual(hits[0].failure_id,'104')

if __name__=='__main__': unittest.main()
