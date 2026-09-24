import unittest
from chippilot.policy import SafetyPolicy, can_claim_verified

class TestPolicy(unittest.TestCase):
    def test_no_verification_no_claim(self):
        self.assertFalse(can_claim_verified({"status":"NOT_RUN"},SafetyPolicy()))
    def test_verified_requires_execution(self):
        self.assertTrue(can_claim_verified({"status":"VERIFIED"},SafetyPolicy()))

if __name__=="__main__": unittest.main()
