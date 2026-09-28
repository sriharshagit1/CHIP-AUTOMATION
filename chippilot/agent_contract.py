from dataclasses import dataclass, field
from typing import Any
@dataclass
class ToolResult:
    tool: str
    status: str
    data: dict[str, Any] = field(default_factory=dict)
    evidence: list[str] = field(default_factory=list)
@dataclass
class Investigation:
    case_id: str
    objective: str
    observations: list[dict[str, Any]] = field(default_factory=list)
    hypotheses: list[dict[str, Any]] = field(default_factory=list)
    actions: list[dict[str, Any]] = field(default_factory=list)
    verification: list[ToolResult] = field(default_factory=list)
    def add_observation(self, source, value): self.observations.append({'source':source,'value':value})
    def add_hypothesis(self, statement, evidence=None): self.hypotheses.append({'statement':statement,'evidence':evidence or []})
    def add_action(self, action, target): self.actions.append({'action':action,'target':target})
