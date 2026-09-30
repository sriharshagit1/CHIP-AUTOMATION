from .engineering_plan import EngineeringPlan
from .eda_tooling import EDAToolCatalog
from .agent_contract import Investigation
from .policy import AgentPolicy

class EngineeringOrchestrator:
    def __init__(self,catalog=None,policy=None):
        self.catalog=catalog or EDAToolCatalog()
        self.policy=policy or AgentPolicy()

    def plan(self,objective,stages):
        plan=EngineeringPlan(objective)
        for stage in stages:
            tools=self.catalog.for_stage(stage)
            tool=tools[0].name if tools else None
            plan.add(stage,f'investigate objective at {stage}',tool)
        plan.require_approval('merge_or_apply_design_change')
        return plan

    def start_investigation(self,case_id,objective):
        return Investigation(case_id,objective)
