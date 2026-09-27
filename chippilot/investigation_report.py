import json
from datetime import datetime, timezone
from pathlib import Path

def build_report(case_id, triage, candidates, patch, attempts, final_status):
    return {'schema_version':'1.0','generated_at':datetime.now(timezone.utc).isoformat(),'case_id':case_id,'executive_summary':{'final_status':final_status,'primary_candidates':candidates[:3]},'triage':triage,'proposed_patch':patch,'repair_attempts':attempts,'verification':attempts[-1].get('verification') if attempts else {'status':'NOT_RUN'},'audit_note':'Heuristic rankings are hypotheses; verification evidence determines acceptance.'}

def write_report(report,path):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(report,indent=2),encoding='utf-8'); return p
