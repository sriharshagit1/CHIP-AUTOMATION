import unittest
from benchmark.run_benchmark import run_case

class TestBenchmarkRunner(unittest.TestCase):
    def test_fsm_case(self):
        result=run_case({"id":"FSM-001","status":"implemented"})
        self.assertEqual(result["status"],"VERIFIED")

if __name__=="__main__":
    unittest.main()
