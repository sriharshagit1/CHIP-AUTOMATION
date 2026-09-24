from dataclasses import dataclass
from .tools import TOOL_REGISTRY

@dataclass
class ToolCall:
    name: str
    result: object

class AgentController:
    def __init__(self,max_calls=8):
        self.max_calls=max_calls
        self.history=[]
    def call(self,name,*args,**kwargs):
        if len(self.history)>=self.max_calls: raise RuntimeError('Tool-call budget exhausted')
        if name not in TOOL_REGISTRY: raise ValueError('Unknown tool: '+name)
        result=TOOL_REGISTRY[name](*args,**kwargs)
        self.history.append(ToolCall(name,result))
        return result
    def trace(self):
        return [{'tool':x.name,'result_type':type(x.result).__name__} for x in self.history]
