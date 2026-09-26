import json
from pathlib import Path
from .run_all import TB
from .ground_truth import CASES

def public_cases():
    # Exposes only executable inputs, never expected patch text.
    root=Path(__file__).parent/'cases'
    return [{'id':case,'rtl':str(root/rtl),'testbench':str(root/tb)} for case,(rtl,tb) in TB.items()]

def score_predictions(predictions):
    rows=[]
    for case,pred in predictions.items():
        truth=CASES.get(case,{})
        rows.append({'id':case,'patch_exact':pred.get('new')==truth.get('new'),'expected_pattern_found':pred.get('old')==truth.get('old')})
    n=len(rows)
    return {'cases':n,'patch_exact_rate':sum(r['patch_exact'] for r in rows)/n if n else 0,'details':rows}

if __name__=='__main__': print(json.dumps(public_cases(),indent=2))
