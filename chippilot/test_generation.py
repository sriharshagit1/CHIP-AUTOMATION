from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
from typing import Iterable

@dataclass(frozen=True)
class TestCandidate:
    name: str
    kind: str
    target_points: tuple[str, ...]
    stimulus: tuple[str, ...]
    rationale: str
    files: tuple[str, ...] = ()
    max_iterations: int = 1

    @property
    def candidate_id(self) -> str:
        payload = "|".join((self.name,self.kind,",".join(self.target_points),",".join(self.stimulus),self.rationale))
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

@dataclass
class CandidateGenerator:
    max_candidates: int = 5

    def generate(self, gaps: Iterable[object], *, available_sequences: Iterable[str] = ()) -> tuple[TestCandidate, ...]:
        sequences = tuple(available_sequences)
        result = []
        for gap in gaps:
            name = str(getattr(gap, "name", "coverage_gap"))
            kind = str(getattr(gap, "kind", "unknown"))
            base = sequences[0] if sequences else "existing_sequence"
            result.append(TestCandidate(
                name=f"cover_{name}", kind=kind, target_points=(name,),
                stimulus=(f"exercise {name}", f"vary stimulus around {name}", f"reuse {base}"),
                rationale=f"Target under-covered {kind} point {name}; prefer existing verification infrastructure before creating new topology."
            ))
            if len(result) >= self.max_candidates: break
        return tuple(result)

@dataclass(frozen=True)
class TestGenerationPlan:
    candidates: tuple[TestCandidate, ...] = field(default_factory=tuple)
    stop_on_regression: bool = True
