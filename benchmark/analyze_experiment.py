import json
from collections import Counter
from pathlib import Path
from .failure_taxonomy import classify

def analyze(path):
    data=json.loads(Path(path).read_text(encoding='utf-8'))
    results=data.get('results',{})
    rows=results.get('cases',results if isinstance(results,list) else [])
    counts=Counter(classify(r) for r in rows)
    return {'cases':len(rows),'failure_modes':dict(counts),'verified':counts.get('VERIFIED',0)}

if __name__=='__main__':
    import sys
    print(json.dumps(analyze(sys.argv[1]),indent=2))
