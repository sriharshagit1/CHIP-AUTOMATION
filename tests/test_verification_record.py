from chippilot.verification_execution import VerificationExecutionStep
from chippilot.uvm_execution import UVMCommandPlan
from chippilot.verification_record import record_attempt

class Result:
    status="PASS"; returncode=0; stdout="ok"; stderr=""

def test_record_accepts_coverage_improvement():
    step=VerificationExecutionStep("fsm","smoke",UVMCommandPlan("sim",("bin",)),"accept")
    e=record_attempt(run_id="r",objective="cover",candidate_id="c",step=step,result=Result(),coverage_before=.5,coverage_after=.75,improved=("fsm",))
    assert e.accepted
