from dataclasses import dataclass, asdict
from pathlib import Path
import json, subprocess, sys

@dataclass
class CaseResult:
    case_id: str
    diagnosis: str
    patch: str
    verification: str
    status: str

def evaluate_fsm():
    cmd=[sys.executable,"-m","chippilot.cli","examples/fsm/regression.log","--verify","--report","/tmp/chippilot-eval.json"]
    p=subprocess.run(cmd,capture_output=True,text=True)
    verified="Verification: VERIFIED" in p.stdout
    return CaseResult("FSM-001","FSM transition root cause","FSM completion patch","PASS" if verified else "FAIL","VERIFIED" if verified else "FAIL")

def run():
    results=[evaluate_fsm()]
    payload={"cases":[asdict(r) for r in results],"metrics":{"verified_fix_rate":sum(r.status=="VERIFIED" for r in results)/len(results)}}
    Path("benchmark/results.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
    return payload

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
