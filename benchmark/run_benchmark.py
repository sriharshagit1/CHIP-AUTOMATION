import json, subprocess, sys, time
from pathlib import Path

def run_case(case):
    start=time.perf_counter()
    if case["id"]=="FSM-001":
        cmd=[sys.executable,"-m","chippilot.cli","examples/fsm/regression.log","--verify","--report","/tmp/chippilot-report.json"]
    else:
        return {"id":case["id"],"status":"PLANNED"}
    p=subprocess.run(cmd,capture_output=True,text=True)
    elapsed=time.perf_counter()-start
    return {"id":case["id"],"status":"VERIFIED" if "Verification: VERIFIED" in p.stdout else "FAIL","seconds":round(elapsed,3),"stdout":p.stdout,"stderr":p.stderr}

if __name__=="__main__":
    cases=json.loads(Path("benchmark/cases.json").read_text())
    results=[run_case(c) for c in cases]
    print(json.dumps({"results":results},indent=2))
