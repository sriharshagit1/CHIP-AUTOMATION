from chippilot.agent_runtime import EngineeringAgentRuntime
from chippilot.mock_provider import ScriptedProvider
from chippilot.tool_registry import ToolRegistry
from chippilot.tool_adapter import RegisteredTool
from .metrics import summarize

def run():
    registry=ToolRegistry()
    registry.register('inspect',RegisteredTool('inspect','inspect fixture',lambda case_id:{'case_id':case_id,'observed':'failure'}))
    rows=[]
    for case_id in ['FSM-001','WIDTH-001','RESET-001','COUNTER-001','HANDSHAKE-001']:
        provider=ScriptedProvider([
            {'action':'inspect','arguments':{'case_id':case_id}},
            {'action':'finish','evidence':['inspection result']}
        ])
        record,state=EngineeringAgentRuntime(provider,registry).run(f'Investigate {case_id}',['rtl','verification'])
        rows.append({'id':case_id,'status':'VERIFIED' if state.completed else 'FAILED','steps':len(state.steps),'seconds':0.0,'reason':state.reason})
    return {'cases':rows,'summary':summarize(rows)}

if __name__=='__main__':
    import json
    print(json.dumps(run(),indent=2))
