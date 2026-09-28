from pathlib import Path
class RepositoryAdapter:
    def __init__(self,root='.'): self.root=Path(root).resolve()
    def read(self,relative):
        p=(self.root/relative).resolve()
        if self.root not in p.parents and p != self.root: raise ValueError('path escapes repository root')
        return p.read_text(encoding='utf-8')
    def list_files(self,suffixes=('.sv','.v','.svh','.vh','.tcl','.py')):
        return sorted(str(p.relative_to(self.root)) for p in self.root.rglob('*') if p.is_file() and p.suffix in suffixes)
