import json
from dataclasses import dataclass
from .tools import TOOL_REGISTRY

@dataclass
class ToolRequest:
    action: str
    arguments: dict

class ProtocolError(Exception):
    pass

def parse_tool_request(text):
    try:
        obj=json.loads(text)
    except (json.JSONDecodeError,TypeError) as e:
        raise ProtocolError("Malformed JSON tool request") from e
    if not isinstance(obj,dict) or not isinstance(obj.get("action"),str):
        raise ProtocolError("Tool request requires a string action")
    args=obj.get("arguments",{})
    if not isinstance(args,dict):
        raise ProtocolError("arguments must be an object")
    if obj["action"] not in TOOL_REGISTRY:
        raise ProtocolError("Tool is not registered")
    return ToolRequest(obj["action"],args)

def execute_tool_request(text, controller):
    req=parse_tool_request(text)
    return controller.call(req.action,**req.arguments)

def tool_schema():
    return [
        {"name":"read_log","arguments":{"path":"string"}},
        {"name":"read_rtl","arguments":{"path":"string","start":"integer","end":"integer"}},
        {"name":"search_repository","arguments":{"root":"string","term":"string"}},
        {"name":"inspect_testbench","arguments":{"path":"string"}},
        {"name":"git_diff","arguments":{"root":"string"}}
    ]
