from dataclasses import dataclass
from .context import collect_context, build_context_prompt
from .analyzer import diagnose
from .patcher import propose_fsm_patch
from .verify import verify_patch

@dataclass
class AgentResult:
    diagnosis: object
    patch: object
    verification: object
    prompt: str

def run_agent(log_path, rtl_path, tb_path):
    ctx=collect_context(log_path,rtl_path)
    failure=type("Failure",(),{"message":ctx["log"]})()
    diagnosis=diagnose(failure,ctx["rtl"])
    patch=propose_fsm_patch(rtl_path)
    verification={"status":"NOT_RUN"}
    if patch["status"]=="PROPOSED":
        verification=verify_patch(rtl_path,tb_path,patch["content"])
    return AgentResult(diagnosis,patch,verification,build_context_prompt(ctx))
