import re

PATTERNS=[
 ("WIDTH-001",r"expected.*8.*observed.*4|width|truncat","width/truncation"),
 ("RESET-001",r"reset|expected.*0.*observed.*1","reset behavior"),
 ("COUNTER-001",r"count|counter|expected.*1.*observed.*2","counter increment"),
 ("HANDSHAKE-001",r"valid|ready|handshake|accepted","valid/ready handshake"),
 ("FSM-001",r"expected.*done.*observed.*idle|state|fsm","FSM transition"),
]

def classify(log,rtl=""):
    text=(log+"\n"+rtl).lower()
    for case,pattern,reason in PATTERNS:
        if re.search(pattern,text,re.I):
            return {"case_id":case,"category":reason,"method":"heuristic"}
    return {"case_id":"UNKNOWN","category":"unknown","method":"heuristic"}
