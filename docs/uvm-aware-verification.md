# UVM-Aware Verification

ChipPilot now has a conservative UVM context boundary.

The context extractor identifies UVM tests, sequences, common UVM components,
assertions, source provenance, and a coarse confidence level. It is not a full
SystemVerilog parser.

The execution planner turns a discovered test into a simulator command plan,
including UVM_TESTNAME. It does not execute the command. Actual execution stays
behind ChipPilot's existing tool and execution-policy boundary and requires an
explicitly configured EDA adapter.
