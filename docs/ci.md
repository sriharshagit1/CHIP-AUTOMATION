# CI strategy

The repository should run deterministic unit and benchmark-contract tests on every change.

Real-model evaluations remain opt-in because they require external credentials and should be recorded as explicit experiment runs.

Recommended CI stages:

1. Python unit tests
2. Benchmark contract tests
3. RTL fixture compilation/simulation where the simulator is available
4. Static checks
5. Optional live-model experiment, never as an implicit credentialed CI step
