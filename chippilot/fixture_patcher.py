from pathlib import Path

PATCHES={
 'WIDTH-001': ('nibble = data;','nibble = data[3:0];'),
 'RESET-001': ("if (rst) q <= 1'b1;","if (rst) q <= 1'b0;"),
 'COUNTER-001': ('count <= count + 2;','count <= count + 1;'),
 'HANDSHAKE-001': ('accepted <= valid & ~ready;','accepted <= valid & ready;'),
}

def propose(case_id,path):
    if case_id not in PATCHES: return {'status':'UNSUPPORTED'}
    old,new=PATCHES[case_id]
    content=Path(path).read_text(encoding='utf-8')
    if old not in content: return {'status':'NOT_APPLICABLE','reason':'expected buggy pattern not found'}
    return {'status':'PROPOSED','case_id':case_id,'old':old,'new':new,'content':content.replace(old,new,1)}
