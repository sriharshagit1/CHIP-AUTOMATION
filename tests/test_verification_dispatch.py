from chippilot.eda_execution import EDAExecutionAdapter
from chippilot.execution_policy import ExecutionPolicy
from chippilot.verification_dispatch import VerificationDispatcher
from chippilot.verification_execution import VerificationExecutionPlan, VerificationExecutionStep
from chippilot.uvm_execution import UVMCommandPlan

def test_dispatch_defaults_to_dry_run():
    step = VerificationExecutionStep("fsm","smoke",UVMCommandPlan("python",("simv",)), "accept")
    plan = VerificationExecutionPlan((step,),"medium")
    result = VerificationDispatcher(EDAExecutionAdapter()).dispatch(plan, policy=ExecutionPolicy(allow_external=True))
    assert result[0].status == "DRY_RUN"
