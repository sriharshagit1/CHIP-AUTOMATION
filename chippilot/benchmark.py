import json
from pathlib import Path

def load_cases(path="benchmark/cases.json"):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def summary(path="benchmark/cases.json"):
    cases=load_cases(path)
    implemented=sum(c["status"]=="implemented" for c in cases)
    return {"total":len(cases),"implemented":implemented,"planned":len(cases)-implemented}

if __name__=="__main__":
    print(json.dumps(summary(),indent=2))
