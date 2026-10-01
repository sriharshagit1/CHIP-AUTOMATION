import json
from pathlib import Path
from .metrics import summarize

def score(path):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    summary=summarize(data.get('cases',[]))
    return {'summary':summary,'benchmark_version':'v1-agent-runtime'}
