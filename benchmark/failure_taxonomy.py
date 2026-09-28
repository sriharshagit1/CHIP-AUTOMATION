CATEGORIES={
 'PROTOCOL_ERROR':'Model returned invalid structured output',
 'NO_PATCH':'Model stopped without a patch',
 'INVALID_PATCH':'Patch could not be applied safely',
 'COMPILE_FAIL':'Candidate patch failed compilation',
 'TARGET_FAIL':'Candidate failed the targeted behavioral test',
 'REGRESSION_FAIL':'Candidate passed target but failed regression',
 'VERIFIED':'Candidate passed all required verification stages',
 'TOOL_ERROR':'A registered investigation tool failed',
 'TIMEOUT':'Agent exceeded configured execution budget',
}

def classify(result):
    verification=result.get('verification') or {}
    status=result.get('agent_status','')
    if verification.get('status')=='VERIFIED':
        return 'VERIFIED'
    if status=='PROTOCOL_ERROR':
        return 'PROTOCOL_ERROR'
    if not result.get('patch'):
        return 'NO_PATCH'
    if verification.get('status')=='FAIL':
        return 'TARGET_FAIL'
    return 'TOOL_ERROR'
