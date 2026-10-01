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

@dataclass(frozen=True)
class VerificationPlan:
    gaps: tuple[CoveragePoint, ...]
    candidates: tuple[TestCandidate, ...]
    steps: tuple[VerificationPlanStep, ...]

class VerificationPlanner:
    def __init__(self, max_gaps: int = 10, max_candidates: int = 5):
        self.max_gaps = max_gaps
        self.generator = CandidateGenerator(max_candidates=max_candidates)

    def plan(self, snapshot: CoverageSnapshot, *, available_sequences: Iterable[str] = ()) -> VerificationPlan:
        gaps = prioritize_gaps(snapshot, self.max_gaps)
        candidates = self.generator.generate(gaps, available_sequences=available_sequences)
        steps = tuple(VerificationPlanStep("generate_and_run", c.name, c.rationale) for c in candidates)
        return VerificationPlan(gaps, candidates, steps)

    @staticmethod
    def accept_coverage_delta(before: CoverageSnapshot, after: CoverageSnapshot) -> bool:
        return compare_coverage(before, after).improved_overall
