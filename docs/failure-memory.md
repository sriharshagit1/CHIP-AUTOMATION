# Failure memory

ChipPilot can store structured, verified failure records for future retrieval.

A record contains:
- failure category
- affected module
- failure signature
- root-cause summary
- patch summary
- verification result
- commit reference

Only verified outcomes should be promoted as reusable engineering evidence. Similarity is a retrieval aid, not proof that an old fix applies to a new failure.
