import json
from pathlib import Path

def load_cases(path="benchmark/cases.json"):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def summary(path="benchmark/cases.json"):
    cases=load_cases(path)
    implemented=sum(1 for c in cases if c.get("status")=="implemented" or c.get("implemented",False))
    return {"total":len(cases),"implemented":implemented,"planned":len(cases)-implemented}

if __name__=="__main__": print(json.dumps(summary(),indent=2))
