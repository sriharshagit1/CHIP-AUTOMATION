from .planner import Planner
from .run_record import RunRecord
from .agent_loop import AgentLoop

class EngineeringAgentRuntime:
    def __init__(self,provider,registry,planner=None,max_steps=8):
        self.provider=provider; self.registry=registry; self.planner=planner or Planner()
        self.loop=AgentLoop(provider,registry,max_steps=max_steps)
    def run(self,objective,stages):
        record=RunRecord(objective); plan=self.planner.plan(objective,stages)
        record.event("plan",steps=[s.__dict__ for s in plan.steps])
        result=self.loop.run(objective,{"plan":[s.__dict__ for s in plan.steps]})
        record.event("agent_result",completed=result.completed,reason=result.reason,steps=result.steps)
        record.finish("VERIFIED" if result.completed else result.reason); return record,result

AgentRuntime=EngineeringAgentRuntime
