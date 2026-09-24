import unittest
from chippilot.debug_pipeline import debug

class TestDebugPipeline(unittest.TestCase):
    def test_verified_result(self):
        r=debug('examples/fsm/regression.log','examples/fsm/packet_controller.sv','examples/fsm/tb_packet_controller.sv')
        self.assertEqual(r.status,'VERIFIED')
        self.assertEqual(r.verification_status,'VERIFIED')
        self.assertTrue(r.evidence)

if __name__=='__main__': unittest.main()
