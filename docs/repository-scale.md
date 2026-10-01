# Repository-scale diagnosis

ChipPilot now has a context layer for whole repositories:
- RTL module/file indexing
- failure-log extraction
- Git change history
- recent changed files
- per-file commit history

The context is evidence passed to the agent; it is not a claim that the agent automatically understands an entire SoC. Production deployments still need richer parsers, elaboration-aware hierarchy, compile databases, UVM topology and EDA metadata.
