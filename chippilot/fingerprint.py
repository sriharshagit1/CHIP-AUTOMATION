import hashlib
import re
from dataclasses import dataclass, asdict

@dataclass
class FailureFingerprint:
    category: str
    module: str
    signal: str
    expected: str
    observed: str
    assertion: str
    file: str
    line: int | None

    @property
    def key(self):
        raw='|'.join([self.category,self.module,self.signal,self.expected,self.observed,self.assertion,self.file,str(self.line)])
        return hashlib.sha256(raw.lower().encode()).hexdigest()[:16]

    def to_dict(self): return asdict(self) | {'key':self.key}

def fingerprint(log):
    text=log.strip()
    file=''; line=None
    m=re.search(r'([\w./-]+\.sv):(\d+)',text)
    if m: file,line=m.group(1),int(m.group(2))
    exp=re.search(r'expected\s+([^,\n]+)',text,re.I)
    obs=re.search(r'observed\s+([^,\n]+)',text,re.I)
    expected=exp.group(1).strip() if exp else ''
    observed=obs.group(1).strip() if obs else ''
    category='fsm_transition' if 'expected done' in text.lower() and 'observed idle' in text.lower() else 'unknown'
    module=file.rsplit('/',1)[-1].replace('.sv','') if file else ''
    return FailureFingerprint(category,module,'',expected,observed,text[:300],file,line)
