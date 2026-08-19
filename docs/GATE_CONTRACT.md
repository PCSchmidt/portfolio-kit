# Gate Contract

**Contract version:** 0.1.0  
**Adapted from:** Meridian [docs/gate-model.md](https://github.com/PCSchmidt/meridian/blob/main/docs/gate-model.md) and `.meridian/gate-schema.yaml`

A **gate** is a checkpoint in a DAG. Discipline is mandatory (no skipping). Shape is project-specific.

## What “pass” means

A gate is **passed** only when **all** of the following hold:

1. **Dependencies** in `requires` are already passed.
2. **Required artifacts** exist and are non-empty (not heading-only stubs).
3. **Mechanical pre-hooks** exit 0. Any hook that fails **exits 2** and **blocks**. The model cannot talk past exit 2.
4. **Independent Evaluator** (when the gate requires it) returns `verdict: pass` with `overall >= 7.0` and **no high-severity issues**.
5. **Human approval** (if `type: human_approval`) is an explicit token typed by a human, not inferred by the model.

A generator scoring its own work is **not** a pass.

## Mechanical vs prompt rules

| Kind | Binding? | Example |
|------|----------|---------|
| Prompt / system text | No | “Please run tests before claiming done” |
| Hook / verifier exit 2 | Yes | `run-tests.sh` fails → tool call / commit blocked |
| Evaluator `fail` | Yes | `overall < 5.0` or any high-severity issue |
| Evaluator `warn` | Advisory unless the project promotes it | `5.0 <= overall < 7.0` |

Principle: *if the model can hallucinate past it, it is not a real boundary.*

## Gate document (`gates.yaml`)

Required fields per gate (see [schemas/gate-schema.yaml](../schemas/gate-schema.yaml) and [templates/gates.yaml](../templates/gates.yaml)):

- `id`, `label`
- `type`: `automated` | `human_approval`
- `required`: boolean
- `requires`: list of other gate ids (AND)
- `requires_artifacts`: paths that must exist
- `hooks.pre` / `hooks.post`
- `emits`: optional artifact written on pass
- `on_fail`: `block_all_writes` | `block_gate_writes` | `warn`

The DAG must be acyclic. Circular graphs are rejected at validate time.

## Evaluator invocation

The Evaluator runs in a **fresh context**. It is told it did not produce the work. It returns only the JSON object in [schemas/evaluator-verdict.schema.json](../schemas/evaluator-verdict.schema.json).

Default Meridian weights (keep unless a project documents a change):

- completeness 0.30
- quality 0.25
- consistency 0.20
- spec_adherence 0.25

Verdict table:

| Condition | Verdict |
|-----------|---------|
| `overall >= 7.0` and no high-severity issues | `pass` |
| `overall >= 5.0` and no high-severity issues | `warn` |
| `overall < 5.0` **or** any high-severity issue | `fail` |

## Runtime mapping

| Runtime | Mechanical block | Evaluator |
|---------|------------------|-----------|
| Meridian | `gate-engine.sh verify` + `meridian-verify.sh` at commit/CI | `gate-evaluator` subagent |
| dsh / Cordis | Waterfall hook abort / reversible effect rollback | Fresh session service |
| LangGraph / CrewAI / Haystack | Node or component that refuses to emit the user-facing artifact | Same verdict schema |

## Self-grading delta

When both a generator self-score and an Evaluator score exist, publish:

`delta = evaluator.overall - generator_self.overall`

Meridian’s measured baseline was **−3.0** (self 5.5 vs independent 2.5). Target for honesty-gate: self-score remains ≥ 2.5 points more generous than the Evaluator on held-out bad work.
