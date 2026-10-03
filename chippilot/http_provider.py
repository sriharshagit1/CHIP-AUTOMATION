import json
from urllib.request import Request,urlopen

class OpenAICompatibleProvider:
    def __init__(self,api_key=None,base_url=None,model=None,timeout=60):
        import os
        self.api_key=api_key or os.getenv("CHIPILOT_API_KEY")
        self.base_url=(base_url or os.getenv("CHIPILOT_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
        self.model=model or os.getenv("CHIPILOT_LLM_MODEL","unset"); self.timeout=timeout
    def next_action(self,*,objective,context,history,tools):
        if not self.api_key: raise RuntimeError("CHIPILOT_API_KEY is not configured")
        payload={"model":self.model,"messages":[{"role":"system","content":"Return exactly one JSON object with action, arguments, optional evidence."},{"role":"user","content":json.dumps({"objective":objective,"context":context,"history":history,"tools":tools})}],"temperature":0,"response_format":{"type":"json_object"}}
        req=Request(self.base_url+"/chat/completions",data=json.dumps(payload).encode(),headers={"Authorization":"Bearer "+self.api_key,"Content-Type":"application/json"},method="POST")
        with urlopen(req,timeout=self.timeout) as response: body=json.loads(response.read().decode())
        content=body["choices"][0]["message"]["content"]; action=json.loads(content)
        if not isinstance(action,dict) or not action.get("action"): raise ValueError("provider returned invalid action object")
        return action

class SimpleJSONProvider(OpenAICompatibleProvider):
    def generate(self,context,tools):
        if not self.api_key: raise RuntimeError("CHIPILOT_API_KEY is not configured")
        payload={"model":self.model,"messages":[{"role":"user","content":json.dumps({"context":context,"tools":tools})}]}
        req=Request(self.base_url+"/chat/completions",data=json.dumps(payload).encode(),headers={"Authorization":"Bearer "+self.api_key,"Content-Type":"application/json"},method="POST")
        with urlopen(req,timeout=self.timeout) as response: body=json.loads(response.read().decode())
        if "output" in body: return body["output"]
        return body["choices"][0]["message"]["content"]
