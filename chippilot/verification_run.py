"""Run-level orchestration for bounded, auditable verification."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable
from .coverage_feedback import CoverageSnapshot
from .evidence import EvidenceStore, VerificationEvidence
from .execution_policy import ExecutionPolicy
from .run_record import RunRecord
from .uvm_context import UVMContext
from .verification_dispatch import VerificationDispatcher
from .verification_execution import VerificationExecutionPlanner
from .verification_planner import VerificationPlanner

@dataclass
class VerificationRunOrchestrator:
    planner: VerificationPlanner
    execution_planner: VerificationExecutionPlanner
    dispatcher: VerificationDispatcher
    evidence_store: EvidenceStore

    def run(self, *, objective: str, coverage: CoverageSnapshot, uvm_context: UVMContext,
            simulator: str, binary: str, policy: ExecutionPolicy, dry_run: bool = True,
            available_sequences: Iterable[str] = ()) -> RunRecord:
        record=RunRecord(objective)
        plan=self.planner.plan(coverage, available_sequences=available_sequences)
        record.event("plan_created", gaps=[g.name for g in plan.gaps], candidates=[c.candidate_id for c in plan.candidates])
        bound=self.execution_planner.bind(plan, uvm_context, simulator=simulator, binary=binary)
        record.event("execution_plan_created", steps=len(bound.steps), blocked_reason=bound.blocked_reason)
        if bound.blocked_reason:
            record.finish("BLOCKED")
            return record
        results=self.dispatcher.dispatch(bound, policy=policy, dry_run=dry_run)
        for candidate,step,result in zip(plan.candidates,bound.steps,results):
            evidence=VerificationEvidence(
                run_id=record.run_id, objective=objective, candidate_id=candidate.candidate_id,
                test_name=step.test_name, executable=step.command.executable,
                arguments=step.command.arguments, execution_status=result.status,
                returncode=result.returncode, coverage_before=coverage.total_coverage,
                coverage_after=None, accepted=False, stdout=result.stdout, stderr=result.stderr)
            path=self.evidence_store.save(evidence)
            record.event("evidence_saved", evidence_id=evidence.evidence_id, path=str(path), status=result.status)
        if dry_run:
            record.finish("DRY_RUN")
        elif results and all(r.status=="PASS" for r in results):
            record.finish("EXECUTED")
        else:
            record.finish("FAILED")
        return record
