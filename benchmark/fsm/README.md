# FSM-001

Intentional bug: completion transitions to IDLE instead of DONE.

Expected diagnosis: the PROCESS state must transition to DONE when complete is asserted.

Expected patch: replace the PROCESS completion transition with DONE.

Verification: examples/fsm/tb_packet_controller.sv
