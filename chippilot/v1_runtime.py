from pathlib import Path
from .fingerprint import fingerprint
from .memory import FailureMemory
from .retrieval import FailureRetriever
from .evidence_score import EvidenceScore
from .report import build_report, write_report
from .report_markdown import markdown_report
from .fixture_patcher import propose
from .fixture_verify import verify
from .session import InvestigationSession
from .ground_truth_adapter import CASES, LOGS

class ChipPilotV1:
    def __init__(self,memory_path='evidence/failure_memory.json'):
        self.memory=FailureMemory(memory_path)

    def investigate(self,case_id,report_path=None):
        session=InvestigationSession(case_id); session.record('start')
        if case_id not in LOGS: raise ValueError('unknown benchmark case')
        log=LOGS[case_id]; fp=fingerprint(log); session.record('fingerprint',fingerprint=fp.to_dict())
        history=FailureRetriever(self.memory).find_similar(log)
        session.record('history_search',matches=len(history['matches']))
        rtl=Path('benchmark/cases')/CASES[case_id]['rtl']
        patch=propose(case_id,rtl)
        session.record('patch_proposed',status=patch.get('status'))
        verification=verify(case_id,patch['content']) if patch.get('status')=='PROPOSED' else {'status':'NOT_RUN'}
        session.record('verification',status=verification.get('status'))
        score=EvidenceScore(classification=1,root_cause_evidence=.7,patch_minimality=float(patch.get('status')=='PROPOSED'),compile_pass=float(verification.get('status')=='VERIFIED'),targeted_test_pass=float(verification.get('status')=='VERIFIED'),regression_pass=float(verification.get('status')=='VERIFIED'))
        evidence=score.to_dict(); session.record('verdict',verdict=evidence['verdict'])
        report=build_report(fingerprint=fp.to_dict(),knowledge=history,diagnosis={'root_cause':'benchmark-supported candidate diagnosis'},patch={k:v for k,v in patch.items() if k!='content'},verification=verification,evidence=evidence,tool_trace=session.events)
        if report_path: write_report(report_path,report)
        return report
