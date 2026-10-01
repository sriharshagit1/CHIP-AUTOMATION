class RuleBasedEngineeringProvider:
    """Deterministic local provider for end-to-end runtime testing."""
    def __init__(self,tool_name='repo.list'):
        self.tool_name=tool_name
        self.used=False
    def next_action(self,*,objective,context,history,tools):
        if not self.used and self.tool_name in tools:
            self.used=True
            return {'action':self.tool_name,'arguments':{}}
        return {'action':'finish','evidence':['approved tool executed']}
