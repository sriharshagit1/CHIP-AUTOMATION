# Verification Evidence and Provenance

ChipPilot now persists auditable verification-attempt records containing the
objective, run ID, candidate/test identity, exact command, execution result,
coverage before/after, changed coverage points, acceptance, timestamp, and
bounded output.

EvidenceStore writes records under evidence/verification. Acceptance is
conservative: passing execution plus coverage improvement without regression is
required when coverage evidence is supplied.

This is a provenance foundation, not a claim of cryptographic attestation,
tamper-proof storage, or enterprise retention.
