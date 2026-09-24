import tempfile, unittest
from pathlib import Path
from chippilot.knowledge import EngineeringKnowledge
from chippilot.memory import FailureMemory, FailureRecord

class TestKnowledge(unittest.TestCase):
    def test_combines_memory_and_git(self):
        with tempfile.TemporaryDirectory() as d:
            m=FailureMemory(str(Path(d)/'memory.json'))
            m.add(FailureRecord('1','fsm','x.sv','DONE IDLE','bad transition','fix','VERIFIED'))
            k=EngineeringKnowledge(m)
            data=k.retrieve('.', 'DONE IDLE')
            self.assertEqual(data['historical_failures'][0]['failure_id'],'1')
            self.assertIn('HISTORICAL',k.build_context(data))

if __name__=='__main__': unittest.main()
