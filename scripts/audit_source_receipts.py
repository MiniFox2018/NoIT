#!/usr/bin/env python3
"""Validate source provenance, or display the unfinished source-review queue."""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".github" / "audits" / "2026-10-09-source-receipts.json"
STATUSES = {
    "theme_integrated", "partially_integrated", "resource_indexed",
    "source_linked", "source_registered",
}
QUEUES = {
    "registered": "source_registered",
    "linked": "source_linked",
    "partial": "partially_integrated",
}


def targets(row: dict) -> list[str]:
    combined: list[str] = []
    for key in ("knowledge_target", "resource_target", "knowledge_targets", "resource_targets"):
        value = row.get(key)
        if isinstance(value, str) and value:
            combined.append(value)
        elif isinstance(value, list):
            combined.extend(entry for entry in value if isinstance(entry, str) and entry)
    return sorted(set(combined))


def validate(rows: list[dict], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    urls: set[str] = set()
    for n, row in enumerate(rows, 1):
        key = str(row.get("id") or "")
        url = row.get("url") or ""
        if not key or key in ids:
            errors.append(f"row {n}: missing or duplicate id {key}")
        ids.add(key)
        if not isinstance(url, str) or not url.startswith(("https://", "http://")) or url in urls:
            errors.append(f"row {n}: missing/invalid/duplicate URL {url}")
        urls.add(url)
        if row.get("knowledge_status") not in STATUSES:
            errors.append(f"row {n}: unknown knowledge_status")
        if not re.fullmatch(r"[0-9a-fA-F]{64}", str(row.get("sha256") or "")):
            errors.append(f"row {n}: missing/invalid SHA-256 evidence")
        try:
            recorded = date.fromisoformat(str(row["acquired_on"]))
            if recorded > date.today():
                errors.append(f"row {n}: future acquisition date")
        except (KeyError, ValueError, TypeError):
            errors.append(f"row {n}: missing/invalid acquired_on")
        if row.get("acquired") is not True:
            errors.append(f"row {n}: acquired flag does not match stored evidence")
        refs = targets(row)
        if row.get("knowledge_status") in {"theme_integrated", "partially_integrated", "resource_indexed", "source_linked"} and not refs:
            errors.append(f"row {n}: processed/linked source without target")
        for ref in refs:
            if ref.startswith("/") or ".." in Path(ref).parts or not (root / ref).is_file():
                errors.append(f"row {n}: missing/unsafe target {ref}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", choices=sorted(QUEUES))
    parser.add_argument("--limit", type=int, default=0, help="0 = all")
    args = parser.parse_args()
    rows = json.loads(SOURCE.read_text(encoding="utf-8"))
    errors = validate(rows)
    counts = Counter(row.get("knowledge_status") for row in rows)
    print(f"Source audit: {len(rows)} receipts, {len(errors)} errors")
    for status in sorted(STATUSES):
        print(f"  {status}: {counts[status]}")
    for error in errors:
        print("ERROR:", error)
    if args.queue:
        selected = [row for row in rows if row.get("knowledge_status") == QUEUES[args.queue]]
        print(f"\n## {args.queue} ({len(selected)}), current evidence state only\n")
        print("| Title | Original URL | Current target |")
        print("| --- | --- | --- |")
        for row in selected[: args.limit] if args.limit > 0 else selected:
            title = str(row.get("title") or "untitled").replace("|", r"\|").replace("\n", " ")
            dest = ", ".join(targets(row)).replace("|", r"\|") or "待判断"
            print(f"| {title} | {row.get('url')} | {dest} |")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
