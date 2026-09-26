# Memory-aware investigation

Historical matches are injected into the agent context only when their stored verification status is `VERIFIED`.

Each match is labeled as `historical_verified_evidence`, keeping it distinct from observations made during the current investigation.

The current case remains authoritative; historical evidence is a lead, not proof.
