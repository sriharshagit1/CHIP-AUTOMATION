import unittest
from chippilot.llm_agent import AgentContext, ChipPilotAgent

class TestAgent(unittest.TestCase):
    def test_prompt_contains_evidence(self):
        agent=ChipPilotAgent()
        prompt=agent.build_prompt(AgentContext("ERROR expected DONE observed IDLE","PROCESS: if (complete) state <= IDLE;"))
        self.assertIn("ERROR",prompt)
        self.assertIn("Do not modify",prompt)

if __name__=="__main__":
    unittest.main()
