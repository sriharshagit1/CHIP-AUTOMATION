def summarize(rows):
    n=len(rows)
    if not n: return {'cases':0}
    first_pass=sum(1 for r in rows if r.get('attempts') and r['attempts'][0].get('verification',{}).get('status')=='VERIFIED')
    verified=sum(r.get('status')=='VERIFIED' for r in rows)
    attempts=sum(len(r.get('attempts',[])) for r in rows)
    return {'cases':n,'first_pass_verified_rate':first_pass/n,'verified_after_repair_rate':verified/n,'mean_attempts':attempts/n}
