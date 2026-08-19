# Contributing

This repository versions **contracts**, not product features.

## Change control

1. Open a PR that updates **both** the markdown contract and the matching file under `schemas/` when a field changes.
2. Bump the “Contract version” line in the affected docs (semver).
3. Add or update a fixture in `schemas/examples/` and keep `python eval/validate_schemas.py` green.
4. Note the bump in sibling READMEs only after the kit is tagged.

## Style

- Public / unclassified examples only.
- Prefer short, testable statements over essays.
- Do not rewrite Meridian internals here. Link to Meridian and copy the contract surface.

## License

MIT. See [LICENSE](LICENSE).
