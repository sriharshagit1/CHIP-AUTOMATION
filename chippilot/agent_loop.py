from dataclasses import dataclass, field
from typing import Any, Callable

@dataclass
class LoopState:
    objective: str
    steps: list[dict[str,Any]] = field(default_factory=list)
    completed: bool = False
    reason: str = ''

class AgentLoop:
    """Provider-agnostic bounded tool loop.

    A model/provider supplies a sequence of action dictionaries. The loop,
    not the model, owns tool execution, budgets and completion evidence.
    """
    def __init__(self,provider,registry,max_steps=8,policy=None):
        self.provider=provider
        self.registry=registry
        self.max_steps=max_steps
        self.policy=policy

    def run(self,objective,context=None):
        state=LoopState(objective)
        context=context or {}
        for step in range(self.max_steps):
            decision=self.provider.next_action(
                objective=objective,
                context=context,
                history=state.steps,
                tools=self.registry.describe(),
            )
            if not isinstance(decision,dict):
                state.reason='PROTOCOL_ERROR'; break
            action=decision.get('action')
            if action=='finish':
                evidence=decision.get('evidence',[])
                if not evidence:
                    state.reason='COMPLETION_WITHOUT_EVIDENCE'; break
                state.completed=True; state.reason='EVIDENCE_BACKED_COMPLETION'; break
            if not action:
                state.reason='INVALID_ACTION'; break
            try:
                tool=self.registry.get(action)
                result=tool.run(**(decision.get('arguments') or {}))
                event={'step':step+1,'action':action,'result':result}
                state.steps.append(event)
                context['last_result']=result
            except Exception as exc:
                state.steps.append({'step':step+1,'action':action,'error':str(exc)})
                state.reason='TOOL_ERROR'
                break
        if not state.completed and not state.reason:
            state.reason='STEP_BUDGET_EXCEEDED'
        return state
