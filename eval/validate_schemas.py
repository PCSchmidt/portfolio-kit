#!/usr/bin/env python3
"""Validate portfolio-kit example fixtures against the published schemas.

Stdlib only. Run from repo root:

    python eval/validate_schemas.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = SCHEMAS / "examples"

# Draft-07 subset used by these contracts. Avoids a jsonschema dependency.
FORMAT_DATE_TIME_KEYS = {
    "timestamp",
    "created",
    "last_validated",
    "last_updated",
    "date",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path}: invalid JSON ({exc})")
        raise


def load_jsonl(path: Path) -> list[object]:
    rows: list[object] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            fail(f"{path}:{i}: invalid JSON ({exc})")
    if not rows:
        fail(f"{path}: empty JSONL")
    return rows


def require_keys(obj: dict, keys: list[str], where: str) -> None:
    missing = [k for k in keys if k not in obj]
    if missing:
        fail(f"{where}: missing keys {missing}")


def check_datetime(value: object, where: str) -> None:
    if not isinstance(value, str) or "T" not in value:
        fail(f"{where}: expected ISO-8601 date-time, got {value!r}")


def validate_semantic(obj: object, where: str) -> None:
    if not isinstance(obj, dict):
        fail(f"{where}: expected object")
    require_keys(obj, ["schema_version", "memory_type", "patterns"], where)
    if obj["schema_version"] != "1.0" or obj["memory_type"] != "semantic":
        fail(f"{where}: schema_version/memory_type mismatch")
    if not isinstance(obj["patterns"], list) or not obj["patterns"]:
        fail(f"{where}: patterns must be a non-empty list")
    for i, pattern in enumerate(obj["patterns"]):
        loc = f"{where}.patterns[{i}]"
        if not isinstance(pattern, dict):
            fail(f"{loc}: expected object")
        require_keys(
            pattern,
            [
                "pattern_id",
                "description",
                "context",
                "confidence",
                "validated_count",
                "hash",
                "created",
                "last_validated",
            ],
            loc,
        )
        if not str(pattern["pattern_id"]).startswith("PAT-"):
            fail(f"{loc}: pattern_id must start with PAT-")
        if pattern["confidence"] not in {"LOW", "MEDIUM", "HIGH"}:
            fail(f"{loc}: bad confidence")
        if len(str(pattern["hash"])) != 64:
            fail(f"{loc}: hash must be 64 hex chars")
        check_datetime(pattern["created"], f"{loc}.created")
        check_datetime(pattern["last_validated"], f"{loc}.last_validated")


def validate_episodic(obj: object, where: str) -> None:
    if not isinstance(obj, dict):
        fail(f"{where}: expected object")
    require_keys(obj, ["timestamp", "event_type", "session_id"], where)
    allowed = {
        "session_start",
        "session_end",
        "gate_passed",
        "gate_blocked",
        "stop_event",
        "feature_complete",
        "error_logged",
    }
    if obj["event_type"] not in allowed:
        fail(f"{where}: unknown event_type {obj['event_type']!r}")
    if len(str(obj["session_id"])) != 8:
        fail(f"{where}: session_id must be 8 hex chars")
    check_datetime(obj["timestamp"], f"{where}.timestamp")


def validate_correction(obj: object, where: str) -> None:
    if not isinstance(obj, dict):
        fail(f"{where}: expected object")
    require_keys(
        obj,
        ["session_id", "gate", "date", "project", "root_cause", "action_next"],
        where,
    )
    check_datetime(obj["date"], f"{where}.date")
    if len(str(obj["root_cause"])) < 10 or len(str(obj["action_next"])) < 10:
        fail(f"{where}: root_cause/action_next too short")


def validate_verdict(obj: object, where: str) -> None:
    if not isinstance(obj, dict):
        fail(f"{where}: expected object")
    require_keys(
        obj,
        [
            "gate",
            "session_id",
            "timestamp",
            "evaluator",
            "artifacts_reviewed",
            "scores",
            "overall",
            "issues",
            "verdict",
            "notes",
        ],
        where,
    )
    scores = obj["scores"]
    if not isinstance(scores, dict):
        fail(f"{where}: scores must be object")
    for key in ("completeness", "quality", "consistency", "spec_adherence"):
        if key not in scores:
            fail(f"{where}: missing score {key}")
        val = scores[key]
        if not isinstance(val, (int, float)) or not 0 <= val <= 10:
            fail(f"{where}.scores.{key}: must be 0-10")
    if obj["verdict"] not in {"pass", "warn", "fail"}:
        fail(f"{where}: bad verdict")
    overall = obj["overall"]
    if not isinstance(overall, (int, float)) or not 0 <= overall <= 10:
        fail(f"{where}: overall must be 0-10")
    check_datetime(obj["timestamp"], f"{where}.timestamp")


def validate_telemetry(obj: object, where: str) -> None:
    if not isinstance(obj, dict):
        fail(f"{where}: expected object")
    require_keys(obj, ["timestamp", "event_type", "session_id", "project"], where)
    check_datetime(obj["timestamp"], f"{where}.timestamp")


def main() -> None:
    for name in (
        "memory-schema.json",
        "evaluator-verdict.schema.json",
        "telemetry-schema.json",
    ):
        path = SCHEMAS / name
        if not path.is_file():
            fail(f"missing schema {path}")
        load_json(path)

    validate_semantic(load_json(EXAMPLES / "semantic.json"), "semantic.json")
    for i, row in enumerate(load_jsonl(EXAMPLES / "episodic.jsonl")):
        validate_episodic(row, f"episodic.jsonl:{i + 1}")
    for i, row in enumerate(load_jsonl(EXAMPLES / "corrections.jsonl")):
        validate_correction(row, f"corrections.jsonl:{i + 1}")
    validate_verdict(
        load_json(EXAMPLES / "evaluator-verdict.json"),
        "evaluator-verdict.json",
    )
    for i, row in enumerate(load_jsonl(EXAMPLES / "telemetry.jsonl")):
        validate_telemetry(row, f"telemetry.jsonl:{i + 1}")

    print("OK: portfolio-kit schemas and examples validated")


if __name__ == "__main__":
    main()
