from chippilot.coverage_feedback import CoveragePoint, CoverageSnapshot
from chippilot.uvm_context import UVMContext, UVMSequence
from chippilot.verification_execution import VerificationExecutionPlanner
from chippilot.verification_planner import VerificationPlanner

def test_binds_coverage_candidates_to_uvm_tests():
    snapshot = CoverageSnapshot((CoveragePoint("fsm", kind="branch", covered=1, total=2),))
    plan = VerificationPlanner(max_candidates=1).plan(snapshot)
    ctx = UVMContext(tests=("smoke_test",), sequences=(UVMSequence("main_seq"),), confidence="medium")
    bound = VerificationExecutionPlanner().bind(plan, ctx, simulator="vcs", binary="./simv")
    assert bound.steps[0].target_point == "fsm"
    assert bound.steps[0].test_name == "smoke_test"
    assert "+UVM_TESTNAME=smoke_test" in bound.steps[0].command.arguments

def test_low_confidence_context_blocks_binding():
    snapshot = CoverageSnapshot((CoveragePoint("fsm", covered=1, total=2),))
    plan = VerificationPlanner(max_candidates=1).plan(snapshot)
    bound = VerificationExecutionPlanner().bind(
        plan, UVMContext(confidence="low"), simulator="vcs", binary="./simv"
    )
    assert bound.blocked_reason == "insufficient_uvm_context"
