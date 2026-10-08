#!/usr/bin/env python3
from __future__ import annotations

import concurrent.futures
import ipaddress
import json
import os
import re
import ssl
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
TIMEOUT_SECONDS = 12
MAX_WORKERS = 20
USER_AGENT = "Mozilla/5.0 (compatible; NoIT-Link-Audit/1.0; +https://github.com/MiniFox2018/NoIT)"
SOFT_HTTP_CODES = {401, 403, 405, 406, 409, 418, 425, 429}
SUSPECT_HTTP_CODES = {404, 410}
SKIP_HOSTS = {"localhost", "0.0.0.0"}


def outside_fences(text: str) -> str:
    result: list[str] = []
    in_fence = False
    fence = None
    backtick_fence = chr(96) * 3
    for line in text.splitlines():
        stripped = line.lstrip()
        current = None
        if stripped.startswith(backtick_fence):
            current = backtick_fence
        elif stripped.startswith("~~~"):
            current = "~~~"
        if current:
            if not in_fence:
                in_fence = True
                fence = current
            elif current == fence:
                in_fence = False
                fence = None
            continue
        if not in_fence:
            result.append(line)
    return "\n".join(result)


def extract_urls(text: str) -> set[str]:
    text = outside_fences(text)
    urls = set(re.findall(r"https?://[^\s<>\]\[\"']+", text))
    cleaned: set[str] = set()
    for url in urls:
        url = url.rstrip(".,;:!?，。；：！？")
        while url.endswith(")") and url.count("(") < url.count(")"):
            url = url[:-1]
        while url.endswith("}") and url.count("{") < url.count("}"):
            url = url[:-1]
        if url:
            cleaned.add(url)
    return cleaned


def non_public_host(host: str) -> bool:
    """Skip literal non-public addresses; a network response is not needed."""
    host = host.lower().rstrip(".")
    if not host or host in SKIP_HOSTS or host.endswith((".local", ".localhost")):
        return True
    try:
        return not ipaddress.ip_address(host).is_global
    except ValueError:
        return False


def request_url(url: str) -> tuple[str, int | None, str]:
    host = (urlsplit(url).hostname or "").lower()
    if non_public_host(host):
        return ("skip", None, "local or non-public host")

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Range": "bytes=0-1023",
    }
    request = urllib.request.Request(url, headers=headers, method="GET")
    context = ssl.create_default_context()

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS, context=context) as response:
            code = getattr(response, "status", 200)
            return ("ok", code, "reachable")
    except urllib.error.HTTPError as exc:
        if exc.code in SUSPECT_HTTP_CODES:
            return ("suspect", exc.code, "HTTP 404/410; not independent evidence of permanent failure")
        if exc.code in SOFT_HTTP_CODES:
            return ("soft", exc.code, "blocked/authenticated/rate-limited; manual review only")
        if 500 <= exc.code <= 599:
            return ("soft", exc.code, "server error; may be transient")
        return ("soft", exc.code, "HTTP response requires manual review")
    except urllib.error.URLError as exc:
        return ("soft", None, f"network/TLS/DNS error: {exc.reason}")
    except Exception as exc:
        return ("soft", None, f"unexpected error: {exc}")


def write_summary(lines: list[str]) -> None:
    path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def build_report(
    sources: dict[str, set[str]],
    results: dict[str, tuple[str, int | None, str]],
) -> dict:
    """A durable snapshot for comparison across scheduled runs."""
    records = []
    totals = {"ok": 0, "suspect": 0, "soft": 0, "skip": 0}
    for url in sorted(results):
        status, code, detail = results[url]
        totals[status] += 1
        records.append({
            "url": url,
            "status": status,
            "http_status": code,
            "detail": detail,
            "source_files": sorted(sources[url]),
        })
    return {
        "schema_version": 2,
        "permanent_failure_verified": False,  # Network scans alone cannot establish permanence.
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository": "MiniFox2018/NoIT",
        "commit_sha": os.environ.get("GITHUB_SHA"),
        "totals": {"unique_urls": len(results), **totals},
        "results": records,
    }


def write_report(report: dict) -> None:
    """Store locally for Actions upload; never commit scan output."""
    target = os.environ.get("NOIT_LINK_AUDIT_REPORT")
    if not target:
        return
    path = Path(target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")



def main() -> int:
    sources: dict[str, set[str]] = defaultdict(set)
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for url in extract_urls(text):
            sources[url].add(path.relative_to(ROOT).as_posix())

    results: dict[str, tuple[str, int | None, str]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_map = {executor.submit(request_url, url): url for url in sorted(sources)}
        for future in concurrent.futures.as_completed(future_map):
            url = future_map[future]
            results[url] = future.result()

    suspect = []
    soft = []
    skipped = []
    for url in sorted(results):
        status, code, detail = results[url]
        record = (url, code, detail, sorted(sources[url]))
        if status == "suspect":
            suspect.append(record)
        elif status == "soft":
            soft.append(record)
        elif status == "skip":
            skipped.append(record)

    print(
        f"External link audit: {len(results)} unique URLs, "
        f"{len(suspect)} suspect URLs (not confirmed permanently invalid), {len(soft)} manual-review, "
        f"{len(skipped)} skipped."
    )
    for url, code, detail, paths in suspect:
        print(f"WARNING: suspect (unconfirmed) [{code}] {url} :: {detail} :: {', '.join(paths)}")
    for url, code, detail, paths in soft:
        print(f"NOTICE: review [{code}] {url} :: {detail} :: {', '.join(paths)}")

    summary = [
        "## External link audit",
        "",
        f"- Unique URLs checked: **{len(results)}**",
        f"- Suspect only (404/410, NOT confirmed permanent): **{len(suspect)}**",
        f"- Manual review (auth/rate-limit/server/network): **{len(soft)}**",
        f"- Skipped local URLs: **{len(skipped)}**",
        "",
        "> This workflow is advisory: HTTP errors do not prove permanent failure. Independent reliable evidence is required before any permanent-failure decision; no resource is automatically deleted.",
    ]
    if suspect:
        summary.extend(["", "### Suspect URLs — requires independent evidence"])
        for url, code, _, paths in suspect[:100]:
            summary.append(f"- {code} {url} — {', '.join(paths)}")
    write_summary(summary)
    write_report(build_report(sources, results))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
