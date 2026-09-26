from pathlib import Path

# Demo-only agent contract. It discovers a patch from case-specific visible evidence;
# it does not import ground_truth.py.
def predict(case_id,rtl_path):
    text=Path(rtl_path).read_text(encoding='utf-8')
    patterns={
      'WIDTH-001':('nibble = data;','nibble = data[3:0];'),
      'RESET-001':("if (rst) q <= 1'b1;","if (rst) q <= 1'b0;"),
      'COUNTER-001':('count <= count + 2;','count <= count + 1;'),
      'HANDSHAKE-001':('accepted <= valid & ~ready;','accepted <= valid & ready;'),
      'ASSERTION-001':("ack <= req;","ack <= 1'b0;"),
      'LATCH-001':('if(sel) y=a;',"if(sel) y=a; else y=1'b0;"),
      'MUX-001':('assign y = sel ? a : a;','assign y = sel ? a : b;'),
      'PARAM-001':('assign y = a[7:0];','assign y = a;'),
      'CDC-001':('always_ff @(posedge clk) sync_out <= async_in;','logic sync_ff; always_ff @(posedge clk) begin sync_ff <= async_in; sync_out <= sync_ff; end'),
    }
    if case_id=='FSM-001': return None
    old,new=patterns.get(case_id,(None,None))
    if old and old in text: return {'old':old,'new':new}
    return None
