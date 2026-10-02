import json
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import asdict, dataclass, field
import hashlib

def write_report(path, failure, diagnosis, verification):
    report={
        "timestamp":datetime.now(timezone.utc).isoformat(),
        "failure":failure,
        "diagnosis":diagnosis,
        "verification":verification,
        "claim_policy":"ChipPilot reports VERIFIED only when the verification command exits successfully."
    }
    Path(path).write_text(json.dumps(report,indent=2),encoding="utf-8")
    return report

@dataclass(frozen=True)
class VerificationEvidence:
    run_id: str
    objective: str
    candidate_id: str
    test_name: str
    executable: str
    arguments: tuple[str, ...]
    execution_status: str
    returncode: int | None
    coverage_before: float | None = None
    coverage_after: float | None = None
    improved_points: tuple[str, ...] = ()
    regressed_points: tuple[str, ...] = ()
    accepted: bool = False
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    stdout: str = ""
    stderr: str = ""

    @property
    def evidence_id(self) -> str:
        return hashlib.sha256(json.dumps(asdict(self), sort_keys=True).encode()).hexdigest()[:20]

class EvidenceStore:
    def __init__(self, root="evidence/verification"):
        self.root=Path(root)

    def save(self, evidence: VerificationEvidence):
        self.root.mkdir(parents=True, exist_ok=True)
        path=self.root/f"{evidence.evidence_id}.json"
        path.write_text(json.dumps(asdict(evidence),indent=2,sort_keys=True),encoding="utf-8")
        return path
