from .evidence import VerificationEvidence
from .verification_execution import VerificationExecutionStep

def record_attempt(*, run_id, objective, candidate_id, step: VerificationExecutionStep,
                   result, coverage_before=None, coverage_after=None,
                   improved=(), regressed=()):
    status=getattr(result,"status","UNKNOWN")
    accepted=(status=="PASS" and coverage_before is not None and coverage_after is not None
              and coverage_after>coverage_before and not regressed)
    return VerificationEvidence(
        run_id,objective,candidate_id,step.test_name,step.command.executable,
        step.command.arguments,status,getattr(result,"returncode",None),
        coverage_before,coverage_after,tuple(improved),tuple(regressed),accepted,
        stdout=getattr(result,"stdout",""),stderr=getattr(result,"stderr",""))
