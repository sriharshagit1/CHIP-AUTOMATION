def to_markdown(report):
    s=report['executive_summary']; lines=[f"# ChipPilot Investigation — {report['case_id']}",f"**Status:** {s['final_status']}","","## Root-cause candidates"]
    for c in s['primary_candidates']: lines.append(f"- {c}")
    lines += ["","## Proposed patch",'```text',str(report.get('proposed_patch') or 'No patch proposed'),'```',"","## Verification",str(report.get('verification',{})),"","## Audit note",report['audit_note']]
    return '\n'.join(lines)
