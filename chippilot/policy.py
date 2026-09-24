from dataclasses import dataclass

@dataclass
class SafetyPolicy:
    max_attempts: int = 2
    allow_original_write: bool = False
    require_simulation_for_verified: bool = True

def can_claim_verified(verification: dict, policy: SafetyPolicy):
    return verification.get("status")=="VERIFIED" and policy.require_simulation_for_verified
