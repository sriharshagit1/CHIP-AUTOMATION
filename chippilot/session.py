from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

@dataclass
class InvestigationSession:
    case_id: str
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    events: list = field(default_factory=list)

    def record(self,event,**data): self.events.append({'event':event,'data':data,'at':datetime.now(timezone.utc).isoformat()})
