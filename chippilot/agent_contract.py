from dataclasses import dataclass, asdict

@dataclass
class Diagnosis:
    category: str
    module: str
    root_cause: str
    evidence: list

@dataclass
class PatchProposal:
    file: str
    old: str
    new: str
    rationale: str

@dataclass
class AgentOutput:
    diagnosis: Diagnosis
    patch: PatchProposal | None
    stop_reason: str = ''

    def to_dict(self): return asdict(self)
