import shutil, unittest
from chippilot.fixture_patcher import propose
from chippilot.fixture_verify import verify
CASES=[('WIDTH-001','benchmark/cases/width_mismatch.sv'),('RESET-001','benchmark/cases/reset_bug.sv'),('COUNTER-001','benchmark/cases/counter_bug.sv'),('HANDSHAKE-001','benchmark/cases/handshake_bug.sv')]
class TestFixturePatches(unittest.TestCase):
 def test_all_patches_verify(self):
  if not shutil.which('iverilog'): self.skipTest('iverilog not installed')
  for case,path in CASES:
   patch=propose(case,path); self.assertEqual(patch['status'],'PROPOSED'); self.assertEqual(verify(case,patch['content'])['status'],'VERIFIED')
if __name__=='__main__': unittest.main()
