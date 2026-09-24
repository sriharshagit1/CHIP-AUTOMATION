import json
from pathlib import Path
from datetime import datetime, timezone

def write_report(path, failure, diagnosis, verification):
    report={
        "timestamp":datetime.now(timezone.utc).isoformat(),
        "failure":failure,
        "diagnosis":diagnosis,
        "verification":verification,
        "claim_policy":"ChipPilot reports VERIFIED only when the verification command exits successfully."
    }
    Path(path).write_text(json.dumps(report,indent=2),encoding="utf-8")
    return report
