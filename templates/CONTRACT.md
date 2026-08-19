# CONTRACT.md

**Project:** [Project name]
**Owner:** Chris Schmidt
**Date:** [YYYY-MM-DD]
**Reliability layer:** Meridian contracts via [portfolio-kit](https://github.com/PCSchmidt/portfolio-kit)

---

## Scope

[One paragraph: what it does and who uses it.]

### In scope

- [Capability 1]
- [Capability 2]
- Public / unclassified fixtures only

### Out of scope

- JPO / F-35 / employer program data
- Replacing Claude Code / Cursor / Copilot
- [Other explicit exclusions]

---

## Stack

| Layer | Technology |
|-------|------------|
| Runtime | [dsh / LangGraph / Haystack / …] |
| Reliability | Meridian gate + independent Evaluator contracts |
| Models | [named, versioned] |
| Deploy | [local / Docker / none] |

---

## Acceptance criteria

A feature is not complete until:

1. Happy path works against the written SPEC
2. Mechanical gate hooks exit 0
3. Independent Evaluator returns `pass` when the gate requires it
4. Eval table uses [EVAL_RUBRIC_TEMPLATE.md](https://github.com/PCSchmidt/portfolio-kit/blob/main/docs/EVAL_RUBRIC_TEMPLATE.md)
5. Data policy grep is clean

---

## Known constraints

- [API rate limits, CPU-only, etc.]
