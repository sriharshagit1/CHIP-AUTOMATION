import unittest
from chippilot.e2e_agent import E2EAgent
from chippilot.local_provider import LocalRuleProvider
class TestE2EAgent(unittest.TestCase):
 def test_local_provider_returns_patch(self):
  r=E2EAgent(LocalRuleProvider()).investigate('WIDTH-001','width_mismatch.sv:6 ERROR expected 8-bit behavior observed truncated 4-bit value')
  self.assertEqual(r['status'],'PATCH_PROPOSED'); self.assertEqual(r['patch']['new'],'nibble = data[3:0];')
if __name__=='__main__': unittest.main()
