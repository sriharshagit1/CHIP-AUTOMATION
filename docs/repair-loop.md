# Bounded repair loop

ChipPilot can optionally retry a failed patch using verifier feedback.

Rules:

- Maximum attempts are bounded.
- The verifier remains authoritative.
- Feedback contains observed execution results, not hidden ground truth.
- A retry cannot directly mark a case verified.
- Exhausted retries are recorded as a failure mode.
