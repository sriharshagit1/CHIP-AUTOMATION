from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from .test_generation import TestCandidate

class TestArtifactStore:
    def __init__(self, root: str | Path = "evidence/tests"):
        self.root = Path(root)

    def save_candidate(self, candidate: TestCandidate, *, result: dict[str, Any] | None = None) -> Path:
        self.root.mkdir(parents=True, exist_ok=True)
        path = self.root / f"{candidate.candidate_id}.json"
        payload = {"candidate_id":candidate.candidate_id,"name":candidate.name,"kind":candidate.kind,"target_points":list(candidate.target_points),"stimulus":list(candidate.stimulus),"rationale":candidate.rationale,"files":list(candidate.files),"max_iterations":candidate.max_iterations,"result":result or {}}
        path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        return path
