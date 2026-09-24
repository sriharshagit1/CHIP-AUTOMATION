import unittest
from chippilot.report_markdown import markdown_report, html_report
class TestReadableReport(unittest.TestCase):
 def test_markdown(self):
  text=markdown_report({'failure_fingerprint':{'category':'fsm_transition','module':'packet_controller'},'diagnosis':{'root_cause':'premature IDLE'},'patch':{'status':'PROPOSED'},'verification':{'status':'VERIFIED'},'evidence':{'verdict':'VERIFIED','evidence_score':1},'tool_trace':[{'tool':'read_log'}]})
  self.assertIn('# ChipPilot Investigation Report',text); self.assertIn('VERIFIED',text); self.assertIn('premature IDLE',text)
 def test_html(self): self.assertIn('<html>',html_report({}))
if __name__=='__main__': unittest.main()
