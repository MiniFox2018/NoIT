#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FORMAL_ROOTS = (ROOT / "知识库", ROOT / "资源库")
REQUIRED_FIELDS = ("title", "tags", "status", "updated")

errors: list[str] = []
warnings: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def outside_fences(text: str) -> list[str]:
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
    return result


def frontmatter(text: str) -> str | None:
    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
    return match.group(1) if match else None


def has_field(fm: str, field: str) -> bool:
    if field == "tags":
        return bool(re.search(r"^tags:\s*(?:\[.*\])?\s*$", fm, re.M))
    return bool(re.search(rf"^{re.escape(field)}:\s*\S.*$", fm, re.M))


formal_docs: list[Path] = []
for root in FORMAL_ROOTS:
    if root.exists():
        formal_docs.extend(
            path
            for path in root.rglob("*.md")
            if path.name != "AGENTS.md"
        )
formal_docs = sorted(formal_docs)

all_md = sorted(ROOT.rglob("*.md"))
stem_index: dict[str, list[Path]] = defaultdict(list)
for path in all_md:
    stem_index[path.stem].append(path)

for path in formal_docs:
    text = read(path)
    fm = frontmatter(text)
    if fm is None:
        errors.append(f"{rel(path)}: 缺少 YAML Frontmatter")
    else:
        for field in REQUIRED_FIELDS:
            if not has_field(fm, field):
                errors.append(f"{rel(path)}: Frontmatter 缺少 {field}")
        if rel(path).startswith("资源库/"):
            type_match = re.search(r"^type:\s*(\S+)\s*$", fm, re.M)
            if not type_match or type_match.group(1) not in {"resource", "resource-index"}:
                errors.append(f"{rel(path)}: 资源文档 type 应为 resource 或 resource-index")

    h1_count = sum(1 for line in outside_fences(text) if re.match(r"^#\s+\S", line))
    if h1_count != 1:
        errors.append(f"{rel(path)}: H1 数量为 {h1_count}，应为 1")

readme = ROOT / "README.md"
if not readme.exists():
    errors.append("README.md: 文件不存在")
else:
    readme_text = read(readme)
    indexed: set[str] = set()
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme_text):
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
        if not target:
            continue
        if target.startswith("./"):
            target = target[2:]
        indexed.add(Path(target).as_posix())

    for path in formal_docs:
        r = rel(path)
        if r not in indexed:
            errors.append(f"README.md: 未索引正式文档 {r}")

for path in all_md:
    text = read(path)

    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if target.startswith("#") or re.match(r"^(?:https?|mailto):", target):
            continue
        clean = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
        if not clean:
            continue
        if clean.startswith("file://"):
            errors.append(f"{rel(path)}: 存在本机 file:// 链接 {clean}")
            continue
        if clean.startswith("/"):
            candidate = ROOT / clean.lstrip("/")
        else:
            candidate = (path.parent / clean).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{rel(path)}: 相对链接越出仓库 {target}")
            continue
        if clean.endswith(".md") and not candidate.exists():
            errors.append(f"{rel(path)}: Markdown 断链 {target}")

    for target in re.findall(r"\[\[([^\]]+)\]\]", text):
        clean = target.split("|", 1)[0].split("#", 1)[0].strip()
        if not clean:
            continue
        clean_path = Path(clean)
        if "/" in clean or "\\" in clean:
            candidate = path.parent / clean_path
            if candidate.suffix != ".md":
                candidate = candidate.with_suffix(".md")
            if not candidate.exists():
                errors.append(f"{rel(path)}: Obsidian 断链 [[{target}]]")
        else:
            stem = clean_path.stem
            matches = stem_index.get(stem, [])
            if not matches:
                errors.append(f"{rel(path)}: Obsidian 断链 [[{target}]]")
            elif len(matches) > 1:
                warnings.append(
                    f"{rel(path)}: Obsidian 链接 [[{target}]] 存在 {len(matches)} 个同名目标"
                )

raw_path_patterns = (
    re.compile(r"/Users/[^/\s]+/[^\s)]+"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\[^\s)]+"),
)
for path in formal_docs:
    text = read(path)
    for pattern in raw_path_patterns:
        for match in pattern.finditer(text):
            errors.append(f"{rel(path)}: 疑似本机绝对路径 {match.group(0)}")

print(
    f"Repository audit: {len(formal_docs)} formal docs, "
    f"{len(all_md)} markdown files, {len(errors)} errors, {len(warnings)} warnings."
)
for warning in warnings:
    print(f"WARNING: {warning}")
for error in errors:
    print(f"ERROR: {error}")

sys.exit(1 if errors else 0)
