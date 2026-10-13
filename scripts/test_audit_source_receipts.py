#!/usr/bin/env python3
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from audit_source_receipts import validate


class SourceReceiptTests(unittest.TestCase):
    def row(self) -> dict:
        return {
            "id": "1", "url": "https://example.org/article/1",
            "sha256": "a" * 64, "acquired": True, "acquired_on": "2026-10-09",
            "knowledge_status": "source_linked", "knowledge_targets": ["知识库/主题.md"],
        }

    def test_valid_traceable_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "知识库").mkdir()
            (root / "知识库" / "主题.md").write_text("# ok", encoding="utf-8")
            self.assertEqual(validate([self.row()], root), [])

    def test_missing_target_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertTrue(any("missing/unsafe target" in e for e in validate([self.row()], Path(tmp))))

    def test_duplicates_do_not_silently_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            errors = validate([self.row(), self.row()], Path(tmp))
            self.assertTrue(any("duplicate id" in e for e in errors))
            self.assertTrue(any("duplicate URL" in e for e in errors))

    def test_registered_source_may_have_no_target(self) -> None:
        row = self.row()
        row["knowledge_status"] = "source_registered"
        row["knowledge_targets"] = []
        self.assertEqual(validate([row], Path(".")), [])

    def test_partial_source_remains_partial(self) -> None:
        row = self.row()
        row["knowledge_status"] = "partially_integrated"
        row["knowledge_target"] = row.pop("knowledge_targets")[0]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "知识库").mkdir()
            (root / "知识库" / "主题.md").write_text("# ok", encoding="utf-8")
            self.assertEqual(validate([row], root), [])


if __name__ == "__main__":
    unittest.main()
