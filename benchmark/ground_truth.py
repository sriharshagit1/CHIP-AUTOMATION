CASES={
'FSM-001':{'rtl':'packet_controller.sv','old':'state <= IDLE;','new':'state <= DONE;'},
'WIDTH-001':{'rtl':'width_mismatch.sv','old':'nibble = data;','new':'nibble = data[3:0];'},
'RESET-001':{'rtl':'reset_bug.sv','old':"if (rst) q <= 1'b1;",'new':"if (rst) q <= 1'b0;"},
'COUNTER-001':{'rtl':'counter_bug.sv','old':'count <= count + 2;','new':'count <= count + 1;'},
'HANDSHAKE-001':{'rtl':'handshake_bug.sv','old':'accepted <= valid & ~ready;','new':'accepted <= valid & ready;'},
'ASSERTION-001':{'rtl':'assertion_bug.sv','old':'ack <= req;','new':'ack <= 1\'b0;'},
'LATCH-001':{'rtl':'latch_bug.sv','old':'if(sel) y=a;','new':'if(sel) y=a; else y=1\'b0;'},
'MUX-001':{'rtl':'mux_bug.sv','old':'assign y = sel ? a : a;','new':'assign y = sel ? a : b;'},
'PARAM-001':{'rtl':'parameter_bug.sv','old':'assign y = a[7:0];','new':'assign y = a;'},
'CDC-001':{'rtl':'cdc_bug.sv','old':'always_ff @(posedge clk) sync_out <= async_in;','new':'logic sync_ff; always_ff @(posedge clk) begin sync_ff <= async_in; sync_out <= sync_ff; end'},
}
