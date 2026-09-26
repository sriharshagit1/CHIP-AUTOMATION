import json
from pathlib import Path

def summarize(path='evidence/benchmark-baseline.json'):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    rows=data['cases']; n=len(rows)
    classified=sum(r.get('diagnosis',{}).get('case_id')==r['case_id'] for r in rows)
    verified=sum(r.get('verification',{}).get('status')=='VERIFIED' for r in rows)
    return {'cases':n,'classification_accuracy':round(classified/n,3) if n else 0,'verified_fix_rate':round(verified/n,3) if n else 0,'results':rows}

if __name__=='__main__': print(json.dumps(summarize(),indent=2))
