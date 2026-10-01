"""Evidence-producing coverage workflow around a simulator run."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .coverage_adapter import CoverageAdapter
from .coverage_feedback import CoverageSnapshot, compare_coverage
from .simulator import Simulator


@dataclass
class CoverageRunner:
    simulator: Simulator
    adapter: CoverageAdapter

    def run(
        self,
        *,
        sources: list[str],
        top: str,
        before: CoverageSnapshot,
        timeout: int = 120,
        **coverage_kwargs: Any,
    ) -> dict[str, Any]:
        simulation = self.simulator.run(sources, top, timeout=timeout)
        if simulation.get("status") != "PASS":
            return {"status": "SIMULATION_NOT_PASS", "simulation": simulation}

        after = self.adapter.collect(self.simulator.root, **coverage_kwargs)
        delta = compare_coverage(before, after)
        accepted = delta.improved_overall
        return {
            "status": "ACCEPTED" if accepted else "REJECTED",
            "simulation": simulation,
            "coverage_before": before.total_coverage,
            "coverage_after": after.total_coverage,
            "improved": list(delta.improved),
            "regressed": list(delta.regressed),
            "unchanged": list(delta.unchanged),
        }
