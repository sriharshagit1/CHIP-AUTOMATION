def score_candidate(candidate, failure, changed_files=None, dependent_modules=None, historical_matches=None):
    changed_files=set(changed_files or []); dependent_modules=set(dependent_modules or []); historical_matches=historical_matches or []
    evidence=[]; score=0
    file_name=candidate.get('file')
    if file_name and file_name in changed_files: score+=3; evidence.append('affected file overlaps recent change')
    if candidate.get('module') in dependent_modules: score+=2; evidence.append('module is in dependency impact path')
    if candidate.get('category') and any(candidate['category'] in str(x) for x in historical_matches): score+=2; evidence.append('similar verified historical failure')
    if candidate.get('earliest_observed'): score+=1; evidence.append('failure was observed early in timeline')
    return {'heuristic_score':score,'evidence':evidence,'status':'HYPOTHESIS_ONLY','warning':'Heuristic evidence does not establish causality; confirm with targeted execution and regression.'}

def rank_candidates(candidates, **kwargs):
    scored=[]
    for c in candidates:
        scored.append(dict(c, **score_candidate(c, **kwargs)))
    return sorted(scored,key=lambda x:x['heuristic_score'],reverse=True)
