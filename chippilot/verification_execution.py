"""Connect verification planning to UVM command planning and evidence.

This module only composes plans. It deliberately does not bypass the execution
policy or launch EDA commands itself.
"""
from __future__ import annotations

from dataclasses import dataclass

from .coverage_feedback import CoverageSnapshot
from .uvm_context import UVMContext
from .uvm_execution import UVMCommandPlan, UVMExecutionPlanner
from .verification_planner import VerificationPlan


@dataclass(frozen=True)
class VerificationExecutionStep:
    target_point: str
    test_name: str
    command: UVMCommandPlan
    acceptance: str


@dataclass(frozen=True)
class VerificationExecutionPlan:
    steps: tuple[VerificationExecutionStep, ...]
    confidence: str
    blocked_reason: str | None = None


class VerificationExecutionPlanner:
    def __init__(self, uvm: UVMExecutionPlanner | None = None):
        self.uvm = uvm or UVMExecutionPlanner()

    def bind(
        self,
        plan: VerificationPlan,
        context: UVMContext,
        *,
        simulator: str,
        binary: str,
    ) -> VerificationExecutionPlan:
        if context.confidence == "low":
            return VerificationExecutionPlan((), context.confidence, "insufficient_uvm_context")

        targets = self.uvm.discover_targets(context)
        if not targets:
            return VerificationExecutionPlan((), context.confidence, "no_uvm_tests_discovered")

        steps = []
        for candidate, target in zip(plan.candidates, targets):
            command = self.uvm.build_command(target, simulator=simulator, binary=binary)
            steps.append(VerificationExecutionStep(
                candidate.target_points[0],
                target.test_name,
                command,
                plan.steps[len(steps)].acceptance,
            ))
        return VerificationExecutionPlan(tuple(steps), context.confidence)
