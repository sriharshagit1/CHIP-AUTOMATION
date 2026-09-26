import os

class LLMProvider:
    def generate(self,messages,tools):
        raise NotImplementedError

class JSONHTTPProvider(LLMProvider):
    """Provider-neutral HTTP boundary; deployment supplies endpoint and credentials."""
    def __init__(self,endpoint=None,api_key=None):
        self.endpoint=endpoint or os.getenv('CHIPILOT_LLM_ENDPOINT','')
        self.api_key=api_key or os.getenv('CHIPILOT_API_KEY','')
        if not self.endpoint: raise ValueError('CHIPILOT_LLM_ENDPOINT is required')

    def generate(self,messages,tools):
        raise NotImplementedError('Deployment-specific HTTP client required')
