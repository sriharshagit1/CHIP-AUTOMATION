from .agent_protocol import parse_request, patch_from_output, ProtocolError

class ModelToolLoop:
    def __init__(self,provider,tools,max_turns=8):
        self.provider=provider; self.tools=tools; self.max_turns=max_turns

    def run(self,messages):
        trace=[]
        for _ in range(self.max_turns):
            raw=self.provider.generate(messages,self.tools)
            try: req=parse_request(raw)
            except ProtocolError as e: return {'status':'PROTOCOL_ERROR','error':str(e),'trace':trace}
            if req.action=='FINAL':
                try: patch=patch_from_output(req.arguments)
                except ProtocolError as e: return {'status':'PROTOCOL_ERROR','error':str(e),'trace':trace}
                return {'status':'PATCH_PROPOSED','patch':patch,'trace':trace}
            tool=self.tools.get(req.action)
            result={'error':'unknown tool'} if tool is None else tool(**req.arguments)
            trace.append({'action':req.action,'result':result})
            messages=messages+[{'role':'assistant','content':raw},{'role':'tool','content':str(result)}]
        return {'status':'MAX_TURNS','trace':trace}
