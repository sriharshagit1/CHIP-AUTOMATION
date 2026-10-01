# Controlled EDA Execution

ChipPilot now has an explicit execution boundary. The generic EDA adapter checks
ExecutionPolicy, supports dry-run, enforces timeouts, captures bounded output,
and returns structured evidence.

The verification dispatcher sends bound UVM plans through that boundary. External
execution remains disabled unless explicitly permitted, and dispatcher dry-run
is the default.

Future vendor-specific adapters can replace the generic runner while retaining
the policy and evidence boundary.
