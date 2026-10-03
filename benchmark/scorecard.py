import json
from pathlib import Path
from dataclasses import dataclass
from .metrics import summarize

@dataclass
class CaseScore:
    case_id:str; verified_fix:int; patch_exact:int; regression_free:int; evidence:int; policy:int; steps:int; time_seconds:float

def aggregate(scores):
    n=len(scores)
    return {"cases":n,"verified_fix_rate":sum(x.verified_fix for x in scores)/n if n else 0,"mean_time_seconds":sum(x.time_seconds for x in scores)/n if n else 0}

def score(path):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    return {"summary":summarize(data.get("cases",[])),"benchmark_version":"v1-agent-runtime"}
