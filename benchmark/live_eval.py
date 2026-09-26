import json, os, time
from .blind_eval import public_cases
from .blind_runner import apply_candidate
from .experiment_ledger import create_run, write_run
from .http_provider import SimpleJSONProvider
from .e2e_agent import E2EAgent
from chippilot.ground_truth_adapter import LOGS

def aggregate(rows):
    n=len(rows)
    return {'cases':n,'patch_proposed_rate':sum(r['agent_status']=='PATCH_PROPOSED' for r in rows)/n if n else 0,'verified_fix_rate':sum(r['verification'].get('status')=='VERIFIED' for r in rows)/n if n else 0,'protocol_error_rate':sum(r['agent_status']=='PROTOCOL_ERROR' for r in rows)/n if n else 0}

def main():
    provider=SimpleJSONProvider()
    agent=E2EAgent(provider)
    rows=[]
    for case in public_cases():
        cid=case['id']; started=time.perf_counter()
        try:
            result=agent.investigate(cid,LOGS[cid]); patch=result.get('patch')
            verification=apply_candidate(cid,patch) if patch else {'status':'NOT_RUN'}
            status=result.get('status','UNKNOWN')
        except Exception as exc:
            status='ERROR'; patch=None; verification={'status':'ERROR','error':str(exc)}
        rows.append({'id':cid,'agent_status':status,'patch':patch,'verification':verification,'seconds':round(time.perf_counter()-started,3)})
    run=create_run({'benchmark_version':'v1','provider':'json-http','model':os.getenv('CHIPILOT_LLM_MODEL','unset'),'max_turns':8},{'summary':aggregate(rows),'cases':rows})
    path=write_run('evidence/experiments/live-latest.json',run); print(json.dumps(run,indent=2)); return path

if __name__=='__main__': main()
