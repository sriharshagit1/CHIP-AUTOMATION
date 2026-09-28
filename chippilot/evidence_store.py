import json
from pathlib import Path

class EvidenceStore:
    def __init__(self,root='evidence/runs'): self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
    def save(self,run_id,payload):
        path=self.root/f'{run_id}.json'
        path.write_text(json.dumps(payload,indent=2,sort_keys=True),encoding='utf-8')
        return path
    def load(self,run_id):
        return json.loads((self.root/f'{run_id}.json').read_text(encoding='utf-8'))
