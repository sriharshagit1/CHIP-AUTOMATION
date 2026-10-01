"""Safe command planning for discovered UVM tests; never executes commands."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from .uvm_context import UVMContext

@dataclass(frozen=True)
class UVMTestTarget:
    test_name: str
    sequence_name: str | None = None
    plusargs: tuple[str, ...] = ()

@dataclass(frozen=True)
class UVMCommandPlan:
    executable: str
    arguments: tuple[str, ...]
    environment: Mapping[str, str] | None = None
    requires_external_approval: bool = True

class UVMExecutionPlanner:
    def discover_targets(self, context: UVMContext) -> tuple[UVMTestTarget, ...]:
        seq = context.sequences[0].name if context.sequences else None
        return tuple(UVMTestTarget(t, seq) for t in context.tests)

    def build_command(self, target: UVMTestTarget, *, simulator: str, binary: str, extra_args: tuple[str, ...] = ()) -> UVMCommandPlan:
        return UVMCommandPlan(simulator, (binary, f"+UVM_TESTNAME={target.test_name}", *target.plusargs, *extra_args))
