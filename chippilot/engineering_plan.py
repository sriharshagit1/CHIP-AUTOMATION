from dataclasses import dataclass, field

STAGES=('rtl','verification','synthesis','sta','dft','post_silicon')

@dataclass
class EngineeringPlan:
    objective: str
    stages: list[str] = field(default_factory=list)
    actions: list[dict] = field(default_factory=list)
    approval_points: list[str] = field(default_factory=list)

    def add(self,stage,action,tool=None):
        if stage not in STAGES: raise ValueError(f'unsupported engineering stage: {stage}')
        self.stages.append(stage)
        self.actions.append({'stage':stage,'action':action,'tool':tool})
    def require_approval(self,point): self.approval_points.append(point)
