from dataclasses import dataclass

@dataclass
class PlanStep:
    tool: str
    args: tuple

class DebugPlanner:
    def plan(self, log_path, rtl_path, tb_path):
        return [
            PlanStep('read_log',(log_path,)),
            PlanStep('read_rtl',(rtl_path,)),
            PlanStep('inspect_testbench',(tb_path,)),
        ]

    def next_after_failure(self, tool_result):
        text=str(tool_result).lower()
        if 'expected done' in text and 'observed idle' in text:
            return 'diagnose_fsm'
        return 'request_llm_reasoning'
