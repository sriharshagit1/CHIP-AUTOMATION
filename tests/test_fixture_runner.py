import shutil, unittest
from benchmark.cases.run_fixtures import run
class TestFixtures(unittest.TestCase):
 def test_intentional_bugs_fail_simulation(self):
  if not shutil.which('iverilog'): self.skipTest('iverilog not installed')
  results=run(); self.assertEqual(len(results),4)
  for r in results:
   self.assertEqual(r['compile'],'PASS'); self.assertEqual(r['simulation'],'FAIL')
if __name__=='__main__': unittest.main()
