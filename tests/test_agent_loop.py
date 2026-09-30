import unittest
from chippilot.agent_loop import AgentLoop
from chippilot.tool_registry import ToolRegistry
from chippilot.tool_adapter import RegisteredTool
from chippilot.mock_provider import ScriptedProvider

class TestAgentLoop(unittest.TestCase):
    def registry(self):
        r=ToolRegistry()
        r.register('echo',RegisteredTool('echo','returns input',lambda value: {'value':value}))
        return r
    def test_tool_then_evidence_backed_finish(self):
        p=ScriptedProvider([{'action':'echo','arguments':{'value':'ok'}},{'action':'finish','evidence':['tool result'] }])
        s=AgentLoop(p,self.registry()).run('test')
        self.assertTrue(s.completed); self.assertEqual(len(s.steps),1)
    def test_no_evidence_cannot_finish(self):
        p=ScriptedProvider([{'action':'finish','evidence':[]}])
        s=AgentLoop(p,self.registry()).run('test')
        self.assertFalse(s.completed); self.assertEqual(s.reason,'COMPLETION_WITHOUT_EVIDENCE')
    def test_budget(self):
        p=ScriptedProvider([{'action':'echo','arguments':{'value':'x'}}]*5)
        s=AgentLoop(p,self.registry(),max_steps=2).run('test')
        self.assertFalse(s.completed); self.assertEqual(s.reason,'STEP_BUDGET_EXCEEDED')
if __name__=='__main__': unittest.main()
