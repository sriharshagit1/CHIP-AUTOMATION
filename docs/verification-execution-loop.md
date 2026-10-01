# Verification Execution Loop

ChipPilot now composes the coverage planner and UVM execution planner.

The flow is:

```text
coverage gap
  -> verification candidate
  -> discovered UVM test
  -> simulator command plan
  -> policy-controlled execution
  -> coverage collection
  -> evidence
  -> bounded re-plan
```

The binding layer refuses to create an execution plan when UVM context confidence
is low or no UVM tests are discovered. It does not execute commands itself.

This keeps repository understanding, planning, execution authority, and evidence
collection separate.
