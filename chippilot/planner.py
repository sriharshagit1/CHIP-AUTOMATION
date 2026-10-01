from dataclasses import dataclass, field
from .engineering_plan import STAGES

@dataclass
class PlanStep:
    stage: str
    action: str
    success_condition: str
    tool: str | None = None

@dataclass
class AgentPlan:
    objective: str
    steps: list[PlanStep] = field(default_factory=list)

    def add(self,stage,action,success_condition,tool=None):
        if stage not in STAGES: raise ValueError(f'unsupported stage: {stage}')
        self.steps.append(PlanStep(stage,action,success_condition,tool))

class Planner:
    def plan(self,objective,stages):
        p=AgentPlan(objective)
        for stage in stages:
            p.add(stage,f'investigate {objective}',f'obtain evidence for {stage}')
        return p
