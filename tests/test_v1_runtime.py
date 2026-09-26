import unittest, tempfile
from pathlib import Path
from chippilot.v1_runtime import ChipPilotV1
class TestV1Runtime(unittest.TestCase):
 def test_verified_case(self):
  with tempfile.TemporaryDirectory() as d:
   r=ChipPilotV1(str(Path(d)/'memory.json')).investigate('WIDTH-001',str(Path(d)/'report.json'))
   self.assertEqual(r['verification']['status'],'VERIFIED')
   self.assertEqual(r['evidence']['verdict'],'VERIFIED')
   self.assertTrue(Path(d,'report.json').exists())
if __name__=='__main__': unittest.main()
