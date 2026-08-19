# Memory Schema

**Contract version:** 0.1.0  
**Machine schema:** [schemas/memory-schema.json](../schemas/memory-schema.json)  
**Adapted from:** Meridian `.meridian/memory-schema.json` and [docs/memory.md](https://github.com/PCSchmidt/meridian/blob/main/docs/memory.md)

Memory is **schema-validated JSON / JSONL**, not markdown the model can silently corrupt. Invalid writes fail closed.

## Three types

| Type | File (Meridian) | Shape | Purpose |
|------|-----------------|-------|---------|
| Semantic | `semantic.json` | `{ schema_version, memory_type: "semantic", patterns[] }` | Validated cross-project patterns, deduped by SHA-256 |
| Episodic | `episodic.jsonl` | one `episodic_event` per line | Append-only session / gate log |
| Corrections | `corrections.jsonl` | one `correction` per line | Predicted vs actual (calibration / reflexion) |

Runtime memory is **per-developer** and should be gitignored. Schemas and examples are versioned here.

## Required fields

### Semantic pattern

`pattern_id`, `description`, `context`, `confidence` (`LOW`\|`MEDIUM`\|`HIGH`), `validated_count`, `hash` (64 hex), `created`, `last_validated`.  
`pattern_id` matches `^PAT-[A-Z0-9]+-[0-9]{3}$`.

### Episodic event

`timestamp`, `event_type`, `session_id` (8 hex).  
`event_type` ∈ `session_start`, `session_end`, `gate_passed`, `gate_blocked`, `stop_event`, `feature_complete`, `error_logged`.

### Correction

`session_id`, `gate`, `date`, `project`, `root_cause`, `action_next`.  
Hours fields are optional when time was not tracked.

## Write rules

1. Validate against `schemas/memory-schema.json` before append.
2. Semantic writes dedupe on `hash`.
3. Episodic and corrections are append-only.
4. A validation failure is **CRITICAL** — do not proceed with a corrupt store.
5. Cross-project semantic sync is allowed; episodic and corrections stay project-isolated unless a later Meridian Phase 9 design says otherwise.

## Examples

See [schemas/examples/](../schemas/examples/). Validate with:

```bash
python eval/validate_schemas.py
```
