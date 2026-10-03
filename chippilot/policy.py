class AgentPolicy:
    def __init__(self,max_patch_attempts=3,max_runtime_seconds=900):
        self.max_patch_attempts=max_patch_attempts; self.max_runtime_seconds=max_runtime_seconds
    def can_attempt_patch(self,attempt): return attempt < self.max_patch_attempts
    def requires_human_merge(self): return True
    def verification_required(self): return True

class SafetyPolicy:
    def __init__(self,require_verification=True): self.require_verification=require_verification

def can_claim_verified(result,policy):
    return (not policy.require_verification) or result.get("status")=="VERIFIED"
