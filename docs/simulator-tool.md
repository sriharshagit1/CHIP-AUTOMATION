# Simulator tool

ChipPilot exposes Verilator as a bounded engineering tool when it is installed.

The simulator is intentionally outside model authority:
- the model may request a simulation;
- the runtime executes it;
- the result becomes evidence;
- completion still requires the verification gate.

A production deployment can register other simulators through the same tool interface.
