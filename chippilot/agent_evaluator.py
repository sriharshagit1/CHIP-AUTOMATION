from .provider import LLMProvider
from .tool_registry import tool_schema
from .llm_prompt import SYSTEM_PROMPT, build_user_prompt

class AgentEvaluator:
    def __init__(self,provider:LLMProvider): self.provider=provider
    def request(self,case_id,log,rtl):
        messages=[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':build_user_prompt(case_id,log,rtl)}]
        return self.provider.generate(messages,tool_schema())
