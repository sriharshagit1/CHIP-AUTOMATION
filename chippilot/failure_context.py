import re

ERROR_PATTERNS=[('ASSERTION','assert(?:ion)?'),('WIDTH','width|truncat|overflow'),('RESET','reset|rst'),('HANDSHAKE','valid|ready|handshake'),('FSM','state|transition|idle|done'),('LATCH','latch|incomplete assignment'),('MUX','mux|select|sel'),('PARAMETER','parameter|width'),('CDC','clock domain|synchron'),('COUNTER','count|increment')]

def normalize_log(log):
    lines=[x.strip() for x in log.splitlines() if x.strip()]
    joined=' '.join(lines).lower()
    categories=[name for name,pat in ERROR_PATTERNS if re.search(pat,joined)]
    files=[]
    for line in lines:
        m=re.search(r'([\w./-]+\.sv)(?::(\d+))?',line)
        if m: files.append({'file':m.group(1),'line':int(m.group(2)) if m.group(2) else None})
    return {'categories':list(dict.fromkeys(categories)),'files':files,'lines':lines,'text':joined}
