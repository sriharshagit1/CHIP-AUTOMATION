import json
from datetime import datetime, timezone
from pathlib import Path

SENSITIVE_KEYS={'api_key','authorization','token','secret','password'}

def sanitize(config):
    return {k:('REDACTED' if k.lower() in SENSITIVE_KEYS else v) for k,v in config.items()}

def create_run(config,results):
    return {'schema_version':'1.0','run_id':datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),'created_at':datetime.now(timezone.utc).isoformat(),'config':sanitize(config),'results':results}

def write_run(path,run):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(run,indent=2),encoding='utf-8'); return p
