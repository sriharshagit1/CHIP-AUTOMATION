from chippilot.uvm_context import UVMContextExtractor

def test_extracts_uvm_entities():
    text = "class smoke_test extends uvm_test; class main_seq extends uvm_sequence; class bus_driver extends uvm_driver; class bus_monitor extends uvm_monitor; property p_ready;"
    ctx = UVMContextExtractor().extract(text, "tb.sv")
    assert "smoke_test" in ctx.tests
    assert ctx.sequences[0].name == "main_seq"
    assert {x.kind for x in ctx.components} == {"driver", "monitor"}
    assert "p_ready" in ctx.assertions

def test_empty_context_has_low_confidence():
    assert UVMContextExtractor().extract("module foo; endmodule").confidence == "low"
