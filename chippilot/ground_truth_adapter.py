CASES={
 'FSM-001':{'rtl':'packet_controller.sv'},'WIDTH-001':{'rtl':'width_mismatch.sv'},'RESET-001':{'rtl':'reset_bug.sv'},'COUNTER-001':{'rtl':'counter_bug.sv'},'HANDSHAKE-001':{'rtl':'handshake_bug.sv'},'ASSERTION-001':{'rtl':'assertion_bug.sv'},'LATCH-001':{'rtl':'latch_bug.sv'},'MUX-001':{'rtl':'mux_bug.sv'},'PARAM-001':{'rtl':'parameter_bug.sv'},'CDC-001':{'rtl':'cdc_bug.sv'}}
LOGS={
 'FSM-001':'packet_controller.sv:6 ERROR expected DONE observed IDLE',
 'WIDTH-001':'width_mismatch.sv:6 ERROR expected 8-bit behavior observed truncated 4-bit value',
 'RESET-001':'reset_bug.sv:8 ERROR expected q=0 observed q=1 during reset',
 'COUNTER-001':'counter_bug.sv:12 ERROR expected count=1 observed count=2',
 'HANDSHAKE-001':'handshake_bug.sv:15 ERROR valid=1 ready=1 expected accepted=1 observed accepted=0',
 'ASSERTION-001':'assertion_bug.sv:8 ERROR expected ack=0 observed ack=1',
 'LATCH-001':'latch_bug.sv:6 ERROR expected y=0 observed y=1 after sel deasserted',
 'MUX-001':'mux_bug.sv:2 ERROR expected y=b observed y=a when sel=0',
 'PARAM-001':'parameter_bug.sv:2 ERROR WIDTH=16 expected 1234 observed 0034',
 'CDC-001':'cdc_bug.sv:5 ERROR expected synchronized latency observed immediate propagation'
}
