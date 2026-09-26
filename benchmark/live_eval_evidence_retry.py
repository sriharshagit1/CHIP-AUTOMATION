import json, os, time
from .blind_eval import public_cases
from .blind_runner import apply_candidate
from .experiment_ledger import create_run, write_run
from .http_provider import SimpleJSONProvider
from .e2e_agent import E2EAgent
from .repair_context import build_feedback
from chippilot.ground_truth_adapter import LOGS

def main():
    provider=SimpleJSONProvider(); agent=E2EAgent(provider,max_turns=8); rows=[]
    for case in public_cases():
        cid=case['id']; messages=None; attempts=[]; started=time.perf_counter()
        for n in range(1,4):
            result=agent.investigate(cid,LOGS[cid]) if n==1 else agent.investigate(cid,LOGS[cid]+'\nREPAIR FEEDBACK:\n'+json.dumps(build_feedback(cid,verification)))
            patch=result.get('patch'); verification=apply_candidate(cid,patch) if patch else {'status':'NO_PATCH'}
            attempts.append({'attempt':n,'agent_status':result.get('status'),'patch':patch,'verification':verification})
            if verification.get('status')=='VERIFIED': break
        rows.append({'id':cid,'attempts':attempts,'final_status':attempts[-1]['verification'].get('status'),'seconds':round(time.perf_counter()-started,3)})
    summary={'cases':len(rows),'first_pass_verified':sum(r['attempts'][0]['verification'].get('status')=='VERIFIED' for r in rows),'verified_after_retry':sum(r['final_status']=='VERIFIED' for r in rows),'mean_attempts':sum(len(r['attempts']) for r in rows)/len(rows) if rows else 0}
    run=create_run({'benchmark_version':'v1','provider':'json-http','model':os.getenv('CHIPILOT_LLM_MODEL','unset'),'max_turns':8,'max_repair_attempts':3},{'summary':summary,'cases':rows})
    write_run('evidence/experiments/live-evidence-retry-latest.json',run); print(json.dumps(run,indent=2))

if __name__=='__main__': main()
