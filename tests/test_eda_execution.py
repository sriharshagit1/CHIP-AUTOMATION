from chippilot.eda_execution import EDAExecutionAdapter
from chippilot.execution_policy import ExecutionPolicy

def test_external_execution_requires_approval():
    result = EDAExecutionAdapter().execute("echo", ("hello",), policy=ExecutionPolicy())
    assert result.status == "APPROVAL_REQUIRED"

def test_dry_run_does_not_launch_command():
    result = EDAExecutionAdapter().execute("definitely-not-a-real-tool", (), policy=ExecutionPolicy(allow_external=True), dry_run=True)
    assert result.status == "DRY_RUN"

def test_available_command_can_execute_when_approved():
    result = EDAExecutionAdapter().execute("python", ("-c", "print('ok')"), policy=ExecutionPolicy(allow_external=True))
    assert result.status == "PASS"
