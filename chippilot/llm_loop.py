from .model_adapter import ModelMessage
from .protocol import execute_tool_request, ProtocolError, tool_schema
from .controller import AgentController

class LLMDebugLoop:
    def __init__(self,model,max_turns=6,max_tool_calls=8):
        self.model=model
        self.max_turns=max_turns
        self.controller=AgentController(max_tool_calls)

    def run(self,initial_context):
        messages=[ModelMessage('system','You are ChipPilot. Use only registered tools. Never claim verification without execution evidence.'),ModelMessage('user',initial_context)]
        trace=[]
        for _ in range(self.max_turns):
            raw=self.model.generate(messages,tool_schema())
            try:
                req=__import__('chippilot.protocol',fromlist=['parse_tool_request']).parse_tool_request(raw)
            except ProtocolError as e:
                trace.append({'error':str(e)})
                break
            if req.action=='STOP':
                return {'status':'STOPPED','trace':trace,'reason':req.arguments.get('reason','model stop')}
            try:
                result=execute_tool_request(raw,self.controller)
            except Exception as e:
                trace.append({'tool':req.action,'error':str(e)})
                break
            observation=str(result)[:12000]
            trace.append({'tool':req.action,'observation':observation})
            messages.append(ModelMessage('assistant',raw))
            messages.append(ModelMessage('tool',observation))
        return {'status':'MAX_TURNS','trace':trace}
