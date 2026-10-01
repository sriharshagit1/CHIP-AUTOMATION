"""Dispatch approved verification command plans through the EDA boundary."""
from __future__ import annotations
from dataclasses import dataclass
from .eda_execution import EDAExecutionAdapter, ExecutionResult
from .execution_policy import ExecutionPolicy
from .verification_execution import VerificationExecutionPlan

@dataclass
class VerificationDispatcher:
    adapter: EDAExecutionAdapter

    def dispatch(self, plan: VerificationExecutionPlan, *, policy: ExecutionPolicy,
                 timeout_seconds: int = 120, dry_run: bool = True) -> tuple[ExecutionResult, ...]:
        if plan.blocked_reason:
            return (ExecutionResult("BLOCKED", reason=plan.blocked_reason),)
        results = []
        for step in plan.steps:
            command = step.command
            result = self.adapter.execute(command.executable, command.arguments, policy=policy,
                                          environment=command.environment,
                                          timeout_seconds=timeout_seconds, dry_run=dry_run)
            results.append(result)
            if result.status not in {"PASS", "DRY_RUN"}:
                break
        return tuple(results)
