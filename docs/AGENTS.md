# AGENTS.md

How coding agents should work in this repository family.

## Read first

1. [DATA_POLICY.md](DATA_POLICY.md) — public data only
2. [GATE_CONTRACT.md](GATE_CONTRACT.md) — what pass means
3. [ARCHITECTURE.md](ARCHITECTURE.md) — spine vs runtime
4. The target repo’s `README.md` and `STATUS.md`

## Do

- Treat Meridian contracts in this kit as the schema source. Bump the kit version if you must change a field; do not silently diverge.
- Write or update tests / schema fixtures when you change contracts.
- Keep telemetry and memory writes valid JSON / JSONL.
- Prefer mechanical checks (exit codes, schema validation) over prompt-only rules.
- Stay inside the current repo unless the task explicitly spans siblings.

## Do not

- Invent a second gate or memory schema.
- Commit secrets, `.env` files, identity documents, or recovery codes.
- Put JPO / F-35 / employer data in fixtures.
- Mark a gate complete because the generator said so.
- Build a from-scratch Claude Code replacement.
- Implement exploit tooling against systems you do not own (redteam-blue-gate is last and sandboxed against own / educational targets).

## Definition of done for foundation work

- Docs link the four shared contracts
- `python eval/validate_schemas.py` passes in portfolio-kit
- No nested `repo/repo` clone
- Each repo `STATUS.md` matches reality (see [STATUS.md](STATUS.md))

## Resume after pause (2026-08-19)

- Do **not** start redteam-blue-gate or a new coding harness.
- Next implementation: agent-framework-bakeoff Phase 1 (CONTRACT/SPEC + golden set).
- Honesty-gate leftover is manual (`dsh-plugin` topic, optional live `dsh plugin add`).
