import unittest
from chippilot.agent_loop import run_agent

class TestAgentLoop(unittest.TestCase):
    def test_end_to_end_fsm(self):
        result=run_agent("examples/fsm/regression.log","examples/fsm/packet_controller.sv","examples/fsm/tb_packet_controller.sv")
        self.assertEqual(result.patch["status"],"PROPOSED")
        self.assertEqual(result.verification["status"],"VERIFIED")
        self.assertIn("REGRESSION LOG",result.prompt)

if __name__=="__main__":
    unittest.main()
