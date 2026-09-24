from dataclasses import dataclass, asdict

@dataclass
class EvidenceScore:
    historical_match: float = 0.0
    module_match: float = 0.0
    git_relevance: float = 0.0
    root_cause_evidence: float = 0.0
    patch_minimality: float = 0.0
    compile_pass: float = 0.0
    targeted_test_pass: float = 0.0
    regression_pass: float = 0.0

    def total(self):
        # Weighted evidence, not model confidence.
        weights={'historical_match':.08,'module_match':.08,'git_relevance':.10,'root_cause_evidence':.14,'patch_minimality':.10,'compile_pass':.12,'targeted_test_pass':.16,'regression_pass':.22}
        return round(sum(getattr(self,k)*w for k,w in weights.items()),3)

    def verdict(self):
        if self.compile_pass>=1 and self.targeted_test_pass>=1 and self.regression_pass>=1: return 'VERIFIED'
        if self.root_cause_evidence>=.6: return 'SUPPORTED_HYPOTHESIS'
        return 'INVESTIGATE'

    def to_dict(self):
        d=asdict(self); d['evidence_score']=self.total(); d['verdict']=self.verdict(); return d
