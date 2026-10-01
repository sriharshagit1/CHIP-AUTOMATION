from pathlib import Path
import subprocess
from .tooling import ToolSpec, EngineeringTooling

def build_builtin_tools(root='.'):
    root=Path(root).resolve()
    t=EngineeringTooling()
    t.register(ToolSpec('repo.list','rtl', 'List repository source files',runner=lambda: sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file())))
    t.register(ToolSpec('repo.read','rtl','Read a repository file',runner=lambda path: (root/path).resolve().read_text(encoding='utf-8')))
    t.register(ToolSpec('git.diff','rtl','Inspect working-tree changes',runner=lambda: subprocess.run(['git','diff'],cwd=root,text=True,capture_output=True).stdout))
    return t
