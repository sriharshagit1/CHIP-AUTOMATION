import json
from pathlib import Path
from .run_mock_blind import main as run_mock

def write_experiment_metadata():
    p=Path('evidence/experiment-metadata.json'); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps({'benchmark_version':'v1','policy':'blind evaluation','ground_truth_hidden_from_agent':True,'execution_verification_required':True},indent=2),encoding='utf-8')

if __name__=='__main__': write_experiment_metadata(); run_mock()
