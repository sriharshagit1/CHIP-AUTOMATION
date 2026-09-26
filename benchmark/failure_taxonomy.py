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
 status=result.get('agent_status')
 if status=='PROTOCOL_ERROR': return 'PROTOCOL_ERROR'
 if status in ('MAX_TURNS','ERROR'): return 'TIMEOUT' if status=='MAX_TURNS' else 'TOOL_ERROR'
 v=result.get('verification',{}).get('status')
 if not result.get('patch'): return 'NO_PATCH'
 return {'INVALID_PATCH':'INVALID_PATCH','FAIL':'TARGET_FAIL','VERIFIED':'VERIFIED'}.get(v,'TOOL_ERROR')
