from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .coverage_feedback import CoveragePoint, CoverageSnapshot, compare_coverage, prioritize_gaps
from .test_generation import CandidateGenerator, TestCandidate

@dataclass(frozen=True)
class VerificationPlanStep:
    action: str
    target: str
    rationale: str
    timeout_seconds: int = 120
    acceptance: str = "simulation_pass_and_coverage_improves_without_regression"

@dataclass(frozen=True)
class VerificationPlan:
    gaps: tuple[CoveragePoint, ...]
    candidates: tuple[TestCandidate, ...]
    steps: tuple[VerificationPlanStep, ...]
    max_rounds: int = 1

class VerificationPlanner:
    def __init__(self, max_gaps: int = 10, max_candidates: int = 5, max_rounds: int = 2):
        self.max_gaps = max_gaps
        self.max_rounds = max_rounds
        self.generator = CandidateGenerator(max_candidates=max_candidates)

    def plan(self, snapshot: CoverageSnapshot, *, available_sequences: Iterable[str] = ()) -> VerificationPlan:
        gaps = prioritize_gaps(snapshot, self.max_gaps)
        candidates = self.generator.generate(gaps, available_sequences=available_sequences)
        steps = tuple(
            VerificationPlanStep(
                "generate_and_run", c.name, c.rationale, timeout_seconds=c.timeout_seconds
            )
            for c in candidates
        )
        return VerificationPlan(gaps, candidates, steps, max_rounds=self.max_rounds)

    def replan(
        self,
        before: CoverageSnapshot,
        after: CoverageSnapshot,
        *,
        available_sequences: Iterable[str] = (),
        round_number: int = 1,
    ) -> VerificationPlan | None:
        delta = compare_coverage(before, after)
        if delta.regressed:
            return None
        if delta.improved_overall:
            remaining = after
        else:
            remaining = after
        if round_number >= self.max_rounds or not prioritize_gaps(remaining, self.max_gaps):
            return None
        return self.plan(remaining, available_sequences=available_sequences)

    @staticmethod
    def accept_coverage_delta(before: CoverageSnapshot, after: CoverageSnapshot) -> bool:
        return compare_coverage(before, after).improved_overall
