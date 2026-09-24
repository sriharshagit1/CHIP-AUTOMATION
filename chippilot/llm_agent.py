from dataclasses import dataclass

@dataclass
class AgentContext:
    log: str
    rtl: str
    diagnosis: str = ""
    constraints: str = "Do not modify the original workspace. Propose minimal changes only."

class LLMProvider:
    """Provider interface. A real model adapter can implement complete()."""
    def complete(self, prompt: str) -> str:
        raise NotImplementedError

class RuleBasedProvider(LLMProvider):
    def complete(self, prompt: str) -> str:
        return "No external LLM configured. Use deterministic analyzers and simulator evidence."

class ChipPilotAgent:
    def __init__(self, provider=None):
        self.provider = provider or RuleBasedProvider()

    def build_prompt(self, ctx: AgentContext) -> str:
        return f"""You are a semiconductor debugging agent.
{ctx.constraints}
Regression log:
{ctx.log}
RTL:
{ctx.rtl}
Existing diagnosis:
{ctx.diagnosis}
Return: failure class, root cause, minimal patch, verification plan.
"""

    def investigate(self, ctx: AgentContext):
        return self.provider.complete(self.build_prompt(ctx))
