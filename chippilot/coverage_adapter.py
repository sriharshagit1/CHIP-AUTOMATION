"""Provider-neutral coverage adapter contract.

Concrete adapters translate simulator/EDA coverage reports into the normalized
CoverageSnapshot used by ChipPilot. No commercial tool is assumed here.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Protocol

from .coverage_feedback import CoverageSnapshot, snapshot_from_rows


class CoverageAdapter(Protocol):
    name: str
    def collect(self, workspace: str | Path, **kwargs: object) -> CoverageSnapshot: ...


@dataclass(frozen=True)
class StaticCoverageAdapter:
    """Adapter for JSON-like rows supplied by a caller or future EDA bridge."""
    name: str = "static"

    def collect(self, workspace: str | Path, *, rows: Iterable[Mapping[str, object]] = (), **_: object) -> CoverageSnapshot:
        return snapshot_from_rows(rows)


@dataclass(frozen=True)
class JsonCoverageAdapter:
    """Read a generic JSON list/dict report without assuming a vendor schema."""
    name: str = "json"

    def collect(self, workspace: str | Path, *, report: str | Path, **_: object) -> CoverageSnapshot:
        import json
        path = Path(workspace) / report
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload.get("coverage", payload) if isinstance(payload, dict) else payload
        if not isinstance(rows, list):
            raise ValueError("coverage report must contain a list or a 'coverage' list")
        return snapshot_from_rows(rows)
