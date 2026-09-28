from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class EDATool:
    name: str
    stage: str
    description: str
    runner: Callable[..., Any]

class EDAToolCatalog:
    def __init__(self): self._tools={}
    def register(self,tool):
        self._tools[tool.name]=tool
    def for_stage(self,stage):
        return [t for t in self._tools.values() if t.stage==stage]
    def stages(self):
        return sorted({t.stage for t in self._tools.values()})
    def manifest(self):
        return [{'name':t.name,'stage':t.stage,'description':t.description} for t in self._tools.values()]
