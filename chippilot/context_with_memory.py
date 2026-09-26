from .context_builder import build_context
from .failure_memory_v2 import FailureMemoryV2

def build_context_with_memory(case_id,log,memory=None):
    memory=memory or FailureMemoryV2()
    matches=memory.search(log)
    return build_context(case_id,log,[{'source':'historical_verified_evidence','record':m} for m in matches if m.get('verification',{}).get('status')=='VERIFIED'])
