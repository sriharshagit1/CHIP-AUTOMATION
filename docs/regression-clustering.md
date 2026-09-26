# Regression failure clustering

Large regressions can produce many secondary failures from one underlying defect. ChipPilot groups failures using normalized categories and affected files.

A cluster is a hypothesis, not proof of a shared root cause. The agent must inspect representative evidence and verify the proposed fix before treating a cluster as resolved.

Future signals can include stack traces, simulator signatures, dependency paths, temporal ordering, and Git-change overlap.
