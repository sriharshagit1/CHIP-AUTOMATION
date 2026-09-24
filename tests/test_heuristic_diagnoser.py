import unittest
from chippilot.heuristic_diagnoser import classify

class TestHeuristicDiagnoser(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(classify("expected DONE observed IDLE")["case_id"],"FSM-001")
        self.assertEqual(classify("valid=1 ready=1 accepted=0")["case_id"],"HANDSHAKE-001")
        self.assertEqual(classify("expected count 1 observed 2")["case_id"],"COUNTER-001")

if __name__=="__main__": unittest.main()
