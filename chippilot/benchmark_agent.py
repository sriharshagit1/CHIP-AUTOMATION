from .heuristic_diagnoser import classify
from .fixture_patcher import propose
from .fixture_verify import verify
from .evidence_score import EvidenceScore

CASE_RTL={'WIDTH-001':'benchmark/cases/width_mismatch.sv','RESET-001':'benchmark/cases/reset_bug.sv','COUNTER-001':'benchmark/cases/counter_bug.sv','HANDSHAKE-001':'benchmark/cases/handshake_bug.sv'}

def run_case(case_id,log):
    diagnosis=classify(log)
    score=EvidenceScore()
    score.classification=float(diagnosis['case_id']==case_id)
    if diagnosis['case_id']!=case_id: return {'case_id':case_id,'diagnosis':diagnosis,'evidence':score.to_dict()}
    patch=propose(case_id,CASE_RTL[case_id])
    score.patch_minimality=float(patch.get('status')=='PROPOSED')
    verification=verify(case_id,patch['content']) if patch.get('status')=='PROPOSED' else {'status':'NOT_RUN'}
    score.compile_pass=float(verification.get('status')=='VERIFIED')
    score.targeted_test_pass=float(verification.get('status')=='VERIFIED')
    score.regression_pass=float(verification.get('status')=='VERIFIED')
    return {'case_id':case_id,'diagnosis':diagnosis,'patch':patch,'verification':verification,'evidence':score.to_dict()}
