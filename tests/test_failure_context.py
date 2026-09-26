import unittest
from chippilot.failure_context import normalize_log
class TestFailureContext(unittest.TestCase):
    def test_normalizes(self):
        x=normalize_log('packet_controller.sv:6 ERROR expected DONE observed IDLE')
        self.assertIn('FSM',x['categories']); self.assertEqual(x['files'][0]['file'],'packet_controller.sv'); self.assertEqual(x['files'][0]['line'],6)
if __name__=='__main__': unittest.main()
