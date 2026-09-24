# Git-aware debugging

ChipPilot can inspect repository history without allowing the model unrestricted shell access.

Available context:
- recent commits
- files changed by a commit
- full commit diff
- line-level blame

The intended diagnosis flow is:

failure -> affected RTL -> recent changes -> causal hypothesis -> candidate patch -> verification.

Git history is evidence, not proof. A proposed fix still requires executable verification.
