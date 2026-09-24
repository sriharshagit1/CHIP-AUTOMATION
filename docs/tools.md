# ChipPilot tool layer

The agent uses controlled repository tools rather than unrestricted shell execution.

Current tools:
- read_log
- read_rtl
- search_repository
- git_diff
- inspect_testbench

Every tool call is recorded and the controller has a hard call budget. Simulation remains separate so the verification policy controls VERIFIED.
