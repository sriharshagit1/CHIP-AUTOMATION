import json
from dataclasses import dataclass

@dataclass
class ToolRequest:
    action: str
    arguments: dict

def parse_tool_request(text):
    try:
        obj=json.loads(text)
        if not isinstance(obj,dict) or 'action' not in obj: return None
        return ToolRequest(obj['action'],obj.get('arguments',{}))
    except (json.JSONDecodeError,TypeError): return None

def tool_schema():
    return [
        {'name':'read_log','description':'Read a regression log','arguments':{'path':'string'}},
        {'name':'read_rtl','description':'Read RTL source','arguments':{'path':'string','start':'integer','end':'integer'}},
        {'name':'search_repository','description':'Search repository text','arguments':{'root':'string','term':'string'}},
        {'name':'inspect_testbench','description':'Read a testbench','arguments':{'path':'string'}},
        {'name':'git_diff','description':'Inspect repository diff','arguments':{'root':'string'}}
    ]
