from dataclasses import dataclass, asdict

@dataclass
class DebugResult:
    status: str
    root_cause: str
    patch_status: str
    verification_status: str
    evidence: list
    tool_trace: list

    def to_dict(self): return asdict(self)
