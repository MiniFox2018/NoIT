# 2026-10-09｜扩展 X 资料第一批：三篇长文逐章核验

## 范围

对 [优先队列](2026-10-09-expansion-reconciliation.md) 的第 1—3 篇逐篇检索作者自有公开网页，读取可见正文并对照 NoIT 原主题。X 原入口保留，三篇不是同一主题的合辑；不向公开仓库复制第三方全文。

- Obsidian 原帖：https://x.com/xaiwind/status/2105453277643211214 ；[作者正文](https://shoptofly.com/doc/article/obsidian-start)，11 章。
- GitHub 原帖：https://x.com/xaiwind/status/2104039563719262546 ；[作者正文](https://shoptofly.com/doc/article/github-start)，15 章。
- Codex 原帖：https://x.com/xaiwind/status/2102738292580225350 ；[作者正文](https://shoptofly.com/doc/article/codex-start)，6 章。

**共同证据边界**：作者网页有部分图片和代码/命令只展示占位或未在文字抓取中显示，无法声称已获取其全部图文素材。已结合可得正文和官方资料整理出可直接使用的原创中文知识；没有安装、运行教程示例、代替用户授权或断言原作者推广数据得到验证。

## 1. Obsidian（十一章）

承接：[LLM 维护型个人知识库](../../知识库/知识管理/LLM维护型个人知识库：从RAG到持续演化的Wiki.md) 的第十七节。

| # | 原文主题 | 入库去向 | 结论 |
|---:|---|---|---|
| 1 | 本地 Markdown 与库 | 最小结构／权限边界 | 正文融合；绝对化比较纠偏 |
| 2 | 安装和第一个库 | Vault 初始化 | 正文融合；截图未取得 |
| 3 | 双链、标签、搜索和图谱 | 检索／关联 | 应用规则已融合 |
| 4 | Frontmatter 与术语 | 元数据规范 | 不新增与 NoIT 冲突的字段 |
| 5 | 核心/社区插件与剪藏 | 插件取舍 | 按需安装；未执行 |
| 6 | 目录/入口笔记 | 任务入口 | 沿用 README 导航 |
| 7 | 日记/模板 | 日记到回顾 | 案例框架融合；模板图未取 |
| 8 | AI、三层架构与 Git | 来源层和修改边界 | 融合；公开版权约束 |
| 9 | 五类 AI 日常工作流 | 任务闭环 | 逐项归入已有方法 |
| 10 | 九种常见坑 | 风险与复核 | 保留可迁移检查 |
| 11 | 十二项问答 | 同步/备份/AI边界 | 按可见内容融合 |

已覆盖十一章的可见文字，**融合而不另建 Obsidian 同质教程**。作者个性化的目录、Frontmatter 和“多少万字必须上向量库”不复制为强制规则；原文含图片中的模板/命令尚不能视为逐字取得或实测。

## 2. GitHub（十五章）

承接：[Git与GitHub实践](../../知识库/独立开发/Git与GitHub实践：版本控制、协作、自动化与安全.md)。该文有独立学习顺序价值，形成独立可用的知识版本，而不是仅列出网址。

| # | 原文主题 | 入库去向 | 结论 |
|---:|---|---|---|
| 1 | Git 与 GitHub | 基础区别 | 完整主题吸收 |
| 2 | 账号/安装/2FA | 身份和安全 | 流程吸收 |
| 3 | 仓库/提交/分支/远程/SSH/PAT | 版本与认证 | 官方纠偏 |
| 4 | Star/Watch/Fork/Issue/PR | 评估项目 | 主题吸收 |
| 5 | 搜索与限定词 | 检索 | 实例纳入 |
| 6 | 五步看代码 | 顺功能读码 | 包括静态/运行差别 |
| 7 | 首个 PR | 贡献工作流 | 含复审和验收 |
| 8 | Actions | CI/账单 | 费用动态化 |
| 9 | Pages | 静态发布 | 隐私边界纠偏 |
| 10 | 七类常见错误 | 故障排查 | 凭据泄露优先撤销 |
| 11 | 免费产品 | 云端能力 | 未固化额度 |
| 12 | 主页简历 | 项目展示 | 保留用法 |
| 13 | 团队分支 | 协作流程 | 按规模适用 |
| 14 | 速查表 | Git 命令 | 可参考；未实测 |
| 15 | Git/SVN/GitLab/Gitee | 不同工具关系 | 已吸收 |

已按十五章归档可见正文，重点纠偏：网页登录/桌面端也可提交；Git CLI 与 GitHub 平台不是同一物；不要把 PAT 明文放在远端 URL；Actions runner 计费和套餐不可沿用固定常数；私有仓库部署 Pages 的可用性取决于套餐，但 Pages 站点默认公开。官方对照：

- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- https://docs.github.com/en/billing/concepts/product-billing/github-actions
- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

## 3. Codex（六章）

承接：[工程 Agent 工作流](../../知识库/AI工作方式/工程Agent工作流：从任务边界到可审查交付.md) 的“Codex 入门的落地顺序”。

| # | 原文主题 | 入库去向 | 结论 |
|---:|---|---|---|
| 1 | 概念 | Agent/Skill/MCP | 正文吸收 |
| 2 | 注册/下载 | 访问与账户安全 | 跳过过时套餐与代购做法 |
| 3 | 界面 | 任务入口 | 截图未完整取得 |
| 4 | 个性化设置 | 项目约束 | 个人设置不固化 |
| 5 | 终端命令 | 运行/风险 | 命令截图有缺口 |
| 6 | 答疑 | 职责与权限 | 部分只有问题标题 |

这篇保持 `partially_integrated`：已把可复用的任务范围、权限、目录基线、命令安全与验收流程归入正文，但部分截图、命令表和答疑没有取得可读全文。不将文章中的个人跨区充值、绕开服务可用限制、固定版本 UI/套餐当作通用教程。技术能力以 [Codex 官方文档](https://developers.openai.com/codex/) 为准。

## 本轮状态与后续动作

- 对优先队列 15 篇中的 **3 篇**建立逐章节去向与正文落地：Obsidian、GitHub 记为 `theme_integrated`（仅代表可见知识已主题处理，不代表原图文全面再版），Codex 为 `partially_integrated`。
- 来源台账更新 `knowledge_targets` 和 `knowledge_note`，保留原采集 URL、sha256 与取得时间不变。
- 队列后续 **12 篇**保持原状态。下一批按顺序从“55 个视频 Skill”与“10 个用得上的 Skill”入手，要求实存源码/版本、逐项用途、可用边界，不能把只有名称的资源当已安装。
- 本次自动审计若通过，证明文件与内部链接符合规则；**不能代替对第三方原图及命令示例的完整性证明**。
