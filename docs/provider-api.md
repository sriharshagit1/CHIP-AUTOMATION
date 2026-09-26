# Provider API contract

ChipPilot's deployment-specific model endpoint receives JSON:

```json
{"messages":[...],"tools":[...]}
```

and returns:

```json
{"output":"<strict ChipPilot JSON response>"}
```

The adapter sends an optional Bearer token from `CHIPILOT_API_KEY`. No provider credentials are stored in Git.
