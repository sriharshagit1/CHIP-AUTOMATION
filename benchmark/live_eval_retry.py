import json, os, time
from .blind_eval import public_cases
from .blind_runner import apply_candidate
from .experiment_ledger import create_run, write_run
from .http_provider import SimpleJSONProvider
from .e2e_agent import E2EAgent
from chippilot.ground_truth_adapter import LOGS

def main():
    provider=SimpleJSONProvider(); agent=E2EAgent(provider,max_turns=8); rows=[]
    for case in public_cases():
        cid=case['id']; started=time.perf_counter(); attempts=[]; status='ERROR'
        for n in range(1,4):
            try:
                result=agent.investigate(cid,LOGS[cid]); patch=result.get('patch'); verification=apply_candidate(cid,patch) if patch else {'status':'NO_PATCH'}
            except Exception as exc:
                result={'status':'ERROR'}; patch=None; verification={'status':'ERROR','error':str(exc)}
            attempts.append({'attempt':n,'agent_status':result.get('status'),'verification':verification})
            if verification.get('status')=='VERIFIED': status='VERIFIED'; break
            status='RETRY_EXHAUSTED' if n==3 else 'RETRYING'
        rows.append({'id':cid,'status':status,'attempts':attempts,'seconds':round(time.perf_counter()-started,3)})
    summary={'cases':len(rows),'verified_after_retry':sum(r['status']=='VERIFIED' for r in rows),'retry_exhausted':sum(r['status']=='RETRY_EXHAUSTED' for r in rows)}
    run=create_run({'benchmark_version':'v1','provider':'json-http','model':os.getenv('CHIPILOT_LLM_MODEL','unset'),'max_repair_attempts':3},{'summary':summary,'cases':rows})
    write_run('evidence/experiments/live-retry-latest.json',run); print(json.dumps(run,indent=2))

if __name__=='__main__': main()
