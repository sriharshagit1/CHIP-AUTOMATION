from .context_with_memory import build_context_with_memory
from .change_context import build_change_context

def build_investigation_context(case_id,log,memory,history,diff):
    base=build_context_with_memory(case_id,log,memory)
    base['changes']=build_change_context(history,diff)
    return base
