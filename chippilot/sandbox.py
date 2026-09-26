from pathlib import Path
import tempfile

class Sandbox:
    def __init__(self,source_root):
        self.source_root=Path(source_root).resolve()
        self.tmp=tempfile.TemporaryDirectory(prefix='chippilot-')
        self.root=Path(self.tmp.name)

    def read(self,relative):
        p=(self.source_root/relative).resolve()
        if self.source_root not in p.parents and p!=self.source_root: raise PermissionError('path outside repository')
        return p.read_text(encoding='utf-8')

    def write(self,relative,content):
        p=(self.root/relative).resolve()
        if self.root not in p.parents and p!=self.root: raise PermissionError('path outside sandbox')
        p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding='utf-8')
        return p

    def close(self): self.tmp.cleanup()
