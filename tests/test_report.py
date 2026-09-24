import json, tempfile, unittest
from chippilot.report import build_report, write_report
class TestReport(unittest.TestCase):
 def test_report_roundtrip(self):
  report=build_report(fingerprint={'category':'fsm'},verification={'status':'VERIFIED'},tool_trace=[{'tool':'read_log'}])
  with tempfile.TemporaryDirectory() as d:
   path=write_report(d+'/report.json',report)
   data=json.load(open(path))
   self.assertEqual(data['schema_version'],'1.0'); self.assertEqual(data['verification']['status'],'VERIFIED'); self.assertEqual(data['tool_trace'][0]['tool'],'read_log')
if __name__=='__main__': unittest.main()
