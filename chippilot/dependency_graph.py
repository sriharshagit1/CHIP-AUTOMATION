import re
from pathlib import Path
MODULE_RE=re.compile(r'\bmodule\s+([A-Za-z_][A-Za-z0-9_]*)')
INSTANCE_RE=re.compile(r'\b([A-Za-z_][A-Za-z0-9_]*)\s+(?:#\s*\([^;]*\)\s*)?([A-Za-z_][A-Za-z0-9_]*)\s*\(')

def build_graph(root='benchmark/cases'):
    root=Path(root); modules={}; edges={}
    for p in root.glob('*.sv'):
        text=p.read_text(encoding='utf-8'); found=MODULE_RE.findall(text)
        if not found: continue
        owner=found[0]; modules[owner]=str(p); edges.setdefault(owner,set())
        for typ,_ in INSTANCE_RE.findall(text):
            if typ!=owner: edges[owner].add(typ)
    return {'modules':modules,'edges':{k:sorted(v) for k,v in edges.items()}}

def reverse_dependents(graph,module):
    return sorted(owner for owner,children in graph.get('edges',{}).items() if module in children)
