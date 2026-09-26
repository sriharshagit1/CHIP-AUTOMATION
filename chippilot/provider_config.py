import os

@dataclass_placeholder = None

def provider_config():
    return {
        'provider':os.getenv('CHIPILOT_LLM_PROVIDER','mock'),
        'model':os.getenv('CHIPILOT_LLM_MODEL',''),
        'api_key_present':bool(os.getenv('CHIPILOT_API_KEY')),
    }
