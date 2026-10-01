import json
from pathlib import Path

class PatchStore:
    def __init__(self,root='evidence/patches'):
        self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
    def save(self,patch_id,payload):
        p=self.root/f'{patch_id}.json'
        p.write_text(json.dumps(payload,indent=2,sort_keys=True),encoding='utf-8')
        return p
