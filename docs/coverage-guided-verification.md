# Coverage-Guided Verification

ChipPilot now has a bounded planning layer for the next verification loop:

```text
coverage report
  -> normalize coverage points
  -> prioritize gaps
  -> inspect available sequences
  -> generate candidate test/sequence artifacts
  -> run simulation
  -> collect coverage
  -> compare before/after
  -> accept only if coverage improves without regression
```

## Implemented

- `coverage_feedback.py` normalizes generic coverage rows and computes deltas.
- `test_generation.py` creates deterministic candidate artifacts without pretending to generate executable UVM code.
- `verification_planner.py` converts gaps into bounded verification steps.
- `test_artifact_store.py` persists candidate/evidence records.
- Tests cover prioritization, regression detection, and planning.

## Boundary

This layer does **not** claim to read commercial coverage databases or execute generated UVM tests automatically. Simulator-specific coverage adapters, executable test synthesis, and post-run coverage collection remain integration work.

A candidate is not evidence of improved verification. ChipPilot should only accept a verification change after simulation and a coverage adapter provide post-run evidence showing improvement without regression.


## Adapter boundary

`coverage_adapter.py` defines the provider-neutral interface. A simulator-specific bridge can implement `CoverageAdapter.collect()` and return normalized `CoverageSnapshot` data. `JsonCoverageAdapter` is a small generic adapter for integration testing; it is not a commercial EDA coverage parser.

`coverage_runner.py` enforces the execution order: simulation must pass first, then coverage is collected, then before/after coverage is compared. A run is accepted only when coverage improves and no coverage point regresses.
