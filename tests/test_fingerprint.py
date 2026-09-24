import unittest
from chippilot.fingerprint import fingerprint
class TestFingerprint(unittest.TestCase):
 def test_fsm(self):
  f=fingerprint('packet_controller.sv:6 ERROR expected DONE observed IDLE')
  self.assertEqual(f.category,'fsm_transition'); self.assertEqual(f.expected,'DONE'); self.assertEqual(f.observed,'IDLE'); self.assertEqual(f.module,'packet_controller'); self.assertEqual(len(f.key),16)
if __name__=='__main__': unittest.main()
