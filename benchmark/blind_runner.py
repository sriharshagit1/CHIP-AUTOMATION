import json, tempfile
from pathlib import Path
from .blind_eval import public_cases, score_predictions
from .ground_truth import CASES
from .fixture_verify import verify


def apply_candidate(case_id, candidate):
    truth=CASES[case_id]
    source=Path('benchmark/cases')/truth['rtl']
    content=source.read_text(encoding='utf-8')
    old=candidate.get('old',''); new=candidate.get('new','')
    if not old or old not in content: return {'status':'INVALID_PATCH','stage':'patch'}
    patched=content.replace(old,new,1)
    try: return verify(case_id,patched)
    except Exception as exc: return {'status':'ERROR','stage':'verification','error':str(exc)}

def run_with_predictions(predictions):
    rows=[]
    for case in public_cases():
        cid=case['id']; pred=predictions.get(cid,{})
        verification=apply_candidate(cid,pred)
        rows.append({'id':cid,'prediction':pred,'verification':verification})
    return rows

if __name__=='__main__':
    print(json.dumps(run_with_predictions({}),indent=2))
