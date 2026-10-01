from chippilot.uvm_context import UVMContextExtractor
from chippilot.uvm_execution import UVMExecutionPlanner

def test_builds_command_without_executing():
    ctx = UVMContextExtractor().extract("class smoke_test extends uvm_test;")
    target = UVMExecutionPlanner().discover_targets(ctx)[0]
    plan = UVMExecutionPlanner().build_command(target, simulator="vcs", binary="./simv")
    assert plan.arguments[0] == "./simv"
    assert "+UVM_TESTNAME=smoke_test" in plan.arguments
    assert plan.requires_external_approval
