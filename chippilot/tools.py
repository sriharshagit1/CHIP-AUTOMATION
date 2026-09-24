from pathlib import Path
import subprocess

def read_log(path):
    return Path(path).read_text(encoding='utf-8')

def read_rtl(path, start=1, end=200):
    lines=Path(path).read_text(encoding='utf-8').splitlines()
    return '\n'.join(str(i+1)+': '+line for i,line in enumerate(lines[start-1:end],start-1))

def search_repository(root, term):
    hits=[]
    for p in Path(root).rglob('*'):
        if p.is_file() and '.git' not in p.parts:
            try: text=p.read_text(encoding='utf-8')
            except (UnicodeDecodeError,OSError): continue
            if term.lower() in text.lower(): hits.append(str(p))
    return hits[:25]

def git_diff(root):
    return subprocess.run(['git','-C',root,'diff','--'],capture_output=True,text=True,timeout=10).stdout

def inspect_testbench(path): return read_rtl(path)

TOOL_REGISTRY={'read_log':read_log,'read_rtl':read_rtl,'search_repository':search_repository,'git_diff':git_diff,'inspect_testbench':inspect_testbench}
