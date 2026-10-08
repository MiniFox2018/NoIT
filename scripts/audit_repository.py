#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FORMAL_ROOTS = (ROOT / "知识库", ROOT / "资源库")
REQUIRED_FIELDS = ("title", "tags", "status", "updated")
ALLOWED_STATUS = {"active", "draft", "deprecated", "archived"}
ALLOWED_RESOURCE_TYPES = {"resource", "resource-index"}
STALE_RESOURCE_DAYS = 180

SOURCE_SECTION_RE = re.compile(
    r"^(?:"
    r"来源与版本记录|来源记录|来源与状态|来源与核验|来源补充|"
    r"来源、版本与吸收边界|来源完整性说明|新增来源|"
    r"参考资料|参考来源"
    r")$"
)
VERIFICATION_EVIDENCE_RE = re.compile(
    r"(?:本次重新核验日期|重新核验日期|核验日期|当前核验|核验于|核验：)"
    r"\\s*[：:]?\\s*(\\d{4}-\\d{2}-\\d{2})"
)

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


def scalar_field(fm: str, field: str) -> str | None:
    match = re.search(rf"^{re.escape(field)}:\s*(.*?)\s*$", fm, re.M)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1].strip()
    return value


def parse_tags(fm: str) -> list[str]:
    inline = re.search(r"^tags:\s*\[(.*?)\]\s*$", fm, re.M)
    if inline:
        return [
            item.strip().strip('"\'')
            for item in inline.group(1).split(",")
            if item.strip().strip('"\'')
        ]

    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^tags:\s*$", line):
            tags: list[str] = []
            for next_line in lines[i + 1 :]:
                item = re.match(r"^\s+-\s+(.+?)\s*$", next_line)
                if item:
                    value = item.group(1).strip().strip('"\'')
                    if value:
                        tags.append(value)
                    continue
                if next_line and not next_line[0].isspace():
                    break
            return tags
    return []


def parse_iso_date(value: str | None) -> date | None:
    if not value or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)


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

title_index: dict[str, list[Path]] = defaultdict(list)
knowledge_docs: list[Path] = []
resource_docs: list[Path] = []

for path in formal_docs:
    text = read(path)
    fm = frontmatter(text)
    r = rel(path)

    if fm is None:
        errors.append(f"{r}: 缺少 YAML Frontmatter")
        continue

    for field in REQUIRED_FIELDS:
        if scalar_field(fm, field) is None and field != "tags":
            errors.append(f"{r}: Frontmatter 缺少 {field}")
    tags = parse_tags(fm)
    if not tags:
        errors.append(f"{r}: tags 至少需要一个有效标签")

    title = scalar_field(fm, "title")
    if title:
        title_index[title].append(path)

    status = scalar_field(fm, "status")
    if status and status not in ALLOWED_STATUS:
        errors.append(
            f"{r}: status={status} 不在允许值 "
            f"{sorted(ALLOWED_STATUS)} 中"
        )

    updated_raw = scalar_field(fm, "updated")
    updated = parse_iso_date(updated_raw)
    if updated is None:
        errors.append(f"{r}: updated 应为有效 YYYY-MM-DD 日期")
    elif updated > date.today():
        errors.append(f"{r}: updated 不能晚于今天 ({updated.isoformat()})")

    # Verification is evidence of a completed review, not a document edit.
    verified_raw = scalar_field(fm, "verified")
    verified = parse_iso_date(verified_raw)
    if verified_raw is not None:
        if verified is None:
            errors.append(f"{r}: verified 应为有效 YYYY-MM-DD 日期")
        elif verified > date.today():
            errors.append(f"{r}: verified 不能晚于今天 ({verified.isoformat()})")

    verified_scope = scalar_field(fm, "verified_scope")
    if verified_scope is not None and verified_scope != "full":
        errors.append(f"{r}: verified_scope 只支持 full；局部核验应在正文记录")
    if verified_scope is not None and verified_raw is None:
        errors.append(f"{r}: verified_scope 缺少对应的 verified 日期")
    if r.startswith("知识库/") and verified_raw is not None and verified_scope != "full":
        errors.append(f"{r}: 知识文档全文核验须标注 verified_scope: full")

    review_after_raw = scalar_field(fm, "review_after")
    if review_after_raw is not None:
        review_after = parse_iso_date(review_after_raw)
        if review_after is None:
            errors.append(f"{r}: review_after 应为有效 YYYY-MM-DD 日期")
        else:
            if review_after <= date.today():
                warnings.append(f"{r}: 已达到风险复核提醒日期 {review_after.isoformat()}；到期不代表失效")
        if not scalar_field(fm, "review_reason"):
            errors.append(f"{r}: review_after 必须有 review_reason 说明风险依据")

    is_resource = r.startswith("资源库/")
    if is_resource:
        resource_docs.append(path)
        doc_type = scalar_field(fm, "type")
        if doc_type not in ALLOWED_RESOURCE_TYPES:
            errors.append(
                f"{r}: 资源文档 type 应为 resource 或 resource-index"
            )
        if verified is not None:
            if (date.today() - verified).days > STALE_RESOURCE_DAYS:
                warnings.append(
                    f"{r}: 资源核验距今超过暂行提醒阈值 "
                    f"{STALE_RESOURCE_DAYS} 天；不代表失效"
                )
        elif doc_type == "resource":
            evidence_dates = [
                parse_iso_date(match.group(1))
                for match in VERIFICATION_EVIDENCE_RE.finditer(text)
            ]
            evidence_dates = [item for item in evidence_dates if item]
            if evidence_dates:
                latest = max(evidence_dates)
                warnings.append(
                    f"{r}: 正文存在明确核验日期 {latest.isoformat()}，"
                    "但 Frontmatter 未记录 verified"
                )
            elif updated and (date.today() - updated).days > STALE_RESOURCE_DAYS:
                warnings.append(
                    f"{r}: 动态资源长期未更新且无 verified，建议重新核验当前状态"
                )
        elif updated and (date.today() - updated).days > STALE_RESOURCE_DAYS:
            warnings.append(
                f"{r}: 动态资源索引长期未更新且无 verified，建议按条目或批次重新核验"
            )
    else:
        knowledge_docs.append(path)

    lines = outside_fences(text)
    h1s = [
        re.match(r"^#\s+(.+?)\s*$", line).group(1).strip()
        for line in lines
        if re.match(r"^#\s+\S", line)
    ]
    if len(h1s) != 1:
        errors.append(f"{r}: H1 数量为 {len(h1s)}，应为 1")
    elif title and h1s[0] != title:
        errors.append(
            f"{r}: Frontmatter title 与 H1 不一致 "
            f"({title!r} != {h1s[0]!r})"
        )

    levels = [
        len(match.group(1))
        for line in lines
        if (match := re.match(r"^(#{1,6})\s+\S", line))
    ]
    for before, after in zip(levels, levels[1:]):
        if after > before + 1:
            warnings.append(
                f"{r}: 标题层级从 H{before} 跳到 H{after}"
            )
            break

    if not is_resource and not re.search(
        r"^#{2,4}\s+.*(?:来源|参考|资料|出处).*$", text, re.M
    ):
        warnings.append(
            f"{r}: 未发现明确的来源/参考章节，建议核对可追溯性"
        )

    if not is_resource:
        headings = [
            (len(match.group(1)), match.group(2).strip())
            for line in lines
            if (match := re.match(r"^(#{1,6})\s+(.+?)\s*$", line))
        ]
        source_indexes = [
            index
            for index, (level, heading) in enumerate(headings)
            if level == 2 and SOURCE_SECTION_RE.fullmatch(heading)
        ]
        new_source_count = sum(
            1 for _, heading in headings if heading == "新增来源"
        )
        if new_source_count > 1:
            warnings.append(
                f"{r}: 出现 {new_source_count} 个“新增来源”章节，"
                "建议归并到稳定的来源补充或统一来源记录"
            )
        if source_indexes:
            first_source_index = source_indexes[0]
            later_main_sections = [
                heading
                for level, heading in headings[first_source_index + 1 :]
                if level == 2
            ]
            if later_main_sections:
                warnings.append(
                    f"{r}: 文档级来源章节之后仍出现 H2 标题 "
                    f"{later_main_sections[0]!r}，请确认正文、使用边界和关联知识"
                    "已安排妥当，再把文档级来源记录置于末尾"
                )

for title, paths in title_index.items():
    if len(paths) > 1:
        warnings.append(
            f"重复 Frontmatter title {title!r}: "
            + ", ".join(rel(path) for path in paths)
        )

readme = ROOT / "README.md"
if not readme.exists():
    errors.append("README.md: 文件不存在")
else:
    readme_text = read(readme)
    indexed: set[str] = set()
    for target in markdown_links(readme_text):
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
    r = rel(path)

    for target in markdown_links(text):
        if target.startswith("#") or re.match(r"^(?:https?|mailto):", target):
            continue
        clean = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
        if not clean:
            continue
        if clean.startswith("file://"):
            errors.append(f"{r}: 存在本机 file:// 链接 {clean}")
            continue
        if clean.startswith("/"):
            candidate = ROOT / clean.lstrip("/")
        else:
            candidate = (path.parent / clean).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{r}: 相对链接越出仓库 {target}")
            continue
        if clean.endswith(".md") and not candidate.exists():
            errors.append(f"{r}: Markdown 断链 {target}")

    for target in re.findall(r"\[\[([^\]]+)\]\]", text):
        clean = target.split("|", 1)[0].split("#", 1)[0].strip()
        if not clean:
            continue
        clean_path = Path(clean)
        if "/" in clean or "\\" in clean:
            candidate = path.parent / (
                clean if clean.endswith(".md") else clean + ".md"
            )
            if not candidate.exists():
                errors.append(f"{r}: Obsidian 断链 [[{target}]]")
        else:
            stem = clean[:-3] if clean.endswith(".md") else clean
            matches = stem_index.get(stem, [])
            if not matches:
                errors.append(f"{r}: Obsidian 断链 [[{target}]]")
            elif len(matches) > 1:
                warnings.append(
                    f"{r}: Obsidian 链接 [[{target}]] 存在 "
                    f"{len(matches)} 个同名目标"
                )

raw_path_patterns = (
    re.compile(r"file:///(?:Users|home)/[^\s)`]+"),
    re.compile(r"/Users/[^/\s]+/[^\s)`]+"),
    re.compile(r"/Applications/[^\s)`]+"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\[^\s)`]+"),
)
for path in formal_docs:
    text = read(path)
    for pattern in raw_path_patterns:
        for match in pattern.finditer(text):
            errors.append(
                f"{rel(path)}: 疑似本机绝对路径 {match.group(0)}"
            )

for path in knowledge_docs:
    text = read(path)
    internal_count = len(re.findall(r"\[\[[^\]]+\]\]", text))
    internal_count += len(
        re.findall(
            r"\[[^\]]+\]\((?!https?:|mailto:|#)[^)]+\.md(?:#[^)]+)?\)",
            text,
        )
    )
    if internal_count == 0:
        warnings.append(
            f"{rel(path)}: 当前没有内部知识链接；若存在真实关联可在后续补充"
        )

print(
    f"Repository audit: {len(formal_docs)} formal docs, "
    f"{len(all_md)} markdown files, {len(errors)} errors, "
    f"{len(warnings)} warnings."
)
for warning in warnings:
    print(f"WARNING: {warning}")
for error in errors:
    print(f"ERROR: {error}")

sys.exit(1 if errors else 0)
