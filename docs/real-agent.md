# Real-model agent

ChipPilot supports an OpenAI-compatible chat-completions provider.

Environment:
- CHIPILOT_API_KEY: provider credential
- CHIPILOT_BASE_URL: optional API base URL
- CHIPILOT_LLM_MODEL: model name
- CHIPILOT_REPO: repository root
- CHIPILOT_MAX_STEPS: bounded action budget

Credentials are read from the environment and are never committed.

Run:

    python -m benchmark.run_real_agent

The model proposes structured actions. The ChipPilot runtime remains authoritative for tool execution, policy, budgets, and evidence-backed completion.

A real-model run must be evaluated separately from deterministic runtime smoke tests.
