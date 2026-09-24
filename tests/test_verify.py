import shutil
import unittest
from chippilot.patcher import propose_fsm_patch
from chippilot.verify import verify_patch

class TestVerify(unittest.TestCase):
    def test_patch_passes(self):
        if not shutil.which("iverilog"):
            self.skipTest("iverilog not installed")
        patch=propose_fsm_patch("examples/fsm/packet_controller.sv")
        result=verify_patch("examples/fsm/packet_controller.sv","examples/fsm/tb_packet_controller.sv",patch["content"])
        self.assertEqual(result["status"],"VERIFIED")
        self.assertIn("PASS",result["stdout"])

if __name__=="__main__":
    unittest.main()
