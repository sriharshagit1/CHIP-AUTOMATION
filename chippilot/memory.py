import json
from pathlib import Path
from dataclasses import dataclass, asdict

@dataclass
class FailureRecord:
    failure_id: str
    category: str
    module: str
    signature: str
    root_cause: str
    patch_summary: str
    verification: str
    commit: str = ''

class FailureMemory:
    def __init__(self,path='evidence/failure_memory.json'):
        self.path=Path(path)
        self.path.parent.mkdir(parents=True,exist_ok=True)
        self.records=[]
        if self.path.exists():
            self.records=[FailureRecord(**x) for x in json.loads(self.path.read_text())]

    def add(self,record):
        self.records.append(record)
        self.path.write_text(json.dumps([asdict(x) for x in self.records],indent=2),encoding='utf-8')

    def search(self,query,limit=5):
        q=query.lower()
        scored=[]
        for r in self.records:
            hay=' '.join([r.category,r.module,r.signature,r.root_cause,r.patch_summary]).lower()
            score=sum(1 for token in q.split() if token and token in hay)
            if score: scored.append((score,r))
        scored.sort(key=lambda x:x[0],reverse=True)
        return [r for _,r in scored[:limit]]
