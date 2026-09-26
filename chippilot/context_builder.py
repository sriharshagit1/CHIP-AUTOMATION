from .failure_context import normalize_log

def build_context(case_id,log,history=None):
    f=normalize_log(log)
    return {'case_id':case_id,'failure':f,'historical_matches':history or [],'constraints':['smallest safe patch','verification required','no unsupported claims']}
