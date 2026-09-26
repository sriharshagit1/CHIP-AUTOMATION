from pathlib import Path

def build_feedback(case_id,verification,repo_root='benchmark/cases'):
    rtl_name={'WIDTH-001':'width_mismatch.sv','RESET-001':'reset_bug.sv','COUNTER-001':'counter_bug.sv','HANDSHAKE-001':'handshake_bug.sv','FSM-001':'packet_controller.sv','ASSERTION-001':'assertion_bug.sv','LATCH-001':'latch_bug.sv','MUX-001':'mux_bug.sv','PARAM-001':'parameter_bug.sv','CDC-001':'cdc_bug.sv'}.get(case_id)
    rtl=''
    if rtl_name:
        p=Path(repo_root)/rtl_name
        if p.exists(): rtl=p.read_text(encoding='utf-8')
    return {'case_id':case_id,'verification':verification,'rtl_context':rtl,'instruction':'Inspect the observed failure and RTL context. Revise only if evidence supports a change. Never claim verification.'}
