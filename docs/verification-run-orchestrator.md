# Verification Run Orchestrator

`chippilot/verification_run.py` provides a run-level composition boundary.

A single RunRecord run_id is carried through planning, UVM binding, controlled dispatch, and evidence persistence. The orchestrator records plan and execution events and terminates with BLOCKED, DRY_RUN, EXECUTED, or FAILED.

The current implementation stores the pre-run coverage baseline with each evidence record. Post-run coverage collection and bounded re-planning remain the next integration step. DRY_RUN remains the default.
