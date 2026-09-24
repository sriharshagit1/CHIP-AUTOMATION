from dataclasses import dataclass, asdict

@dataclass
class CaseScore:
    case_id: str
    classification: float = 0.0
    root_cause: float = 0.0
    patch: float = 0.0
    compile: float = 0.0
    targeted_test: float = 0.0
    regression: float = 0.0
    seconds: float = 0.0

    @property
    def verified_fix(self): return int(self.compile==1 and self.targeted_test==1 and self.regression==1)

    def to_dict(self): return asdict(self) | {'verified_fix':self.verified_fix}

def aggregate(cases):
    if not cases: return {'cases':0}
    n=len(cases)
    return {
        'cases':n,
        'classification_accuracy':round(sum(x.classification for x in cases)/n,3),
        'root_cause_accuracy':round(sum(x.root_cause for x in cases)/n,3),
        'patch_success_rate':round(sum(x.patch for x in cases)/n,3),
        'verified_fix_rate':round(sum(x.verified_fix for x in cases)/n,3),
        'mean_time_seconds':round(sum(x.seconds for x in cases)/n,3)
    }
