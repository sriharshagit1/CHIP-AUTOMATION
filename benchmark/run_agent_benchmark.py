import json, time
from pathlib import Path
from chippilot.benchmark_agent import run_case

CASES={
 'WIDTH-001':'width_mismatch.sv:6 ERROR expected 8-bit behavior observed truncated 4-bit value',
 'RESET-001':'reset_bug.sv:8 ERROR expected q=0 observed q=1 during reset',
 'COUNTER-001':'counter_bug.sv:12 ERROR expected count=1 observed count=2',
 'HANDSHAKE-001':'handshake_bug.sv:15 ERROR valid=1 ready=1 expected accepted=1 observed accepted=0',
 'FSM-001':'packet_controller.sv:6 ERROR expected DONE observed IDLE',
}

def run():
    results=[]
    for case,log in CASES.items():
        started=time.perf_counter()
        try:
            result=run_case(case,log)
            result['seconds']=round(time.perf_counter()-started,6)
        except Exception as exc:
            result={'case_id':case,'status':'ERROR','error':str(exc),'seconds':round(time.perf_counter()-started,6)}
        results.append(result)
    return results

def main():
    results=run()
    out=Path('evidence/benchmark-baseline.json'); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps({'benchmark':'chipilot-baseline-v1','cases':results},indent=2),encoding='utf-8')
    print(json.dumps(results,indent=2))

if __name__=='__main__': main()
