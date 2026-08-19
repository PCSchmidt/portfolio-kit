# Workspace map

Local clones live as **siblings of Meridian** under `c:\Dev\AIEngineeringProjects` (single-level, not `repo/repo`).

Family pause snapshot: [STATUS.md](STATUS.md) (2026-08-19). Honesty-gate is implemented through Phase 4; other siblings remain Phase 0 docs.

| Local path | GitHub | Role |
|------------|--------|------|
| `Meridian/Meridian/` | [PCSchmidt/meridian](https://github.com/PCSchmidt/meridian) | Reliability spine (existing; zip-migrated nest) |
| `portfolio-kit/` | [PCSchmidt/portfolio-kit](https://github.com/PCSchmidt/portfolio-kit) | Shared contracts (this repo) |
| `dsh-plugin-honesty-gate/` | [PCSchmidt/dsh-plugin-honesty-gate](https://github.com/PCSchmidt/dsh-plugin-honesty-gate) | dsh / Cordis honesty gate |
| `agent-framework-bakeoff/` | [PCSchmidt/agent-framework-bakeoff](https://github.com/PCSchmidt/agent-framework-bakeoff) | Multi-framework bake-off |
| `living-docs-architect/` | [PCSchmidt/living-docs-architect](https://github.com/PCSchmidt/living-docs-architect) | Living documentation agent |
| `meridian-jspace/` | [PCSchmidt/meridian-jspace](https://github.com/PCSchmidt/meridian-jspace) | J-space / J-lens |
| `gate-enforced-rag/` | [PCSchmidt/gate-enforced-rag](https://github.com/PCSchmidt/gate-enforced-rag) | Gate-enforced RAG |
| `redteam-blue-gate/` | [PCSchmidt/redteam-blue-gate](https://github.com/PCSchmidt/redteam-blue-gate) | Sandboxed red/blue |
| `deepseek-harness/` | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | Upstream reference checkout (`dsh-v0.1.0-rc.8`). Not a portfolio repo. |

## Nearby but not in this family

| Path | Note |
|------|------|
| `information_docs/` | Archive of Grok PDF exports. Not the contract source of truth. |
| `PCSchmidt.github.io/` | Portfolio site. Update after first real artifact. |
| `Automated global inventory collection architecture for F35 program - Claude/` | Local dump. **Do not** commit or copy into these repos. |
| `IdeasFolder/ariadne.zip` | Unextracted migration leftover. |
| `ghost-researcher/ghost-researcher/files.zip` | Migration leftover; `files/` already extracted beside it. |
| workspace-root `node_modules/` | No root `package.json`. Safe to delete later; not touched this sprint. |

## Hygiene rules

- Do not nest new clones (`portfolio-kit/portfolio-kit`).
- Do not add recovery codes, identity images, or `.env` files.
- Do not flatten older double-nested projects in this sprint.
