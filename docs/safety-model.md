# ChipPilot safety model

- The original RTL workspace is never modified by the V1 verification path.
- Candidate changes are executed in a temporary isolated workspace.
- The retry budget is bounded.
- A model response alone cannot produce a VERIFIED verdict.
- VERIFIED requires successful executable verification.
- Every attempt can be represented as evidence for audit and debugging.
