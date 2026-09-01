# Family status — gate-enforced-rag Phase 2 2026-09-01

**Contract version:** 0.1.0  
**Capacity:** 8–12 hours/week  
**This session:** gate-enforced-rag Phase 2 (CI-safe Haystack / LlamaIndex adapters)  
**Previous:** honesty-gate Phases 1–4; bake-off Phases 1–4; living-docs Phases 1–5; meridian-jspace Phase 1; gate-enforced-rag Phase 1

This is the handoff for the next working session. Sibling `STATUS.md` files should match this table.

## What shipped

### portfolio-kit (`ed7e29d`)

Shared contracts, JSON schemas, templates, schema validator, CI, workspace map.

- Docs: ARCHITECTURE, GATE_CONTRACT, MEMORY_SCHEMA, EVAL_RUBRIC_TEMPLATE, DATA_POLICY, THREAT_MODEL, REPRO, WORKSPACE, AGENTS
- `python eval/validate_schemas.py` (stdlib, Python 3.11+)
- GitHub: [PCSchmidt/portfolio-kit](https://github.com/PCSchmidt/portfolio-kit)

### dsh-plugin-honesty-gate (`c5869cf`)

Phases 1–4 implemented. Not a live dsh install.

| Phase | Content | Evidence |
|-------|---------|----------|
| 1 | Cordis `name` + `apply(ctx)`, GateRegistry, `tools/pre-execute` veto | `src/plugin.js`, `src/gate-registry.js` |
| 2 | Independent Evaluator, portfolio-kit verdict JSON | `src/evaluator.js`, `src/verdict.js` |
| 3 | Schema-validated MemoryStore + `revertLast()` | `src/memory-store.js` |
| 4 | Example profile, CI, held-out eval | `examples/profile/`, `eval/`, `.github/workflows/test.yml` |

Last local run (2026-08-19): **32/32** `npm test`; `npm run eval` **ok: true** — D3 catch 1.0 (6 known-bad), verdict agreement 1.0, schema/isolation 1.0.

Reference checkout: `../deepseek-harness` @ `dsh-v0.1.0-rc.8` (`141eb6f`). Upstream only; not a portfolio repo.

### agent-framework-bakeoff (Phase 4)

Four runtimes on `src/tools.js`. Published [eval/SCORE_TABLE.md](https://github.com/PCSchmidt/agent-framework-bakeoff/blob/main/eval/SCORE_TABLE.md). D3 catch 1.0 (n=24); D5 3/3 × 4; Meridian-only fail-closed query gate (D6). No LLM.

### living-docs-architect (Phase 5)

Three mechanical rules, gated `act` flag, 39-case eval, synthetic `fixtures/sample-app`, local git observer, mechanical architect, gated local remediation, dogfood allowlist (`src/dogfood.js`). Dry-run on own public family remotes. HardPowerIntelligence, Meridian, and GitHub comments/issues/webhooks refused.

### meridian-jspace (Phase 1)

Mechanical J-space readout of Evaluator rejects (`src/project.js`). Concept catalog, 12-case eval, GitHub writes and live Qwen / jacobian-lens refused. No GPU, no HuggingFace in CI.

### gate-enforced-rag (Phase 1)

Mechanical single-source RAG (`src/answer.js`). Keyword retrieve + extractive citations, Evaluator gate before delivery. Phase 2 adds CI-safe Haystack / LlamaIndex adapters (`src/adapters.js`). GitHub writes, live LLM, live Haystack / LlamaIndex packages, and federated multi-source refused. No GPU, no embeddings API in CI. Eval GER-001–020.

### Remaining Phase 0 siblings (docs only)

| Repo | Implementation |
|------|----------------|
| [redteam-blue-gate](https://github.com/PCSchmidt/redteam-blue-gate) | not started; **last in sequence** |

### Meridian

Existing spine ([PCSchmidt/meridian](https://github.com/PCSchmidt/meridian) `0e75c75`). Local nest: `Meridian/Meridian/`. Only dirty file is `.meridian/session.json` (runtime; do not commit). Phase 9 items (routing, MCP, delegate-then-evaluate) remain later.

## Remaining work (priority)

Do **not** start red/blue or a from-scratch coding harness.
gate-enforced-rag Phase 2 shipped. Next: gate-enforced-rag Phase 3 (multi-source router) or meridian-jspace Phase 2 unless redirected.
1. **Manual, no code:** GitHub topic `dsh-plugin` on honesty-gate.
2. **Optional live check:** install `dsh` CLI and run `dsh plugin --profile honesty-gate-demo add .` then `--dump-config`. Unit tests do not require this.
3. **Bake-off Phase 4 shipped.** Next implementation in this family is gate-enforced-rag Phase 3 or meridian-jspace Phase 2 — not red/blue.
4. **Optional honesty-gate increment:** LLM judge vs mechanical judge on the same HG-001–008 fixtures (needs API keys; not required to resume).
5. **Later family:** gate-enforced-rag Phase 3+ → meridian-jspace Phase 2+ → redteam-blue-gate.
6. **Meridian Phase 9** after the kit has a second consumer (bake-off), not before.
7. **portfolio-kit Phase 1:** golden-set loader + scoring helpers once bake-off has cases.
8. **Portfolio site** ([PCSchmidt.github.io](https://github.com/PCSchmidt/PCSchmidt.github.io)): update after bake-off has numbers, not now.

## Explicit non-goals (still)

- No JPO / F-35 / employer data in any public repo.
- Do not flatten older `repo/repo` nests this sprint.
- Do not delete workspace-root `node_modules/` unless you intend a cleanup PR outside this family.
- Do not commit recovery codes, identity images, or `.env`.
- Do not treat generator self-score as a gate pass.

## Hygiene left alone

- `Automated global inventory collection architecture for F35 program - Claude/`
- `IdeasFolder/ariadne.zip`
- `ghost-researcher/ghost-researcher/files.zip`
- Workspace-root `node_modules/` (no root `package.json`)

## Resume checklist

1. Read this file and the target repo `STATUS.md`.
2. Confirm `git status` is clean on family remotes (except Meridian session).
3. Do not start red/blue. Next: gate-enforced-rag Phase 3 (multi-source router) unless the user redirects. Do not download Qwen unless asked for meridian-jspace Phase 2.
