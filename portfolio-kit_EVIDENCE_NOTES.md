# portfolio-kit: Evidence Notes

Companion to `portfolio-kit.md`. Labels: Confirmed, Ran it, Per the docs, My reading, Ask the author, Author says. Repo at commit c39cbea (4 Sep 2026), read-only clone. All runs were in a scratch copy made with `git archive HEAD`; a scratch virtual environment held the one extra package (`jsonschema`). Nothing was installed globally and nothing was written in the clone.

## E1 Fact sheet

| Fact | Notes |
| --- | --- |
| Name, address, licence | portfolio-kit; github.com/PCSchmidt/portfolio-kit; MIT, LICENSE file present; public, 0 stars, 0 forks, no releases, no git tags (Confirmed via GitHub API and `git tag`). |
| Kind | Shared contracts, schemas, templates and one validator script (Confirmed). |
| Status | README: "Contracts 0.1.0 published"; docs/STATUS.md is a family hand-off dated 4 Sep 2026 (Per the docs). |
| Size | 32 tracked files; one Python file (eval/validate_schemas.py, 206 lines, stdlib only); the rest are Markdown, JSON, JSONL, YAML (Confirmed). |
| Tests | None of its own. The only check is the validator; it prints OK (Ran it, Python 3.14). |
| Commits | 19, 19 Aug to 4 Sep 2026, all authored under the owner's name. 0 of 19 carry a Co-Authored-By credit or any builder credit (Confirmed). 17 of 19 are small documentation notes; the first commit adds 31 files in one step. |
| Clean-copy run | `python eval/validate_schemas.py` succeeded from `git archive HEAD` (Ran it). |
| Needs | Python 3.11+, nothing else; no network, key or hardware (Confirmed). |
| CI | `.github/workflows/validate.yml`: checkout, setup Python 3.11, run the validator. 19 runs, all success (Confirmed via `gh run list`); the latest ten took 6 to 14 seconds. |
| Deployed? Users? | No deployment; no evidence of users besides the author (Confirmed absence). |
| Related | Meridian (spine) and five consumers named in the README: dsh-plugin-honesty-gate, agent-framework-bakeoff, living-docs-architect, meridian-jspace, gate-enforced-rag; redteam-blue-gate is "not started" (Per the docs). |

## E2 Reading and running log

Read: README, CONTRIBUTING, LICENSE, .gitignore, all nine docs plus STATUS, all schemas and examples, all templates, eval/validate_schemas.py, eval/README, docker/README, the CI workflow, full git log with stats. Not read: sibling repositories (outside the clone), Meridian, any `.env` (none present). Searched file text for secret-like words: only prose hits (policy text), no values. Commands (scratch copy): validator (OK); twelve one-field mutation probes (E4); mutation of templates/gates.yaml to create a loop (validator still OK); a malformed JSONL line (validator fails, correct); jsonschema Draft-07 `check_schema` on each schema and `iter_errors` on each example. Final `git status` in the clone: no changes.

## E3 Claims check

| ID | Claim (where) | Evidence | Level | Verdict |
| --- | --- | --- | --- | --- |
| CL-01 | "Contracts 0.1.0 published" (README) | Version label in docs; no tag, no release | L1 | Partly: labelled, not published as a release |
| CL-02 | Phase 0 done: docs, schemas, templates, CI stub | All present; the CI runs the validator | L2 | Supported |
| CL-03 | `python eval/validate_schemas.py` "validates schemas and examples" (README, CI step name) | The script parses the schemas as JSON only and hand-checks examples; it never applies the schemas | L2 | Partly (see E4) |
| CL-04 | Gate DAG "must be acyclic; cycles rejected at validate time" (GATE_CONTRACT) | Not done in this repo (script never reads YAML); loop probe accepted | L2 | Not supported here; may hold in Meridian |
| CL-05 | Evaluator weights sum to 1; verdict thresholds 7.0 / 5.0 (GATE_CONTRACT) | 0.30+0.25+0.20+0.25 = 1.0; sample overall 7.875 shown as 7.9 | L3 | Supported arithmetic; not machine-enforced |
| CL-06 | Sample correction: 3 of 4 hours = 0.75, variance -25% | Recomputed | L3 | Supported |
| CL-07 | Meridian self-grading baseline -3.0 (5.5 vs 2.5) (GATE_CONTRACT) | 2.5 - 5.5 = -3.0; underlying experiment is in Meridian, not here | L1 | Per the docs |
| CL-08 | Honesty-gate "already copies verdict + memory schemas at 0.1.0" (README) | Sibling not read | none | Per the docs |
| CL-09 | Sibling figures in STATUS (32/32 tests, 36-case set, 39-case eval, GER-001 to 028) | Siblings not read here | none | Per the docs |
| CL-10 | Phases 1 to 3 (loader, Docker image, versioned releases) | docker/ holds README and .gitkeep; eval has only the validator | L2 | Planned only, correctly labelled as planned |

## E4 Rule attacks (Ran it, scratch copy)

Twelve single-field mutations of the valid samples; validator exit code and the Draft-07 library result (memory schema patched in scratch only, removing the invalid `exclusiveMinimum: true`).

| Mutation | Validator | Schema library |
| --- | --- | --- |
| Verdict "pass" with overall 1.0 | accepted | accepted (rule not in schema) |
| Extra field on verdict | accepted | refused |
| Quality score 12 | refused | refused |
| Severity "catastrophic" | accepted | refused |
| Hash of 64 `z` characters | accepted | refused |
| pattern_id "PAT-bad" | accepted | refused |
| session_id "zzzzzzzz" | accepted | refused |
| Outcome "maybe" | accepted | refused |
| Telemetry event_type "nope" | accepted | refused |
| Telemetry cost_usd -5 | accepted | refused |
| Correction gate = 7 | accepted | refused |
| Correction actual_hours -1 | accepted | refused (after patch) |

Result: validator refused 1 of 12; schemas (via library) refused 11 of 12. Other probes: loop in templates/gates.yaml accepted (validator never reads YAML; grep for "yaml|gates" in the script returns 0); malformed JSONL line refused; emptied episodic.jsonl refused by design.

## E5 Code map

docs/ (9 contract docs + STATUS); schemas/ (evaluator-verdict.schema.json, memory-schema.json, telemetry-schema.json, gate-schema.yaml, examples/ with 5 samples); templates/ (CONTRACT.md, SPEC.md, gates.yaml); eval/validate_schemas.py (functions validate_semantic, validate_episodic, validate_correction, validate_verdict, validate_telemetry, main); docker/ (placeholder); .github/workflows/validate.yml.

## E6 Model call sites

None. No model, no network call, no key.

## E7 Tests and CI

No test suite. CI runs the validator only. Spot-check of the "tests": the validator's verdict check asserts presence of keys, 0 to 10 range for four scores and overall, verdict in {pass, warn, fail}; it does not compare overall to the weighted sum or verdict to thresholds. Coverage: not applicable.

## E8 Plan-versus-results and history

No results exist, so no plan-versus-results question. History: first commit 19 Aug 13:20 (-0400) is a one-line workspace note followed by the 31-file foundation commit the same day; 17 later commits are one-line family-status notes. GitHub API reports last push 28 Sep 2026 although the last commit is 4 Sep (My reading: a later push of the same history; not investigated). Builder credits: none.

## E9 Gates and approvals

The kit defines gates and a human-approval token but contains no gate engine and no record of any approval.

## E10 Environment

No dependencies; Python 3.11+ stated; validator ran on 3.14. The extra package used for cross-checks (jsonschema) is not part of the repo.

## E11 Security and privacy

Secret-word scan of files: only policy prose. No `.env` in clone; `.gitignore` covers `.env` and variants except `.env.example`. Docs include local machine paths in the workspace map (not secrets; kept out of the guide). No outside services used. History scan limited to a text search of tracked files at HEAD plus commit messages (My reading: adequate for a 32-file docs repo; a dedicated secret scanner was not run).

## E12 Shortcomings register

| ID | Shortcoming | Evidence | Severity | Disclosed? | Options | Recommendation | Effort / payoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | Validator does not apply the schemas; 1 of 12 bad records caught | E4 | High | No (README says "validate schemas and examples") | A: use a real schema library in a venv; B: extend hand rules; C: reword and leave | A, keep script as wrapper (breaks the "no third-party packages" line, update README) | Small / High |
| S2 | memory-schema.json invalid under Draft-07 (`exclusiveMinimum: true` is Draft-04 style) | jsonschema check_schema error | Medium | No | A: use numeric `exclusiveMinimum: 0`; B: state Draft-04 | A | Small / Medium |
| S3 | Verdict arithmetic and thresholds not enforced anywhere here | E4 first row | Medium | Partly (doc says what pass means) | A: add arithmetic check to script; B: leave to siblings | A | Small / Medium |
| S4 | Gate list never validated; no DAG or reference check | E4 loop probe; gate-schema.yaml says "not a JSON Schema" | Medium | Reference says so; contract text implies a validate step | A: add YAML check with a loop test; B: document that Meridian owns it | A | Medium / Medium |
| S5 | No tags or releases despite "published 0.1.0" | `git tag` empty; gh release empty | Low | No | tag v0.1.0 | Tag | Small / Medium |
| S6 | Consumers copy schemas; no drift check | README says siblings copy | Medium | No | A: conformance test in one sibling; B: vendoring script | A | Medium / High |
| S7 | Minor doc mismatches ("four shared contracts" vs nine listed; README phase list stale; docker placeholder) | AGENTS.md, README | Low | n/a | Correct wording | Correct | Small / Low |

## E13 Math and method detail

Overall = 0.30 completeness + 0.25 quality + 0.20 consistency + 0.25 spec_adherence. Sample: 2.4 + 1.875 + 1.6 + 2.0 = 7.875. Verdict: pass if overall >= 7.0 and no high issue; warn if >= 5.0 and no high issue; fail otherwise. Self-grading delta = evaluator.overall - generator_self.overall (baseline -3.0). Correction: delta_ratio = actual/predicted = 0.75; variance_percent = (actual - predicted)/predicted x 100 = -25. Semantic dedupe by 64-hex SHA-256 hash (per docs; the hash in the sample was not recomputed because the hashed text is not specified).

## E14 Discrepancies

README and CI say "validate schemas"; script hand-checks. GATE_CONTRACT claims a loop is rejected at validate time; this repo does not do it. AGENTS.md "four shared contracts" vs README's nine docs. README "published" vs no tag. memory-schema `exclusiveMinimum: true`. Episodic schema allows `outcome` values (pass/fail/warn/block) with no cross-check against event type.

## E15 Production readiness detail

Reusable-from-clean-start: yes (one command). Checks that block a bad change: partly (E4). Quality against baseline: not applicable. Safe failure handling: not applicable. Human review: documented, not enforced. Versioning: labels only, no tags. Logs and monitoring: telemetry format defined, no writer. Data and secrets: data policy, `.gitignore`, scan clean. Placement: Works locally. Gap to deployable: tagged releases, real schema validation, conformance test, drift handling. Showcase: not suited.

## E16 Review dispositions

Self-review during drafting: corrected an initial claim that all twelve bad records break schema rules (one, verdict versus score, is prose-only); corrected CI run count (19, not the ten first listed); removed a motive for the data choice that the repo does not state.

## E17 Completeness and backlog

| Promised | Status |
| --- | --- |
| Shared docs, schemas, templates, CI (Phase 0) | Done; validator partial |
| Golden-set loader and scoring helpers (Phase 1) | Planned only |
| Docker base image, reusable Actions (Phase 2) | Planned only (placeholder) |
| Versioned schema releases (Phase 3) | Planned only; no tags yet |
| Threat model | Blank template by design |

Backlog. Fix: S1, S2, S3, S5, S7. Finish: Phase 1 loader once two runtimes emit the same case JSON. Improve: S4, S6. Add: conformance test; tagged release. Next milestone: stricter checker plus a v0.1.0 tag; exit test is that all twelve probe records are refused. Overall: finish small, then freeze.

## Revision log (v1 to v2 draft, reader-check fixes)
Archived prior draft as portfolio-kit.v1draft.md (5,286 words by wc -w). Revised draft is about 4,150 words by wc -w. No facts or numbers changed; all figures re-used from E1 to E4.
1. Opening now leads with "no AI, fixed rules" and the calculator-versus-forecast point; licence and status details kept short beneath it.
2. Gate, judge, Meridian, sibling projects and contract/schema defined in plain words at first use (opening paragraphs); sibling projects listed once by kind.
3. One running example (an agent says "done", a gate refuses until checks pass) introduced early and referred back to in the user, rules and results chapters.
4. The checker's one-in-twelve flaw stated in the opening caveats and in the shortcomings; repeats trimmed from the real-use, strengths and results chapters. A note added that the twelve breakages were chosen by me, so it is not a general catch rate.
5. Eleven-case sentence cut to five examples plus the picture (which still lists all twelve); eight-row table replaced by short prose.
6. Rules chapter: DAG and SHA-256 dropped, exit code kept to one clause, formula paragraph merged into the worked example; memory kinds explained in one sentence each.
7. Jargon replaced or defined: conformance test, virtual environment ("isolated Python setup"), thin wrapper ("short wrapper"), drift, pin to a release, scratch copy, held-out, commit.
8. Recruiter table removed; what it shows and does not show kept in prose; Q&A turned into a short list.
9. Glossary gained Meridian, sibling projects, judge, conformance test. No outline codes, confirm section, local paths or builder tool names in the guide.
10. Pictures: no labels or numbers changed, so none regenerated; parts and checker-probes images viewed, no clipped or overlapping text.

## Review fix: parts picture (docker wording)
Reviewer finding (parts picture said the docker folder is "empty") confirmed: clone docker/ holds README.md, a placeholder note ("Phase 0 ships no image"). Regenerated images/portfolio-kit-parts.png (matplotlib in a scratch venv, same layout and style); footer now reads "...a container image (the docker folder holds a placeholder note only)". Viewed: no clipped or overlapping text. Scanned the other three pictures (learned-vs-rules, verdict-flow, checker-probes) against the guide: no conflicting wording (verdict-flow "spec adherence" and "warn" are shorthand for the guide's "fit to the written specification" and "warning"; left unchanged). Guide text unchanged.
