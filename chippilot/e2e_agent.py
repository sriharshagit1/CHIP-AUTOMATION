from .model_tool_loop import ModelToolLoop
from .runtime_tools import RuntimeTools
from .llm_prompt import SYSTEM_PROMPT, build_user_prompt

class E2EAgent:
    def __init__(self,provider,repo_root='benchmark/cases',max_turns=8):
        self.provider=provider; self.tools=RuntimeTools(repo_root); self.max_turns=max_turns
    def investigate(self,case_id,log):
        messages=[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':build_user_prompt(case_id,log,'Use read_rtl to inspect the implementation before proposing a patch.')}]
        return ModelToolLoop(self.provider,self.tools.mapping(),self.max_turns).run(messages)
