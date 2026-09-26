import unittest, tempfile
from pathlib import Path
from benchmark.experiment_ledger import create_run, write_run
class TestLedger(unittest.TestCase):
 def test_redacts_secrets(self):
  with tempfile.TemporaryDirectory() as d:
   run=create_run({'model':'test','api_key':'secret'},[{'id':'A'}]); p=write_run(Path(d)/'run.json',run)
   self.assertEqual(run['config']['api_key'],'REDACTED'); self.assertTrue(p.exists())
if __name__=='__main__': unittest.main()
