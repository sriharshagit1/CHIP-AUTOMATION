import json
import os
from urllib.request import Request, urlopen
from .provider import LLMProvider

class SimpleJSONProvider(LLMProvider):
    """Minimal JSON-over-HTTP adapter. Endpoint must return {"output": "..."}."""
    def __init__(self,endpoint=None,api_key=None,timeout=60):
        self.endpoint=endpoint or os.environ.get('CHIPILOT_LLM_ENDPOINT','')
        self.api_key=api_key or os.environ.get('CHIPILOT_API_KEY','')
        self.timeout=timeout
        if not self.endpoint: raise ValueError('CHIPILOT_LLM_ENDPOINT is required')

    def generate(self,messages,tools):
        payload=json.dumps({'messages':messages,'tools':tools}).encode()
        headers={'Content-Type':'application/json'}
        if self.api_key: headers['Authorization']='Bearer '+self.api_key
        req=Request(self.endpoint,data=payload,headers=headers,method='POST')
        with urlopen(req,timeout=self.timeout) as resp:
            data=json.loads(resp.read().decode('utf-8'))
        if not isinstance(data,dict) or not isinstance(data.get('output'),str):
            raise ValueError('provider response must contain string field output')
        return data['output']
