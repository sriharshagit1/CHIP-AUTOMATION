def build_pr_summary(report):
    status=report.get('executive_summary',{}).get('final_status','UNKNOWN')
    verification=report.get('verification',{})
    return {'status':status,'verification_status':verification.get('status','NOT_RUN'),'human_review_required':True,'merge_allowed_by_agent':False}
