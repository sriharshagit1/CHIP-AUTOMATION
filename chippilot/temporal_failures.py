import re
from dataclasses import dataclass

@dataclass
class FailureEvent:
    test_id: str
    timestamp: float | None
    category: str
    file: str | None
    line: int | None
    message: str

def parse_timestamped_failures(rows):
    events=[]
    for row in rows:
        log=row.get('log',''); first=log.splitlines()[0] if log else ''
        m=re.search(r'\[(\d+(?:\.\d+)?)\]',first)
        timestamp=float(m.group(1)) if m else None
        fm=re.search(r'([\w./-]+\.sv)(?::(\d+))?',log)
        events.append(FailureEvent(row.get('id','unknown'),timestamp,row.get('category','UNKNOWN'),fm.group(1) if fm else None,int(fm.group(2)) if fm and fm.group(2) else None,first))
    return events

def order_failures(events):
    known=[e for e in events if e.timestamp is not None]
    unknown=[e for e in events if e.timestamp is None]
    known.sort(key=lambda e:e.timestamp)
    return known+unknown

def primary_candidates(events,limit=5):
    ordered=order_failures(events)
    return [{'test_id':e.test_id,'timestamp':e.timestamp,'category':e.category,'file':e.file,'line':e.line,'reason':'earlier observed failure; requires causal confirmation'} for e in ordered[:limit]]
