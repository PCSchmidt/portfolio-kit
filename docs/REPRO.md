# Reproducibility

**Contract version:** 0.1.0

Every published run should be replayable from a clean checkout.

## Baseline environment

| Component | Pin |
|-----------|-----|
| Python | 3.11+ |
| Node.js | 20+ (dsh / Cordis) |
| Package managers | pip or uv; pnpm for Node |
| Containers | Docker + Compose when a project has a sandbox |
| OS notes | Windows host is supported via Git Bash / WSL2 for Meridian scripts |

Record exact versions in each project’s `REPRO.md` or CI log.

## What to pin per run

- Model vendor, name, and version or snapshot date
- Decoding: temperature, top_p, max tokens
- Random seeds (Python `PYTHONHASHSEED`, library seeds)
- Dataset / golden-set commit SHA
- `portfolio-kit` commit SHA (this repo)
- Meridian commit SHA if consumed as a dependency
- Prompt / profile file hashes

## This repository

```bash
python eval/validate_schemas.py
```

No network, no API keys, no Docker required for the Phase 0 schema check.

## Later projects

- Prefer a `docker compose` path that does not need host GPU unless the project is meridian-jspace.
- J-space / J-lens work should name the open-weight checkpoint and whether CPU-only is supported.
- CI should run schema validation and unit tests without secrets. Eval jobs that need keys stay manual or use repo secrets never committed to git.
