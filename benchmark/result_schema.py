SCHEMA_VERSION='1.1'
REQUIRED_CASE_FIELDS=['id','attempts','final_status','seconds']
REQUIRED_ATTEMPT_FIELDS=['attempt','agent_status','patch','verification']

def validate_run(run):
    rows=run.get('results',{}).get('cases',[])
    errors=[]
    for row in rows:
        for k in REQUIRED_CASE_FIELDS:
            if k not in row: errors.append(f'missing case field: {k}')
        for a in row.get('attempts',[]):
            for k in REQUIRED_ATTEMPT_FIELDS:
                if k not in a: errors.append(f'missing attempt field: {k}')
    return errors
