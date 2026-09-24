from dataclasses import dataclass
from .agent_loop import run_agent

@dataclass
class Attempt:
    number: int
    diagnosis: str
    patch_status: str
    verification: str

def run_with_retry(log_path, rtl_path, tb_path, max_attempts=2):
    attempts=[]
    for n in range(1,max_attempts+1):
        result=run_agent(log_path,rtl_path,tb_path)
        attempts.append(Attempt(n,result.diagnosis.root_cause,result.patch["status"],result.verification["status"]))
        if result.verification["status"]=="VERIFIED":
            return {"status":"VERIFIED","attempts":[a.__dict__ for a in attempts]}
    return {"status":"UNVERIFIED","attempts":[a.__dict__ for a in attempts]}
