from pathlib import Path
import re

class RTLIndex:
    MODULE=re.compile(r'\bmodule\s+([A-Za-z_][A-Za-z0-9_$]*)')
    INSTANCE=re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_$]*)\s+(?:#\s*\([^;]*\)\s*)?([A-Za-z_][A-Za-z0-9_$]*)\s*\(',re.M)
    def __init__(self,root='.'): self.root=Path(root).resolve()
    def build(self):
        modules={}
        for p in self.root.rglob('*'):
            if not p.is_file() or p.suffix not in {'.sv','.v','.svh','.vh'}: continue
            try: text=p.read_text(encoding='utf-8',errors='ignore')
            except OSError: continue
            names=self.MODULE.findall(text)
            for name in names:
                modules[name]={'file':str(p.relative_to(self.root)),'instances':[]}
            for parent in names:
                modules[parent]['instances']=sorted(set(self.INSTANCE.findall(text)))
        return modules
