# Repository-aware agent loop

ChipPilot treats debugging as a tool-use problem:

1. Read the regression log.
2. Read the affected RTL.
3. Form a diagnosis.
4. Generate the smallest candidate patch.
5. Execute it in an isolated workspace.
6. Inspect simulator output.
7. Emit VERIFIED only when execution succeeds.

The current FSM path is deterministic. The provider interface in llm_agent.py can later replace or augment diagnosis and patch planning for unseen failures.
