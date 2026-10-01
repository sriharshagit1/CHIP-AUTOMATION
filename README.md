# CHIPILOT

**AI Engineering Agent for Semiconductor Teams**

> Turn regression failures into verified fixes.

ChipPilot is being built as an AI Engineering OS for Silicon. The first wedge is simulator-backed RTL regression investigation; the platform architecture expands across verification, synthesis, STA, DFT and post-silicon workflows.

## Current platform
- bounded agent runtime
- provider-independent model interface
- repository/Git tools
- planning and objective contracts
- evidence and run records
- failure memory/retrieval
- simulator-backed benchmark foundation
- CI and public product demo
- cross-stage EDA tool abstraction

## Run local tests

```bash
python -m unittest discover -s tests -v
```

## Run the real-model benchmark

Set `CHIPILOT_API_KEY` and optionally `CHIPILOT_BASE_URL`, `CHIPILOT_LLM_MODEL`, `CHIPILOT_REPO`, and `CHIPILOT_MAX_STEPS`.

```bash
python -m benchmark.run_real_agent
```

The real-model benchmark is an experimental evaluation, not a product accuracy claim.

## Vision

Build an AI Engineering OS for Silicon that can accept an engineering objective, plan bounded work, operate approved engineering tools, learn from verified history, produce auditable evidence, and stop at human approval boundaries.

See `docs/complete-vision.md` and `docs/vision-implementation-map.md`.
