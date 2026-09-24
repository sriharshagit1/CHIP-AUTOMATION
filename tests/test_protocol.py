import unittest
from chippilot.protocol import parse_tool_request, tool_schema

class TestProtocol(unittest.TestCase):
    def test_parse(self):
        r=parse_tool_request('{"action":"read_rtl","arguments":{"path":"x.sv","start":1,"end":20}}')
        self.assertEqual(r.action,'read_rtl')
        self.assertEqual(r.arguments['path'],'x.sv')
    def test_schema(self): self.assertGreaterEqual(len(tool_schema()),5)

if __name__=='__main__': unittest.main()
