# PR integration

ChipPilot's intended pull-request workflow is report-first.

1. A PR triggers deterministic validation.
2. Regression failures are collected.
3. ChipPilot clusters and triages failures.
4. An investigation report is generated.
5. A proposed patch and evidence are presented for human review.
6. Merge remains a human-controlled action.

Live-model analysis is opt-in and requires deployment credentials. The default workflow never stores or requests model secrets.
