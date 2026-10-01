"""Controlled execution adapters for external EDA commands."""
from __future__ import annotations
from dataclasses import dataclass
import subprocess
from typing import Mapping, Sequence
from .execution_policy import ExecutionPolicy

@dataclass(frozen=True)
class ExecutionResult:
    status: str
    returncode: int | None = None
    stdout: str = ""
    stderr: str = ""
    reason: str = ""

class EDAExecutionAdapter:
    name = "generic"
    def execute(self, executable: str, arguments: Sequence[str], *, policy: ExecutionPolicy,
                environment: Mapping[str, str] | None = None, timeout_seconds: int = 120,
                dry_run: bool = False) -> ExecutionResult:
        decision = policy.decide("run_eda")
        if not decision.allowed:
            return ExecutionResult("APPROVAL_REQUIRED", reason=decision.reason)
        if dry_run:
            return ExecutionResult("DRY_RUN", reason="execution permitted; command not launched")
        try:
            completed = subprocess.run([executable, *arguments], text=True, capture_output=True,
                                       timeout=timeout_seconds,
                                       env=dict(environment) if environment else None)
        except FileNotFoundError:
            return ExecutionResult("UNAVAILABLE", reason=f"executable not found: {executable}")
        except subprocess.TimeoutExpired as exc:
            return ExecutionResult("TIMEOUT", stdout=(exc.stdout or "")[-4000:],
                                   stderr=(exc.stderr or "")[-4000:], reason="EDA command exceeded timeout")
        return ExecutionResult("PASS" if completed.returncode == 0 else "FAIL",
                               completed.returncode, completed.stdout[-4000:], completed.stderr[-4000:])
