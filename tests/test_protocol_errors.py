import unittest
from chippilot.protocol import parse_tool_request, ProtocolError

class TestProtocolErrors(unittest.TestCase):
    def test_bad_json(self):
        with self.assertRaises(ProtocolError): parse_tool_request('not json')
    def test_unknown_tool(self):
        with self.assertRaises(ProtocolError): parse_tool_request('{"action":"shell","arguments":{}}')
    def test_bad_arguments(self):
        with self.assertRaises(ProtocolError): parse_tool_request('{"action":"read_log","arguments":[] }')

if __name__=='__main__': unittest.main()
