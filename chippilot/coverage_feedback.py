from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

@dataclass(frozen=True)
class CoveragePoint:
    name: str
    kind: str = "unknown"
    covered: int = 0
    total: int = 1
    weight: float = 1.0
    target: float = 1.0

    @property
    def percentage(self) -> float:
        if self.total <= 0:
            return 1.0
        return max(0.0, min(1.0, self.covered / self.total))

    @property
    def gap(self) -> float:
        return max(0.0, self.target - self.percentage)

@dataclass(frozen=True)
class CoverageSnapshot:
    points: tuple[CoveragePoint, ...]

    @property
    def total_coverage(self) -> float:
        if not self.points:
            return 0.0
        weight = sum(p.weight for p in self.points)
        return sum(p.percentage * p.weight for p in self.points) / weight

@dataclass(frozen=True)
class CoverageDelta:
    improved: tuple[str, ...]
    regressed: tuple[str, ...]
    unchanged: tuple[str, ...]
    before: float
    after: float

    @property
    def improved_overall(self) -> bool:
        return self.after > self.before and not self.regressed

def snapshot_from_rows(rows: Iterable[Mapping[str, object]]) -> CoverageSnapshot:
    points = []
    for row in rows:
        name = str(row.get("name") or row.get("point") or "").strip()
        if not name:
            continue
        points.append(CoveragePoint(
            name=name,
            kind=str(row.get("kind") or row.get("type") or "unknown"),
            covered=int(row.get("covered", 0)),
            total=int(row.get("total", 1)),
            weight=float(row.get("weight", 1.0)),
            target=float(row.get("target", 1.0)),
        ))
    return CoverageSnapshot(tuple(points))

def compare_coverage(before: CoverageSnapshot, after: CoverageSnapshot) -> CoverageDelta:
    left, right = {p.name:p for p in before.points}, {p.name:p for p in after.points}
    improved, regressed, unchanged = [], [], []
    for name in sorted(set(left) | set(right)):
        bp = left[name].percentage if name in left else 0.0
        ap = right[name].percentage if name in right else 0.0
        if ap > bp: improved.append(name)
        elif ap < bp: regressed.append(name)
        else: unchanged.append(name)
    return CoverageDelta(tuple(improved), tuple(regressed), tuple(unchanged), before.total_coverage, after.total_coverage)

def prioritize_gaps(snapshot: CoverageSnapshot, limit: int = 10) -> tuple[CoveragePoint, ...]:
    return tuple(sorted((p for p in snapshot.points if p.gap > 0), key=lambda p:(-p.gap*p.weight,p.kind,p.name))[:limit])
