import json
from pathlib import Path
from datetime import datetime, timezone

def build_report(*, fingerprint=None, knowledge=None, diagnosis=None, patch=None, verification=None, evidence=None, tool_trace=None):
    return {
        'schema_version':'1.0',
        'generated_at':datetime.now(timezone.utc).isoformat(),
        'failure_fingerprint':fingerprint,
        'knowledge':knowledge,
        'diagnosis':diagnosis,
        'patch':patch,
        'verification':verification,
        'evidence':evidence,
        'tool_trace':tool_trace or []
    }

def write_report(path, report):
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(report,indent=2,default=str),encoding='utf-8')
    return str(p)
