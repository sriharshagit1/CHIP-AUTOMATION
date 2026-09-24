from chippilot.patcher import propose_fsm_patch

def test_patch_proposal():
    r=propose_fsm_patch("examples/fsm/packet_controller.sv")
    assert r["status"] == "PROPOSED"
    assert "state <= DONE" in r["content"]
