def summarize(rows):
    n=len(rows)
    return {
        'cases':n,
        'completion_rate':sum(r.get('status')=='VERIFIED' for r in rows)/n if n else 0.0,
        'error_rate':sum(r.get('status')=='ERROR' for r in rows)/n if n else 0.0,
        'mean_steps':sum(r.get('steps',0) for r in rows)/n if n else 0.0,
        'mean_seconds':sum(r.get('seconds',0.0) for r in rows)/n if n else 0.0,
    }
