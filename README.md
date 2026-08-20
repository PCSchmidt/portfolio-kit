# portfolio-kit

Shared contracts, schemas, eval templates, and starter files for the agent-reliability portfolio built around [Meridian](https://github.com/PCSchmidt/meridian).

**Status:** Contracts 0.1.0 published — family paused 2026-08-19

Meridian is the reliability spine: mechanical gates, an independent Evaluator, and schema-validated memory. This kit versions those contracts so sibling projects can consume them without forking a second gate language.

Handoff: [docs/STATUS.md](docs/STATUS.md). First consumer: [dsh-plugin-honesty-gate](https://github.com/PCSchmidt/dsh-plugin-honesty-gate) Phases 1–4 on `main`.

## Shared contracts

| Document | Role |
|----------|------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Meridian as spine; interchangeable runtimes |
| [docs/GATE_CONTRACT.md](docs/GATE_CONTRACT.md) | What a gate pass means mechanically |
| [docs/MEMORY_SCHEMA.md](docs/MEMORY_SCHEMA.md) | Semantic / episodic / corrections |
| [docs/EVAL_RUBRIC_TEMPLATE.md](docs/EVAL_RUBRIC_TEMPLATE.md) | Shared scoring dimensions |
| [docs/DATA_POLICY.md](docs/DATA_POLICY.md) | Public / unclassified data only |
| [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md) | Lightweight threat-model template |
| [docs/REPRO.md](docs/REPRO.md) | How to reproduce runs |
| [docs/WORKSPACE.md](docs/WORKSPACE.md) | Local path ↔ GitHub map |
| [docs/AGENTS.md](docs/AGENTS.md) | How coding agents should work in this family |

Machine-readable copies live in [schemas/](schemas/). Starter `CONTRACT.md`, `SPEC.md`, and `gates.yaml` live in [templates/](templates/).

## Sibling projects

| Repo | Role |
|------|------|
| [dsh-plugin-honesty-gate](https://github.com/PCSchmidt/dsh-plugin-honesty-gate) | Meridian patterns as a DeepSeek Harness / Cordis plugin |
| [agent-framework-bakeoff](https://github.com/PCSchmidt/agent-framework-bakeoff) | Same public task on LangGraph, CrewAI, AG2/MAF, Meridian |
| [living-docs-architect](https://github.com/PCSchmidt/living-docs-architect) | Architectural-integrity / living-docs agent |
| [meridian-jspace](https://github.com/PCSchmidt/meridian-jspace) | Interpretable memory + Jacobian-lens instrumentation |
| [gate-enforced-rag](https://github.com/PCSchmidt/gate-enforced-rag) | Haystack / LlamaIndex + Evaluator gate |
| [redteam-blue-gate](https://github.com/PCSchmidt/redteam-blue-gate) | Sandboxed red/blue crew behind the same gate |

## Public / unclassified data only

No JPO, F-35, or other non-public program data. Allowed stand-ins are listed in [docs/DATA_POLICY.md](docs/DATA_POLICY.md).

## Validate schemas

```bash
python eval/validate_schemas.py
```

Requires Python 3.11+. No third-party packages.

## Planned phases

0. Shared docs, schemas, templates, CI stub *(done; `0c2d119`)*
1. Golden-set loader + scoring helpers used by the bake-off *(bake-off Phase 1 catalog exists; shared loader still later)*
2. Docker base image + reusable GitHub Actions
3. Versioned schema releases as more siblings consume them

Honesty-gate already copies verdict + memory schemas at 0.1.0. Do not bump fields without a kit version bump.
