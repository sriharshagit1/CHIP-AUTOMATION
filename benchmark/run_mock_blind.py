import json
from .blind_eval import public_cases, score_predictions
from .blind_runner import run_with_predictions
from .mock_agent import predict

def main():
    predictions={}
    for case in public_cases():
        p=predict(case['id'],case['rtl'])
        if p: predictions[case['id']]=p
    rows=run_with_predictions(predictions)
    print(json.dumps({'score':score_predictions(predictions),'verification':rows},indent=2))

if __name__=='__main__': main()
