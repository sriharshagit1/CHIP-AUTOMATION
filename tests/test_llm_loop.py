import unittest
from chippilot.llm_loop import LLMDebugLoop
from chippilot.model_adapter import MockModel

class TestLLMLoop(unittest.TestCase):
    def test_mock_tool_loop(self):
        result=LLMDebugLoop(MockModel(),max_turns=2).run('ERROR expected DONE observed IDLE')
        self.assertGreaterEqual(len(result['trace']),1)
        self.assertEqual(result['trace'][0]['tool'],'read_rtl')

if __name__=='__main__': unittest.main()
