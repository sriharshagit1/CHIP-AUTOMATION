import re
from dataclasses import dataclass

@dataclass
class FailureContext:
    summary:str; files:list[str]; modules:list[str]; signals:list[str]

class FailureContextExtractor:
    FILE=re.compile(r'([\\w./-]+\\.(?:sv|v|svh|vh))')
    SIGNAL=re.compile(r'\\b(?:expected|observed|actual|signal|value)\\s*[:=]\\s*([A-Za-z_][A-Za-z0-9_$]*)',re.I)
    MODULE=re.compile(r'\\bmodule\\s+([A-Za-z_][A-Za-z0-9_$]*)',re.I)
    def extract(self,log):
        return FailureContext(' '.join(log.strip().split())[:1000],sorted(set(self.FILE.findall(log))),sorted(set(self.MODULE.findall(log))),sorted(set(self.SIGNAL.findall(log)))

def normalize_log(log):
    files=[]
    for m in re.finditer(r'([\\w./-]+\\.(?:sv|v|svh|vh)):(\\d+)',log):
        files.append({"file":m.group(1),"line":int(m.group(2))})
    categories=[]
    low=log.lower()
    if any(x in low for x in ("expected","observed","idle","done","transition")): categories.append("FSM")
    return {"categories":categories,"files":files,"summary":" ".join(log.split())}
