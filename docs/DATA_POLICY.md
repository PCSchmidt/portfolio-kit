# Data Policy

**Contract version:** 0.1.0  
**Rule:** public, unclassified data only.

This family is a **portfolio shadow** of defense-adjacent data-modernization work. It is not a place for employer, program, or classified content.

## Forbidden

- JPO, F-35, or any real program-of-record inventory, schedules, or architecture
- Controlled unclassified information (CUI), ITAR, or export-controlled technical data
- Internal contractor documents, tickets, credentials, or network diagrams
- Personal identity documents, recovery codes, private keys, `.env` files
- Scraped content that the source ToS forbids republishing

If a document would not be appropriate on a public GitHub repo under your own name, it does not belong here.

## Allowed stand-ins

| Need | Public stand-in |
|------|-----------------|
| Airspace / flight context | Public ADS-B samples, published NOTAMs, public TFR summaries |
| Satellite geometry | Public TLEs (CelesTrak / Space-Track public sets) |
| Inventory / reconciliation | GSA / SAM.gov public award or catalog extracts, Wikipedia equipment lists, synthetic CSVs checked into `fixtures/` |
| Multi-repo synthesis | Your own public repos + other OSI-licensed public repos |
| RAG corpora | Wikipedia, arXiv abstracts, official public HTML/PDF |
| Security lab | Your own public repos or known **educational** vulnerable apps, run in Docker |

Prefer checking a **small fixture** into the repo over live scraping in CI.

## Attribution

Cite the public source and retrieval date in `fixtures/SOURCES.md` (or equivalent) for every dataset.

## Review trigger

Before the first public eval run of a project, grep the tree for program names, internal hostnames, and secret-like strings. A hit is a release blocker.
