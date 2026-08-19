# Eval Rubric Template

**Contract version:** 0.1.0

Use this rubric for every public eval table in the family. Score **0–10** unless the metric is a rate (then report percent + n). Always publish golden-set size, judge calibration (or inter-annotator agreement), and a short failure retrospective.

## Dimensions

| ID | Dimension | What it measures | Typical target |
|----|-----------|------------------|----------------|
| D1 | Factual / citation accuracy | Grounded claims; citations resolve | ≥ 8 / 10 or ≥ 90% grounded |
| D2 | Completeness vs SPEC / CONTRACT | Required sections and acceptance criteria | ≥ 8 / 10 |
| D3 | Gate catch rate | Known-bad outputs blocked by mechanical gate or Evaluator | ≥ 85% |
| D4 | Hallucination / fabrication rate | Ungrounded entities, dates, citations | ≤ 10% of claims |
| D5 | Trajectory success (pass@k) | Reaches the written goal without human rescue | Report pass@1 and pass@3 |
| D6 | Recovery / resilience | Tool failure, empty retrieval, rate limit | Documented recovery path |
| D7 | Latency / cost | p50 / p95 wall time; tokens; USD | Report, no vanity target |
| D8 | Observability completeness | Step, tool, gate verdict, memory write logged | 100% of required event types |
| D9 | Interpretability | Human can say why the Evaluator rejected (J-space project) | Faithfulness ≥ 80% |

Evaluator-internal dimensions (completeness, quality, consistency, spec_adherence) remain those in [GATE_CONTRACT.md](GATE_CONTRACT.md). This rubric is for **published bake-offs and project reports**.

## Required report fields

- Golden-set size and split (train/dev/held-out if any)
- Model + version + decoding settings
- Seed(s)
- Date of run
- n for every rate
- Failure-mode tags (missing citation, scope drift, stub-as-done, tool timeout, …)
- “What I would do next”

## Scoring script hook

Later phases should emit one JSON object per case:

```json
{
  "case_id": "AIR-001",
  "project": "agent-framework-bakeoff",
  "runtime": "langgraph",
  "scores": { "D1": 8, "D2": 7, "D3": null },
  "gate_verdict": "pass",
  "notes": "Missing NOTAM citation on conflict 2"
}
```

Keep field names stable so the bake-off runner and honesty-gate harness can share loaders.
