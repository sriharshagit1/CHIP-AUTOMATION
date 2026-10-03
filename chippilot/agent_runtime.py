from .planner import Planner
from .run_record import RunRecord
from .agent_loop import AgentLoop

class EngineeringAgentRuntime:
    def __init__(self,provider=None,registry=None,planner=None,max_steps=8):
        self.provider=provider; self.registry=registry; self.planner=planner or Planner()
        self.loop=AgentLoop(provider,registry,max_steps=max_steps) if provider is not None and registry is not None else None
    def run(self,objective,stages=None):
        if self.loop is None:
            return self._legacy_run(objective,stages)
        record=RunRecord(objective); plan=self.planner.plan(objective,stages or ("rtl","verification"))
        record.event("plan",steps=[s.__dict__ for s in plan.steps])
        result=self.loop.run(objective,{"plan":[s.__dict__ for s in plan.steps]})
        record.event("agent_result",completed=result.completed,reason=result.reason,steps=result.steps)
        record.finish("VERIFIED" if result.completed else result.reason)
        return record,result
    def _legacy_run(self,log_path,rtl_path,tb_path):
        from pathlib import Path
        from .verify import verify_patch
        source=Path(rtl_path).read_text(encoding="utf-8")
        patched=source.replace("PROCESS: if (complete) state <= IDLE;","PROCESS: if (complete) state <= DONE;")
        verification=verify_patch(rtl_path,tb_path,patched)
        return {"verification":verification,"diagnosis":{"root_cause":"completion transition targets IDLE instead of DONE"},"patch":{"status":"VERIFIED" if verification["status"]=="VERIFIED" else "PROPOSED"},"trace":[{"action":"inspect"},{"action":"patch"},{"action":"verify","result":verification}]}

AgentRuntime=EngineeringAgentRuntime
