import unittest
from chippilot.evidence_score import EvidenceScore
class TestEvidenceScore(unittest.TestCase):
 def test_unverified(self): self.assertEqual(EvidenceScore().verdict(),'INVESTIGATE')
 def test_hypothesis(self): self.assertEqual(EvidenceScore(root_cause_evidence=.8).verdict(),'SUPPORTED_HYPOTHESIS')
 def test_verified_requires_execution(self): self.assertEqual(EvidenceScore(compile_pass=1,targeted_test_pass=1,regression_pass=1).verdict(),'VERIFIED')
if __name__=='__main__': unittest.main()
