import unittest
from chippilot.agent_protocol import parse_request, patch_from_output, ProtocolError
class TestAgentProtocol(unittest.TestCase):
 def test_request(self): self.assertEqual(parse_request('{"action":"read_rtl","arguments":{"path":"x.sv"}}').action,'read_rtl')
 def test_reject(self):
  with self.assertRaises(ProtocolError): parse_request('{"bad":1}')
 def test_patch_contract(self):
  p=patch_from_output({'category':'fsm','module':'x','root_cause':'r','file':'x.sv','old':'a','new':'b','rationale':'minimal'})
  self.assertEqual(p['new'],'b')
if __name__=='__main__': unittest.main()
