from dataclasses import dataclass

@dataclass
class ToolSpec:
    name: str
    description: str
    arguments: dict

TOOLS=[
 ToolSpec('read_rtl','Read RTL inside the repository',{'path':'string'}),
 ToolSpec('git_history','Inspect recent commits',{'limit':'integer'}),
 ToolSpec('git_diff','Inspect a commit diff',{'commit':'string'}),
 ToolSpec('verify','Run isolated verification',{'case_id':'string'}),
]

def tool_schema(): return [t.__dict__ for t in TOOLS]
