# ChipPilot public demo

## The 60-second story

**Input:** a failing semiconductor regression.

**ChipPilot:** clusters failures, inspects RTL and recent Git changes, retrieves verified historical evidence, proposes a minimal patch, runs targeted verification, checks regression impact, and produces an auditable report.

**Output:** a verified result when execution evidence supports it—or an explicit failure when it does not.

## Example

```text
REGRESSION: FSM-014

Failure: expected DONE, observed IDLE
Affected module: packet_controller.sv

Recent change:
  completion handling modified in PROCESS state

Historical evidence:
  2 verified FSM transition failures with similar signature

Hypothesis:
  PROCESS transitions to IDLE before completion is asserted

Proposed patch:
  PROCESS -> DONE on completion condition

Verification:
  targeted test: PASS
  regression: PASS

STATUS: VERIFIED
Evidence: diff + logs + test results + investigation report
```

The example is illustrative; benchmark claims must come from recorded experiments.

## Safety boundaries

- The model cannot mark a patch verified.
- Retry attempts are bounded.
- Historical memory is separated from current evidence.
- Git changes are hypotheses, not proof of causality.
- PR merge remains human-controlled.
