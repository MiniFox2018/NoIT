#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from audit_bookmarks import audit_exports, canonical_url, parse_bookmarks


def html(name: str, urls: list[tuple[str, str]]) -> str:
    items = "".join(
        f'<DT><A HREF="{url}">{title}</A>\n<DD>用途说明\n'
        for url, title in urls
    )
    return (
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<DL><p>\n'
        f'<DT><H3>{name}</H3>\n<DL><p>\n'
        '<DT><H3>03 学习资料</H3>\n<DL><p>\n'
        '<DT><H3>课程与社群</H3>\n<DL><p>\n'
        + items + '</DL><p>\n</DL><p>\n</DL><p>\n</DL><p>\n'
    )


class BookmarkAuditTests(unittest.TestCase):
    def test_parser_keeps_descriptions_and_two_category_levels(self) -> None:
        p = parse_bookmarks(html("NoIT｜常用书签", [("https://example.com", "学习站")]))
        self.assertFalse(p.errors)
        self.assertEqual(len(p.entries), 1)
        self.assertEqual(p.entries[0].folder, ("NoIT｜常用书签", "03 学习资料", "课程与社群"))
        self.assertEqual(p.entries[0].description, "用途说明")

    def test_cross_file_duplicate_with_protocol_and_www_variation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            a, b = folder / "NoIT_常用书签.html", folder / "NoIT_其他待选书签.html"
            a.write_text(html("NoIT｜常用书签", [("https://www.example.com/", "A")]), encoding="utf-8")
            b.write_text(html("NoIT｜其他待选", [("http://example.com", "B")]), encoding="utf-8")
            errors, _, counts = audit_exports((a, b))
            self.assertEqual(counts, [1, 1])
            self.assertTrue(any("duplicate bookmark" in e for e in errors), errors)

    def test_missing_selected_description_blocks_but_candidate_only_warns(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            a, b = folder / "NoIT_常用书签.html", folder / "NoIT_其他待选书签.html"
            text = html("NoIT｜常用书签", [("https://one.example", "A")])
            a.write_text(text.replace("<DD>用途说明", ""), encoding="utf-8")
            b.write_text(html("NoIT｜其他待选", [("https://two.example", "B")]).replace("<DD>用途说明", ""), encoding="utf-8")
            errors, warnings, _ = audit_exports((a, b))
            self.assertTrue(any("selected bookmarks lack descriptions" in e for e in errors))
            self.assertTrue(any("candidate bookmarks" in w for w in warnings))

    def test_url_query_and_fragment_are_preserved_in_duplicate_key(self) -> None:
        self.assertNotEqual(canonical_url("https://example.com/?q=one"), canonical_url("http://example.com/?q=two"))
        self.assertNotEqual(canonical_url("https://example.com/docs#a"), canonical_url("https://example.com/docs#b"))

    def test_approved_selected_set_cannot_change_silently(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            exports = root / "exports"
            exports.mkdir()
            a, b = exports / "NoIT_常用书签.html", exports / "NoIT_其他待选书签.html"
            a.write_text(html("NoIT｜常用书签", [("https://unselected.example", "B")]), encoding="utf-8")
            b.write_text(html("NoIT｜其他待选", [("https://old.example", "A")]), encoding="utf-8")
            baseline = root / ".github" / "bookmarks"
            baseline.mkdir(parents=True)
            (baseline / "selected-urls.txt").write_text(
                "# Approved by user\nhttps://old.example\n", encoding="utf-8"
            )
            errors, _, _ = audit_exports((a, b))
            self.assertTrue(any("approved selected URLs missing" in e for e in errors), errors)
            self.assertTrue(any("absent from approval baseline" in e for e in errors), errors)

    def test_extra_export_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            a, b = folder / "NoIT_常用书签.html", folder / "NoIT_其他待选书签.html"
            a.write_text(html("NoIT｜常用书签", [("https://one.example", "A")]), encoding="utf-8")
            b.write_text(html("NoIT｜其他待选", [("https://two.example", "B")]), encoding="utf-8")
            (folder / "old-export.html").write_text("stale", encoding="utf-8")
            errors, _, _ = audit_exports((a, b))
            self.assertTrue(any("unexpected file" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
