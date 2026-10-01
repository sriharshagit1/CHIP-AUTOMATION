import unittest
from chippilot.agent_runtime import EngineeringAgentRuntime
from chippilot.mock_provider import ScriptedProvider
from chippilot.tool_registry import ToolRegistry
from chippilot.tool_adapter import RegisteredTool

class TestRuntime(unittest.TestCase):
    def test_runtime_completes_with_evidence(self):
        r=ToolRegistry(); r.register('echo',RegisteredTool('echo','echo',lambda value:{'value':value}))
        p=ScriptedProvider([{'action':'echo','arguments':{'value':'verified'}},{'action':'finish','evidence':['echo result']}])
        rec,res=EngineeringAgentRuntime(p,r).run('inspect RTL',['rtl'])
        self.assertTrue(res.completed); self.assertEqual(rec.final_status,'VERIFIED')
if __name__=='__main__': unittest.main()
