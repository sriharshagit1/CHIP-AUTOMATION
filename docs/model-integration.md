# Model integration

ChipPilot keeps the foundation model behind a provider boundary.

Required deployment configuration:

- `CHIPILOT_LLM_ENDPOINT`
- `CHIPILOT_API_KEY`
- `CHIPILOT_LLM_MODEL` (optional provider-specific selector)

No credentials belong in source control.

The benchmark harness remains provider-neutral so the same cases and verification rules can be used across models.
