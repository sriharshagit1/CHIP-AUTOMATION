from chippilot.log_parser import parse_failure
from chippilot.analyzer import diagnose

def test_failure_parser():
    log="examples/fsm/packet_controller.sv:6 ERROR expected DONE observed IDLE"
    f=parse_failure(log)
    assert f.file.endswith("packet_controller.sv")
    assert f.line == 6
    assert f.category == "simulation_error"

def test_fsm_diagnosis():
    rtl=open("examples/fsm/packet_controller.sv",encoding="utf-8").read()
    f=parse_failure(open("examples/fsm/regression.log",encoding="utf-8").read())
    d=diagnose(f,rtl)
    assert "DONE" in d.root_cause
    assert d.confidence > 0.8
