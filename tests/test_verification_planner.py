from chippilot.coverage_feedback import CoveragePoint, CoverageSnapshot
from chippilot.verification_planner import VerificationPlanner

def test_planner_targets_undercovered_points():
    snapshot = CoverageSnapshot((CoveragePoint("fsm_state",kind="branch",covered=1,total=4),CoveragePoint("done",kind="toggle",covered=1,total=1)))
    plan = VerificationPlanner().plan(snapshot, available_sequences=["main_seq"])
    assert plan.gaps[0].name == "fsm_state"
    assert plan.candidates[0].target_points == ("fsm_state",)
    assert "main_seq" in plan.candidates[0].stimulus

def test_plan_acceptance_requires_improvement_without_regression():
    before = CoverageSnapshot((CoveragePoint("a",covered=1,total=2),))
    after = CoverageSnapshot((CoveragePoint("a",covered=2,total=2),))
    assert VerificationPlanner.accept_coverage_delta(before, after)
