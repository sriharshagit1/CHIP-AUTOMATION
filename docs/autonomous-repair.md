# Autonomous repair

ChipPilot treats a patch as a candidate until independent verification succeeds.

Repair loop:
1. Produce a patch artifact.
2. Apply it in an isolated workspace.
3. Compile.
4. Run targeted verification.
5. Run regression.
6. Reject on any failed gate.
7. Allow bounded re-attempts.
8. Accept only a VERIFIED patch.
9. Persist patch + evidence + execution trace.

The model never has authority to mark a patch verified.
