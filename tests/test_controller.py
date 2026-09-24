import unittest
from chippilot.controller import AgentController

class TestController(unittest.TestCase):
    def test_tool_trace(self):
        c=AgentController(max_calls=3)
        self.assertIn('expected DONE',c.call('read_log','examples/fsm/regression.log'))
        self.assertIn('PROCESS',c.call('read_rtl','examples/fsm/packet_controller.sv',1,10))
        self.assertEqual(len(c.trace()),2)

if __name__=='__main__': unittest.main()
