import json, os
from .experiment_ledger import create_run, write_run
from .blind_eval import public_cases

def config():
    return {'benchmark_version':'v1','provider':os.getenv('CHIPILOT_LLM_PROVIDER','unset'),'model':os.getenv('CHIPILOT_LLM_MODEL','unset'),'max_turns':int(os.getenv('CHIPILOT_MAX_TURNS','8'))}

def main():
    cases=[{'id':c['id'],'status':'NOT_RUN','reason':'real provider not configured'} for c in public_cases()]
    run=create_run(config(),cases); path=write_run('evidence/experiments/latest.json',run); print(json.dumps(run,indent=2)); return path

if __name__=='__main__': main()
