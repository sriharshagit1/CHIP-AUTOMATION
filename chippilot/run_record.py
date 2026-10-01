from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid

@dataclass
class RunRecord:
    objective: str
    run_id: str = field(default_factory=lambda: uuid.uuid4().hex)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    events: list[dict] = field(default_factory=list)
    final_status: str = 'RUNNING'

    def event(self,kind,**data): self.events.append({'kind':kind,'data':data})
    def finish(self,status): self.final_status=status
