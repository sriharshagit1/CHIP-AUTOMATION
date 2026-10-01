import unittest
from chippilot.rule_provider import RuleBasedEngineeringProvider

class TestRuleProvider(unittest.TestCase):
    def test_protocol(self):
        p=RuleBasedEngineeringProvider('x')
        self.assertEqual(p.next_action(objective='o',context={},history=[],tools={'x':'tool'})['action'],'x')
        self.assertEqual(p.next_action(objective='o',context={},history=[],tools={'x':'tool'})['action'],'finish')
if __name__=='__main__':
    unittest.main()
