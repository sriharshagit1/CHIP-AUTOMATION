# ChipPilot Agent Architecture

The AI layer is deliberately separated from execution.

1. **Observe** — collect regression logs, RTL context and repository metadata.
2. **Reason** — classify the failure and form a root-cause hypothesis.
3. **Propose** — generate a minimal patch.
4. **Execute** — apply the patch only inside an isolated workspace.
5. **Verify** — compile, simulate and run regression.
6. **Report** — emit evidence and a machine-readable verdict.

The model never gets to declare a fix successful by itself. Execution evidence controls the VERIFIED state.
