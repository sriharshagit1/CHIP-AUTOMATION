import json
from dataclasses import dataclass

@dataclass
class ModelMessage:
    role: str
    content: str

class ModelAdapter:
    def generate(self,messages,tools):
        raise NotImplementedError

class MockModel(ModelAdapter):
    """Deterministic model used for tests and demos without API credentials."""
    def generate(self,messages,tools):
        text='\n'.join(m.content for m in messages)
        if 'expected DONE' in text and 'observed IDLE' in text:
            return json.dumps({'action':'read_rtl','arguments':{'path':'examples/fsm/packet_controller.sv','start':1,'end':20}})
        return json.dumps({'action':'STOP','arguments':{'reason':'insufficient evidence'}})

class ProviderAdapter(ModelAdapter):
    """Integration boundary for a real LLM provider; credentials stay outside the repo."""
    def __init__(self, client): self.client=client
    def generate(self,messages,tools):
        return self.client.generate(messages=messages,tools=tools)
