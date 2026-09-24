import unittest
from chippilot.agent_runtime import AgentRuntime

class TestRuntime(unittest.TestCase):
    def test_runtime_verifies_fsm(self):
        result=AgentRuntime().run('examples/fsm/regression.log','examples/fsm/packet_controller.sv','examples/fsm/tb_packet_controller.sv')
        self.assertEqual(result['verification']['status'],'VERIFIED')
        self.assertGreaterEqual(len(result['trace']),3)

if __name__=='__main__': unittest.main()
