from dataclasses import dataclass
from typing import Any, Callable

@dataclass
class ToolSpec:
    name: str
    stage: str
    description: str
    write: bool = False
    external: bool = False
    runner: Callable[..., Any] | None = None

class EngineeringTooling:
    def __init__(self): self.tools={}
    def register(self,spec):
        if spec.name in self.tools: raise ValueError(f'duplicate tool: {spec.name}')
        self.tools[spec.name]=spec
    def manifest(self):
        return [{'name':s.name,'stage':s.stage,'description':s.description,'write':s.write,'external':s.external} for s in self.tools.values()]
    def execute(self,name,policy,**kwargs):
        spec=self.tools[name]
        if spec.write and not policy.allow_write: return {'status':'APPROVAL_REQUIRED','tool':name}
        if spec.external and not policy.allow_external: return {'status':'ENVIRONMENT_APPROVAL_REQUIRED','tool':name}
        if spec.runner is None: return {'status':'ADAPTER_NOT_CONFIGURED','tool':name}
        return {'status':'OK','tool':name,'result':spec.runner(**kwargs)}
