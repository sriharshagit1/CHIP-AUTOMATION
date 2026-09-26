import json
from pathlib import Path
from .failure_context import normalize_log

class FailureMemoryV2:
    def __init__(self,path='evidence/failure-memory-v2.json'):
        self.path=Path(path); self.records=[]
        if self.path.exists(): self.records=json.loads(self.path.read_text(encoding='utf-8'))
    def add(self,case_id,log,diagnosis,verification):
        ctx=normalize_log(log); rec={'case_id':case_id,'categories':ctx['categories'],'files':[x['file'] for x in ctx['files']],'diagnosis':diagnosis,'verification':verification}
        self.records.append(rec); self.path.parent.mkdir(parents=True,exist_ok=True); self.path.write_text(json.dumps(self.records,indent=2),encoding='utf-8')
    def search(self,log,limit=5):
        q=normalize_log(log); qc=set(q['categories']); qf={x['file'] for x in q['files']}; scored=[]
        for r in self.records:
            rc=set(r.get('categories',[])); rf=set(r.get('files',[])); score=2*len(qc&rc)+3*len(qf&rf)
            if score: scored.append((score,r))
        scored.sort(key=lambda x:x[0],reverse=True); return [r for _,r in scored[:limit]]
