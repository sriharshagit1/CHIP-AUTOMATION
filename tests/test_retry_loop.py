import unittest
from chippilot.retry_loop import run_with_retry

class TestRetryLoop(unittest.TestCase):
    def test_bounded_success(self):
        result=run_with_retry("examples/fsm/regression.log","examples/fsm/packet_controller.sv","examples/fsm/tb_packet_controller.sv",max_attempts=2)
        self.assertEqual(result["status"],"VERIFIED")
        self.assertEqual(len(result["attempts"]),1)

if __name__=="__main__":
    unittest.main()
