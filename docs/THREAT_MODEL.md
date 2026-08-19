# Threat Model Template

**Contract version:** 0.1.0  
Copy this file into a project and fill the tables. Do not claim residual risk is zero.

## System

- **Name:**
- **Trust boundary:** local CLI / CI / public demo
- **Data class:** public / unclassified (see DATA_POLICY.md)
- **Actors:** operator, coding agent, Evaluator, optional external tools

## Assets

| Asset | Why it matters |
|-------|----------------|
| Gate verdict integrity | False pass ships unfinished work |
| Memory store | Poisoned patterns change future sessions |
| Tool credentials | API keys, git tokens |
| Target codebase (red/blue) | Accidental damage outside sandbox |
| User-facing answer (RAG) | Hallucinated citations |

## Threats (starter set)

| ID | Threat | Example | Mitigation |
|----|--------|---------|------------|
| T1 | Tool misuse | Agent runs destructive git or network calls | Least-privilege tools; blocklists; exit-2 hooks |
| T2 | Hallucinated completion | Generator marks gate done; tests fail | Mechanical verify + independent Evaluator |
| T3 | Memory poisoning | Model writes a false HIGH-confidence pattern | Schema validation; human review for semantic writes |
| T4 | Prompt injection via retrieved docs | RAG corpus contains “ignore gates” | Treat retrieval as untrusted; Evaluator after synthesis |
| T5 | Sandbox escape | Red-team agent reaches host | Containers, no docker.sock, no privileged mode |
| T6 | SSRF / data exfil via tools | Agent fetches internal URLs | Allowlist public hosts; no cloud-metadata IPs |
| T7 | Self-grading | Same session scores its own work | Fresh-context Evaluator only |
| T8 | Scope drift | Extra features land mid-gate | Drift sensor + CONTRACT/SPEC artifacts |

## Residual risk

Document what you are **not** mitigating in v1 (for example: no formal proof of sandbox isolation; LLM-as-judge noise).
