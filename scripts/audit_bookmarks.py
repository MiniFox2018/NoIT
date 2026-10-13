#!/usr/bin/env python3
"""Offline structural audit of the two Chrome bookmark exports (no network requests)."""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = (
    ROOT / "exports" / "NoIT_常用书签.html",
    ROOT / "exports" / "NoIT_其他待选书签.html",
)
CATEGORIES = {
    "01 信息雷达", "02 数据洞察", "03 学习资料", "04 AI与开发",
    "05 视觉影像", "06 运营与商业", "07 数字服务",
}


@dataclass
class Bookmark:
    url: str
    title: str
    folder: tuple[str, ...]
    description: str = ""


class BookmarkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.entries: list[Bookmark] = []
        self.levels: list[str | None] = []
        self.pending_folder: str | None = None
        self.capture: str | None = None
        self.parts: list[str] = []
        self.current_href: str | None = None
        self.note_target: Bookmark | None = None
        self.notes: list[str] = []
        self.errors: list[str] = []
        self.root_folder: str | None = None

    def flush_note(self) -> None:
        if self.note_target is not None:
            self.note_target.description = " ".join(" ".join(self.notes).split())
            self.note_target = None
            self.notes = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"dt", "dl"}:
            self.flush_note()
        if tag == "h3":
            self.capture, self.parts = "h3", []
        elif tag == "dl":
            self.levels.append(self.pending_folder)
            self.pending_folder = None
        elif tag == "a":
            self.capture, self.parts = "a", []
            self.current_href = dict(attrs).get("href")
        elif tag == "dd":
            self.note_target = self.entries[-1] if self.entries else None
            self.notes = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.parts.append(data)
        elif self.note_target is not None:
            self.notes.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "h3" and self.capture == "h3":
            name = " ".join(" ".join(self.parts).split())
            self.pending_folder = name
            if self.root_folder is None:
                self.root_folder = name
            self.capture = None
        elif tag == "a" and self.capture == "a":
            title = " ".join(" ".join(self.parts).split())
            folder = tuple(value for value in self.levels if value)
            self.entries.append(Bookmark(self.current_href or "", title, folder))
            self.capture = None
        elif tag == "dl":
            self.flush_note()
            if self.levels:
                self.levels.pop()
            else:
                self.errors.append("orphan closing DL")
        elif tag == "dd":
            self.flush_note()

    def close(self) -> None:
        super().close()
        self.flush_note()
        if self.levels:
            self.errors.append("unclosed DL")


def parse_bookmarks(content: str) -> BookmarkParser:
    parser = BookmarkParser()
    parser.feed(content)
    parser.close()
    return parser


def canonical_url(url: str) -> str:
    """Conservative duplicate key; never remove query, hash, login or deep paths."""
    parts = urlsplit(url.strip())
    hostname = (parts.hostname or "").lower()
    if hostname.startswith("www."):
        hostname = hostname[4:]
    port = f":{parts.port}" if parts.port else ""
    path = parts.path.rstrip("/")
    # Treat http and https versions of the same address as candidate duplicates.
    return hostname + port + path + (f"?{parts.query}" if parts.query else "") + (f"#{parts.fragment}" if parts.fragment else "")


def audit_exports(paths: tuple[Path, Path] = EXPORTS) -> tuple[list[str], list[str], list[int]]:
    errors: list[str] = []
    warnings: list[str] = []
    counts: list[int] = []
    seen: dict[str, str] = {}
    curated_urls: set[str] = set()
    if not paths[0].parent.is_dir():
        return ["exports/ directory is missing"], [], []
    actual_files = {p.name for p in paths[0].parent.iterdir() if p.is_file()}
    expected_files = {p.name for p in paths}
    for name in sorted(actual_files - expected_files):
        errors.append(f"exports/: unexpected file {name}")
    for path in paths:
        if not path.is_file():
            errors.append(f"missing bookmark export: {path.name}")
            counts.append(0)
            continue
        content = path.read_text(encoding="utf-8")
        parser = parse_bookmarks(content)
        errors.extend(f"{path.name}: {e}" for e in parser.errors)
        if not content.startswith("<!DOCTYPE NETSCAPE-Bookmark-file-1>"):
            errors.append(f"{path.name}: missing Netscape bookmark doctype")
        counts.append(len(parser.entries))
        if not parser.entries:
            errors.append(f"{path.name}: contains no bookmarks")
        blank_descriptions = 0
        for item in parser.entries:
            parts = urlsplit(item.url)
            if parts.scheme.lower() not in {"http", "https"} or not parts.hostname:
                errors.append(f"{path.name}: invalid bookmark URL {item.url!r}")
                continue
            if not item.title:
                errors.append(f"{path.name}: empty bookmark title for {item.url}")
            if len(item.folder) != 3 or item.folder[1] not in CATEGORIES or not item.folder[2]:
                errors.append(f"{path.name}: invalid folder depth/category for {item.url}: {item.folder}")
            key = canonical_url(item.url)
            if path == paths[0]:
                curated_urls.add(key)
            if key in seen:
                errors.append(f"{path.name}: duplicate bookmark (also in {seen[key]}): {item.url}")
            else:
                seen[key] = path.name
            if not item.description:
                blank_descriptions += 1
        if path == paths[0] and blank_descriptions:
            errors.append(f"{path.name}: {blank_descriptions} selected bookmarks lack descriptions")
        elif blank_descriptions:
            warnings.append(
                f"{path.name}: {blank_descriptions} candidate bookmarks lack descriptions; "
                "add only confirmed, useful purposes rather than inventing them"
            )
    # The external URL list is not evidence of user selection. A separate approved
    # snapshot makes accidental removals and promotions detectable in a PR.
    baseline = paths[0].parent.parent / ".github" / "bookmarks" / "selected-urls.txt"
    if baseline.is_file():
        approved_urls = [
            line.strip() for line in baseline.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        ]
        approved = {canonical_url(url) for url in approved_urls}
        if len(approved) != len(approved_urls):
            errors.append("bookmarks selected-urls.txt: duplicate baseline URL")
        removed = approved - curated_urls
        promoted = curated_urls - approved
        if removed:
            errors.append(f"bookmarks: {len(removed)} approved selected URLs missing from 常用 (update baseline only on explicit choice)")
        if promoted:
            errors.append(f"bookmarks: {len(promoted)} selected URLs absent from approval baseline (update baseline only on explicit choice)")
    return errors, warnings, counts


def main() -> int:
    errors, warnings, counts = audit_exports()
    print(f"Bookmark audit: {sum(counts)} entries across {len(counts)} exports, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    for warning in warnings:
        print("WARNING:", warning)
    for error in errors:
        print("ERROR:", error)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
