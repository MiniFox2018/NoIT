# 2026-10-13｜NoIT 质量门禁与资料治理优化记录

> 基准：`main` @ `3fbcc16982cab89acfdc64db6b05a0e45691004c`。本记录为本轮实施台账，不代表原始资料已全部阅读、外链均可访问或文档全文核验通过。

## 已实施并纳入仓库

1. **核验日期回归修复**：修复 `audit_repository.py` 的错误正则转义，补充 `核验日期：YYYY-MM-DD` 的正反向测试；不批量生成 `verified`。
2. **书签双表防回归**：新增 `audit_bookmarks.py` 与单元测试，覆盖文件数量、Netscape HTML、URL 合法性、保守归一化去重、两表交叉重复、七类两层业务目录以及常用书签说明字段。两表完整保留原网址及用户挑选状态。
3. **书签描述完善**：将其他待选书签原 187 条缺失的 `<DD>` 补上简短说明，其中 116 条机器人资料依据仓库现有六个月学习资源索引按月份与模块标注。其余按照已存名称与链接类型作保守说明；没有冒充逐站访问、实测功能或价格核验。
4. **外链覆盖扩展**：定期 `audit_external_links.py` 在 Markdown 之外也扫描两个书签 HTML，输出统一链接来源；404/410 仍只是疑似失效，扫描报告不回写正式资源。
5. **采集凭据审计**：新增 `audit_source_receipts.py` 对 ID、URL、SHA-256、采集日期、已登记知识路径进行结构核查，可直接输出只读待审清单；不自动改变 `knowledge_status`。
6. **知识文档维护**：旅行照片主题将后加的 12 种编辑与静态艺术内容移到来源章节前，文末统一来源记录；保留原方法与来源链接。
7. **跨 AI 工作规则**：更新 README、PROJECT_RULES 与 AGENTS 的自动检查入口；增加最小 `.gitignore` 防止本机缓存和私密配置误提交。

## 仍待逐篇内容验收（未宣称完成）

原始 311 条来源当前状态：`theme_integrated` 74、`partially_integrated` 6、`resource_indexed` 1、`source_linked` 132、`source_registered` 98。**98 条仅登记含 97 条扩展来源与 1 条原合集线索**。上述数字仅是来源处理进度，不是全文覆盖率或事实核实率。

- **队列 A：97 条扩展仅登记**。逐篇先比较已有知识主题，决定增补、去重、资源保留、降级或待补；不能凭标题编造内容。优先阅读可实际复用的长篇、涉及合规的高风险文章：
  - [微信小程序虚拟支付](https://x.com/songsong/status/2099460884582305906)：官方平台支付政策/适用主体优先；对照「小程序商业化」现有章节。
  - [X 起号实录与反思](https://x.com/i/status/2104548529972658559)：对照「X 平台账号运营」，把作者实测、平台推断和可迁移方法分开。
  - [Reddit 账号受限后获客 SOP](https://x.com/i/status/2099164807748575422) 与 [CQS 恢复经验](https://x.com/i/status/2100083029662367901)：区分官方规则与作者经验。
  - [Codex + 达芬奇编辑方法](https://x.com/Sabrina_Ramonov/status/2100615977599955328)：核对可复现命令、依赖版本与现有 AI 视频流程。
  - [闲鱼 AI + 飞书实操](https://x.com/i/status/2087059333406490683)：对照创业运营，收益数字仅作原作者叙述。
  - [Obsidian 任务插件线索](https://x.com/Sunkeke_AI/status/2103759910416809999)：核对真实项目与 Skill/知识管理分流。
- **队列 B：132 条 `source_linked`**。已有关联并不等于完成原文吸收；对照 `knowledge_targets` 检查步骤、关键例外、场景和失败条件后再决定状态。
- **队列 C：6 条 `partially_integrated`**。维持尚缺的图片/原文/命令/项目全量技能测试的准确记录；没有取得材料之前不提升状态。
- **动态事实**：税务、83(b)/BOI、小程序支付备案、AI 平台版本能力和商业许可按官方资料动态复核；局部核验不能填整篇 `verified`。
- **分支治理**：旧分支有保存历史变更的价值，本轮未删除。主分支保护和旧分支合并状态留待有依据时处理。

## 可重复的本地验收命令

```bash
python scripts/audit_repository.py
python scripts/audit_bookmarks.py
python scripts/audit_source_receipts.py
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/audit_source_receipts.py --queue registered --limit 20
python scripts/audit_source_receipts.py --queue linked --limit 20
```

待审清单动态取自 [311 条原始来源凭据](2026-10-09-source-receipts.json)，不另存一份易过期的 97/132 名单。外链扫描不能证明永久失效，也不将来源采集等同于第三方原文转载授权。
