#!/usr/bin/env python3
"""Offline regression tests for URL extraction and durable link-audit snapshots."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from audit_external_links import (
    build_report,
    extract_urls,
    non_public_host,
    request_url,
    write_report,
)


class ExternalLinkAuditTests(unittest.TestCase):
    def test_extract_urls_ignores_fences_and_strips_punctuation(self):
        text = (
            "Reference: https://example.com/docs.\n"
            "\n```text\nhttps://excluded.example.com\n```\n"
            "Another (https://example.org/a).\n"
        )
        self.assertEqual(
            extract_urls(text),
            {"https://example.com/docs", "https://example.org/a"},
        )

    def test_non_public_literal_hosts_are_skipped_without_network(self):
        for hostname in (
            "localhost", "localhost.", "build.local", "127.0.0.2",
            "10.0.0.1", "192.168.1.1", "169.254.169.254", "::1",
            "fc00::1",
        ):
            with self.subTest(hostname=hostname):
                self.assertTrue(non_public_host(hostname))
        self.assertFalse(non_public_host("example.com"))
        self.assertFalse(non_public_host("8.8.8.8"))
        with patch("audit_external_links.urllib.request.urlopen") as opener:
            self.assertEqual(request_url("http://127.0.0.2/")[0], "skip")
            opener.assert_not_called()

    def test_report_contains_full_traceable_classification(self):
        sources = {
            "https://a.example.com": {"资源库/a.md", "知识库/b.md"},
            "https://z.example.com": {"资源库/z.md"},
        }
        results = {
            "https://z.example.com": ("soft", 403, "blocked"),
            "https://a.example.com": ("ok", 200, "reachable"),
        }
        report = build_report(sources, results)
        self.assertEqual(report["schema_version"], 2)
        self.assertFalse(report["permanent_failure_verified"])
        self.assertEqual(report["totals"]["unique_urls"], 2)
        self.assertEqual(report["totals"]["ok"], 1)
        self.assertEqual(report["totals"]["soft"], 1)
        self.assertEqual(
            [item["url"] for item in report["results"]],
            ["https://a.example.com", "https://z.example.com"],
        )
        self.assertEqual(
            report["results"][0]["source_files"],
            ["知识库/b.md", "资源库/a.md"],
        )

    def test_json_report_is_utf8_and_written_only_when_enabled(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "audit" / "results.json"
            report = {"results": [{"source_files": ["知识库/测试.md"]}]}
            with patch.dict(os.environ, {"NOIT_LINK_AUDIT_REPORT": str(path)}):
                write_report(report)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), report)
            path.unlink()
            with patch.dict(os.environ, {"NOIT_LINK_AUDIT_REPORT": ""}):
                write_report(report)
            self.assertFalse(path.exists())


    def test_404_is_only_suspect_not_a_permanent_failure(self):
        import urllib.error

        url = "https://example.com/missing"
        error = urllib.error.HTTPError(url, 404, "Not Found", None, None)
        with patch("audit_external_links.urllib.request.urlopen", side_effect=error):
            status, code, detail = request_url(url)
        self.assertEqual((status, code), ("suspect", 404))
        self.assertIn("not independent evidence", detail)

        report = build_report({url: {"资源库/测试.md"}}, {url: (status, code, detail)})
        self.assertEqual(report["totals"]["suspect"], 1)
        self.assertFalse(report["permanent_failure_verified"])

if __name__ == "__main__":
    unittest.main()
