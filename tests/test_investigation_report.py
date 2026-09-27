import unittest, tempfile
from pathlib import Path
from chippilot.investigation_report import build_report, write_report
from chippilot.report_renderer import to_markdown
class TestReport(unittest.TestCase):
    def test_report(self):
        r=build_report('X',{},['root cause'],{'new':'fix'},[{'verification':{'status':'VERIFIED'}}],'VERIFIED')
        self.assertIn('# ChipPilot Investigation',to_markdown(r))
        with tempfile.TemporaryDirectory() as d:
            self.assertTrue(write_report(r,Path(d)/'r.json').exists())
if __name__=='__main__': unittest.main()
