import json
from dataclasses import dataclass

@dataclass
class ToolRequest:
    action: str
    arguments: dict

class ProtocolError(ValueError): pass

def parse_request(raw):
    try: data=json.loads(raw) if isinstance(raw,str) else raw
    except Exception as e: raise ProtocolError(f'invalid JSON: {e}')
    if not isinstance(data,dict) or not isinstance(data.get('action'),str) or not isinstance(data.get('arguments',{}),dict):
        raise ProtocolError('request must contain action and object arguments')
    return ToolRequest(data['action'],data['arguments'])

def patch_from_output(data):
    required=['category','module','root_cause','file','old','new','rationale']
    if not all(isinstance(data.get(k),str) for k in required): raise ProtocolError('patch proposal missing required string fields')
    return {k:data[k] for k in required}
