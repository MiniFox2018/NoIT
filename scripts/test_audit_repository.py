#!/usr/bin/env python3
"""Regression tests for the repository's public Markdown audit contract."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE_SCRIPT = Path(__file__).with_name("audit_repository.py")
BASE_DOCUMENT = """---
title: 测试主题
tags:
  - 测试
status: active
updated: 2026-10-03
---

# 测试主题

## 学习内容

这是一份可以独立理解的知识记录。

## 来源与版本记录

- 资料名称：测试资料；处理于 2026-10-03。
"""


class RepositoryAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self._temporary.cleanup)
        self.root = Path(self._temporary.name)
        script_dir = self.root / "scripts"
        script_dir.mkdir()
        shutil.copyfile(SOURCE_SCRIPT, script_dir / "audit_repository.py")
        self.document = self.root / "知识库" / "示例" / "测试主题.md"
        self.document.parent.mkdir(parents=True)
        self.document.write_text(BASE_DOCUMENT, encoding="utf-8")
        (self.root / "README.md").write_text(
            "# 测试仓库\n\n- [测试主题](./知识库/示例/测试主题.md)\n",
            encoding="utf-8",
        )

    def run_audit(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(self.root / "scripts" / "audit_repository.py")],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_valid_minimal_repository(self) -> None:
        result = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 errors", result.stdout)

    def test_future_updated_is_an_error(self) -> None:
        self.document.write_text(
            BASE_DOCUMENT.replace("updated: 2026-10-03", "updated: 2999-01-01"),
            encoding="utf-8",
        )
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("updated 不能晚于今天", result.stdout)

    def test_future_resource_verification_is_an_error(self) -> None:
        resource = self.root / "资源库" / "测试工具" / "示例工具.md"
        resource.parent.mkdir(parents=True)
        resource.write_text(
            """---
title: 示例工具
tags:
  - 工具
type: resource
status: active
updated: 2026-10-03
verified: 2999-01-01
---

# 示例工具

- 官网：https://example.org/
""",
            encoding="utf-8",
        )
        readme = self.root / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8")
            + "\n- [示例工具](./资源库/测试工具/示例工具.md)\n",
            encoding="utf-8",
        )
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("verified 不能晚于今天", result.stdout)

    def test_unfinished_source_section_is_a_warning(self) -> None:
        self.document.write_text(
            BASE_DOCUMENT + "\n## 后续新增正文\n\n还有需要整理的知识。\n",
            encoding="utf-8",
        )
        result = self.run_audit()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("文档级来源章节之后仍出现 H2 标题", result.stdout)

    def test_broken_internal_markdown_link_is_an_error(self) -> None:
        self.document.write_text(
            BASE_DOCUMENT + "\n[缺失资料](./不存在.md)\n",
            encoding="utf-8",
        )
        result = self.run_audit()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Markdown 断链", result.stdout)


if __name__ == "__main__":
    unittest.main()
