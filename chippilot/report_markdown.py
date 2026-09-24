from html import escape

def markdown_report(report):
    fp=report.get('failure_fingerprint') or {}
    diag=report.get('diagnosis') or {}
    patch=report.get('patch') or {}
    ver=report.get('verification') or {}
    ev=report.get('evidence') or {}
    lines=['# ChipPilot Investigation Report','',f"**Verdict:** `{ev.get('verdict',ver.get('status','UNKNOWN'))}`",'', '## Failure', f"- Category: `{fp.get('category','unknown')}`", f"- Module: `{fp.get('module','unknown')}`", f"- File: `{fp.get('file','unknown')}`", f"- Line: `{fp.get('line','unknown')}`", f"- Expected: `{fp.get('expected','')}`", f"- Observed: `{fp.get('observed','')}`",'', '## Diagnosis', f"{diag.get('root_cause',diag.get('root_cause_summary','No diagnosis recorded.'))}",'', '## Patch', f"Status: `{patch.get('status','UNKNOWN')}`",'', '## Verification', f"Status: `{ver.get('status','NOT_RUN')}`", f"Stage: `{ver.get('stage','')}`",'', '## Evidence', f"Score: `{ev.get('evidence_score','not calculated')}`",'', '## Tool Trace']
    for item in report.get('tool_trace',[]): lines.append(f"- `{item.get('tool','unknown')}`")
    return '\n'.join(lines)+'\n'

def html_report(report):
    md=markdown_report(report)
    return '<html><body><pre>'+escape(md)+'</pre></body></html>'
