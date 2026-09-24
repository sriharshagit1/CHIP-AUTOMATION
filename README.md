# ChipPilot — Autonomous Semiconductor Debugging Agent

ChipPilot is an engineering-first prototype for AI-assisted semiconductor regression debugging.

> **Turn regression failures into verified fixes.**

## What it is

The prototype is designed around a verification-first agent loop:

```
Failure
  ↓
Diagnosis
  ↓
Repository context
  ↓
Patch proposal
  ↓
Simulation
  ↓
Verification
  ↓
Evidence
```

The core product idea is deliberately narrower than "AI that designs chips": start with a painful workflow — regression failure investigation — and automate the repeated engineering work around it.

## Product thesis

A useful engineering agent should not stop at generating an explanation. It should:

1. inspect the real repository and failure artifacts,
2. use deterministic tools,
3. make a bounded change,
4. execute the relevant test/regression,
5. and report the evidence behind the result.

## V1 scope

- SystemVerilog / Verilator benchmark
- Regression-log analysis
- RTL search and context gathering
- Git-change inspection
- Root-cause hypothesis generation
- Minimal patch proposal
- Targeted simulation
- Regression verification
- Evidence bundle

## Planned architecture

```
                    Agent Controller
                           |
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
      Log Tool          RTL Tool         Git Tool
          |                |                |
          └────────────────┼────────────────┘
                           ↓
                    Root-Cause Engine
                           ↓
                      Patch Engine
                           ↓
                    Verification Runner
                           ↓
                      Evidence Store
```

## Roadmap

**V1 — Regression Failure Investigator**  
Controlled benchmark, diagnosis, patch proposals, and verified evidence.

**V2 — Repository & CI Agent**  
GitHub/GitLab integration, pull-request analysis, regression orchestration, and historical failure search.

**V3 — Verification Engineering Platform**  
UVM/debug workflows, reusable evaluation suites, enterprise controls, and EDA integrations.

**Long-term vision — AI Engineering OS for Silicon**  
Verification → RTL debugging → synthesis → STA → DFT → post-silicon validation.

## Important note

The current public page is a product/architecture demo. The benchmark and agent implementation are being expanded iteratively; claims about accuracy or time savings should be added only after reproducible evaluation.

## Demo

The GitHub Pages site is the recruiter/founder-facing overview. The repository is the technical source of truth.

