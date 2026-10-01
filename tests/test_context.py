import unittest, tempfile
from pathlib import Path
from chippilot.rtl_index import RTLIndex
from chippilot.failure_context import FailureContextExtractor

class TestContext(unittest.TestCase):
    def test_rtl_index(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'a.sv'; p.write_text('module top; child u1(.a(a)); endmodule\nmodule child; endmodule')
            x=RTLIndex(d).build()
            self.assertIn('top',x); self.assertIn('child',x)
    def test_failure_extraction(self):
        f=FailureContextExtractor().extract('packet_controller.sv expected: DONE observed: IDLE')
        self.assertIn('packet_controller.sv',f.files); self.assertIn('DONE',f.signals)
if __name__=='__main__': unittest.main()
