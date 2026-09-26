import unittest, tempfile
from pathlib import Path
from chippilot.failure_memory_v2 import FailureMemoryV2
class TestMemoryV2(unittest.TestCase):
    def test_similarity(self):
        with tempfile.TemporaryDirectory() as d:
            m=FailureMemoryV2(str(Path(d)/'m.json')); m.add('A','packet_controller.sv:6 state ERROR',{'root_cause':'fsm'}, {'status':'VERIFIED'})
            self.assertEqual(m.search('packet_controller.sv:8 state ERROR')[0]['case_id'],'A')
if __name__=='__main__': unittest.main()
