# Failure fingerprints

ChipPilot normalizes regression failures into structured fingerprints so similar failures can be retrieved even when log wording differs.

Fields include category, module, signal, expected value, observed value, assertion text, source file and line.

The fingerprint is a retrieval key, not a proof of causality. Current RTL and executable verification remain authoritative.
