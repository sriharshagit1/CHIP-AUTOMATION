import re
from dataclasses import dataclass

@dataclass
class FailureContext:
    summary: str
    files: list[str]
    modules: list[str]
    signals: list[str]

class FailureContextExtractor:
    FILE=re.compile(r'([\w./-]+\.(?:sv|v|svh|vh))')
    SIGNAL=re.compile(r'\b(?:expected|observed|actual|signal|value)\s*[:=]\s*([A-Za-z_][A-Za-z0-9_$]*)',re.I)
    MODULE=re.compile(r'\bmodule\s+([A-Za-z_][A-Za-z0-9_$]*)',re.I)
    def extract(self,log):
        return FailureContext(
            summary=' '.join(log.strip().split())[:1000],
            files=sorted(set(self.FILE.findall(log))),
            modules=sorted(set(self.MODULE.findall(log))),
            signals=sorted(set(self.SIGNAL.findall(log))),
        )
