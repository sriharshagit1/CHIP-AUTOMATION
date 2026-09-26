import unittest, tempfile
from pathlib import Path
from chippilot.failure_memory_v2 import FailureMemoryV2
from chippilot.context_with_memory import build_context_with_memory
class TestContextMemory(unittest.TestCase):
    def test_only_verified_history_is_included(self):
        with tempfile.TemporaryDirectory() as d:
            m=FailureMemoryV2(str(Path(d)/'m.json'))
            log='packet_controller.sv:6 state ERROR'
            m.add('VER','packet_controller.sv:6 state ERROR',{'root_cause':'x'},{'status':'VERIFIED'})
            m.add('UNVER','packet_controller.sv:7 state ERROR',{'root_cause':'y'},{'status':'FAIL'})
            c=build_context_with_memory('NEW',log,m)
            ids=[x['record']['case_id'] for x in c['historical_matches']]
            self.assertEqual(ids,['VER'])
if __name__=='__main__': unittest.main()
