---
title: Skill 教程与实践笔记
date: 2026-10-01
updated: 2026-10-09
tags:
  - Skill
type: resource-index
status: active
---

# Skill 教程与实践笔记

> 本页保存与 Skill 使用、Agent 工作流和相关工程方法有关的资料入口。方法论若后续扩展为可独立学习的主题，应继续融合进知识库，而不是长期只停留在资源索引。

收录 Skill 的使用方法，以及与相关 Agent 工作流设计有关的方法资料。具体技能与安装状态见 [[Skill收藏与安装清单]]。

## Agent 工程方法

### 12-Factor Agents

[原仓库与阅读入口](https://github.com/humanlayer/12-factor-agents)

面向可靠 LLM 应用的工程原则资料。仓库没有实际 `SKILL.md`，因此不列入技能安装清单；它与 Agent 工作流、工具调用和上下文设计有关，作为相关方法资料保留。

其重点是让开发者掌握提示词、上下文、控制流和状态，使用结构化工具调用，并让长任务可以暂停、恢复或请求人工处理。其他原则包括压缩错误信息、构建职责集中的小型 Agent、从多种入口触发工作，以及把 Agent 设计为无状态 reducer。

适合规划需要调用 Skill 或工具的 Agent 系统时，检查执行边界、恢复机制和上下文组织。这里记录的是方法入口及 README 所列原则，不代表已完整实践或验证其效果。

核对日期：2026-10-01。作者推荐排名、身份宣传和动态星标数不作为收录依据。

## 社交媒体公开数据采集：完整性比“抓到结果”更重要

2026-10-03 核验了 `jinchenma94/social-media-data-tools` 中的 `douyin-transcript-exporter` 实际 `SKILL.md`。

这个 Skill 只能在豆包工作环境执行，其真正值得复用的工程经验不是某个平台选择器，而是一套**长内容采集与结构化写入的质量控制流程**。

### 1. 先写输入契约

开始前明确来源主页或视频 URL、采集数量、是否需要完整逐字稿、写入飞书表格还是本地文件。缺少真正必要输入时先补齐，不要默默猜测。

### 2. 动态平台优先使用真实浏览器

Skill 明确要求通过豆包工作内置浏览器读取抖音公开页面，并在需要时由用户完成登录。

长期原则是：

> 有登录态、动态加载和反爬机制的平台，不能默认直接 HTTP 请求与浏览器行为等价。

### 3. 长文本必须分页验证完整性

逐字稿返回时需要比较当前 `end_offset` 与 `total_length`。只要前者仍小于后者，就继续分页读取并拼接。

这是一个可推广到所有长文档 / 长 API 的规则：

> **“返回了文本”不等于“返回了全文”。**

### 4. 禁止占位符冒充成功

如果逐字稿失败，应留空、记录失败原因并走回退路径。不能写“完整内容已获取”之类占位句替代实际数据。

**空值可以被发现和修复，假完成会污染后续知识与分析。**

### 5. 分类使用受控词表

如果目标表格已经有“选题方向”等标签，应从已有选项选择，而不是让模型不断创造近义词。受控词表能够保持筛选稳定、统计可比、长期分类不碎裂。

### 6. 主键去重 + 写后验证

结构化写入后至少检查 URL / ID 是否重复、预期数量和实际数量、关键字段是否为空、长文本是否异常短、是否残留占位符、日期和字段类型是否正确。

### 7. 公开不等于无限制使用

仓库 README 和 Skill 均提醒仅处理有权访问和使用的内容，并遵守平台规则与法律要求。

因此这类 Skill 的长期边界包括：不绕过访问控制；不把公开可见自动理解成可任意再分发或商业使用；批量采集前考虑平台条款、版权、隐私和适用法律。

### 已核验资源

- Skill：[douyin-transcript-exporter](https://github.com/jinchenma94/social-media-data-tools/blob/main/skills/douyin-transcript-exporter/SKILL.md)
- 仓库：[jinchenma94/social-media-data-tools](https://github.com/jinchenma94/social-media-data-tools)
- 核验日期：2026-10-03

具体资源条目见 [[Skill收藏与安装清单]]；豆包工作本身见 [[豆包工作：桌面Agent与飞书协作工作台]]。

## Plugin、Skill 与 MCP：按“流程、工具、分发”分层

2026-10-03 重新核验《ChatGPT 橙皮书》中关于 Plugin、Skill、MCP 的说明，并与 OpenAI 当前开发者文档对照。原教程的核心判断仍然有价值，但当前产品体系已经更明确地把三者拆成不同层。

### 1. Skill 负责“怎么做”

Skill 是一个可复用工作流目录。当前 OpenAI 文档要求核心文件 SKILL.md 至少包含：

- name；
- description，用于告诉模型什么时候考虑这个 Skill；
- 具体工作指令；
- 可选的 references、scripts、templates、assets 等支持文件。

Skill 适合保存“同类任务每次都要按一套方法执行”的流程，例如代码 Review、研究、README 生成、发布检查或固定内容生产。

一次性要求仍应放在当前 prompt；项目硬规则优先放 AGENTS.md，而不是为了“看起来体系化”把所有规则都做成 Skill。

### 2. MCP 负责“连什么实时能力”

MCP Server 提供外部数据、认证、授权和受控动作。Skill 可以围绕 MCP 的工具补充：

- 什么情况下调用；
- 先调用哪个工具；
- 返回不完整时怎么办；
- 如何组合多次调用；
- 最终结果必须包含什么。

因此更精确的判断不是“Skill 和 MCP 二选一”，而是：

> **MCP 提供能力，Skill 组织能力。**

没有外部实时数据或受控动作时，一个 Skill 可以完全不依赖 MCP。

### 3. Plugin 负责“怎么打包和分发”

当前 OpenAI Plugin 架构可以把 Skill、MCP Server、连接应用和其他扩展能力组合成一个可安装、可发布的能力包。

长期理解：

- Skill：工作方法层；
- MCP：数据 / 工具 / 动作层；
- Plugin：组合与分发层。

不要再把“Plugin = 一个单独工具”当作固定定义。

### 4. 选择载体的最小决策表

| 需求 | 更合适的载体 |
| --- | --- |
| 本次临时要求 | Prompt / Thread |
| 仓库长期硬规则 | AGENTS.md |
| 可重复专项流程 | Skill |
| 实时外部数据或动作 | MCP / connected app |
| 一组能力需要安装和共享 | Plugin |
| 定期或条件触发的重复任务 | Automation |

这和 [[工程Agent工作流：从任务边界到可审查交付]] 中的上下文分层保持一致。

### 5. Skill 不应越写越厚

OpenAI 在 2026-09 针对 GPT-6 Astra 的实践更新中明确建议重新审视过去积累的 Skill、AGENTS.md 和任务提示词。模型变强后，一些旧式“手把手脚手架”会变成上下文噪声。

维护 Skill 时优先：

- description 只负责准确触发；
- 主文件保存必要步骤和决策点；
- 大块参考资料拆到 references；
- 确实需要确定性处理时再放 scripts；
- 不重复项目本身已经清楚表达的信息；
- 模型和工具升级后重新验证旧规则；
- 删除失效约束，而不是无限追加“补丁”。

### 6. Skill 要同时测试“该触发”和“不该触发”

当前官方构建指南建议至少测试：

1. 明确点名 Skill 的请求；
2. 没点名但意图相同的请求；
3. 输入不完整、应先补信息的请求；
4. 不应该触发该 Skill 的请求；
5. 容易产生幻觉、越权或异常动作的边界情况。

触发错误通常先改 description；已经触发但流程不稳定，再改正文指令。

### 7. OpenAI Docs MCP：变化信息不要写死

OpenAI 当前提供只读开发者文档 MCP：

https://developers.openai.com/mcp

Codex CLI 当前可用：

~~~bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
~~~

处理 OpenAI API、Codex、Plugin 等快速变化主题时，优先从 Docs MCP / 官方文档获取当前信息，再把真正长期稳定的结论沉淀进知识库。

### 8. 本次核验的外部 Skill 资源

《ChatGPT 橙皮书》推荐的一组 Skill / 技能包已分别核对：

- obra/superpowers：实际包含多项软件开发 Skill，并形成从需求澄清、设计、计划、TDD、Review 到完成分支的完整工程方法；作为上游原版合集登记。
- JimLiu/baoyu-skills：实际包含 20+ 内容创作、生成与效率 Skill；README 明确建议按需安装，避免全量安装造成额外上下文负担。
- Panniantong/Agent-Reach：实际存在 agent_reach/skill/SKILL.md，定位为多平台互联网能力路由与工具选择层；现有清单中的 agent-reach 条目补充上游来源。
- vercel-labs/skills/find-skills：实际存在独立 SKILL.md，用于发现和安装开放 Agent Skills；其推荐逻辑只是辅助筛选，最终仍应核查实际 SKILL.md、来源和适用边界。

具体收藏与安装状态见 [[Skill收藏与安装清单]]。

### 来源与核验

- 《ChatGPT 橙皮书》，v0.2.0，原资料最后校验 2026-07-13。
- OpenAI Skills：https://developers.openai.com/plugins/concepts/skills
- OpenAI Plugin architecture：https://developers.openai.com/plugins/concepts/plugins
- OpenAI Build skills：https://developers.openai.com/plugins/build/skills
- OpenAI Docs MCP：https://developers.openai.com/learn/docs-mcp
- OpenAI《Rethinking skills and prompts for GPT-6 Astra》：https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- 外部资源核验日期：2026-10-03。


## 2026-10-09 视频和中文表达 Skill 的处理方法

- 文章提到 Skill 时先查看实际 SKILL.md、README、依赖和边界，不凭“开源”“一键”判断能力。
- cida 作为中文表达 Skill 收录；其 P0—P4 方法已另行融入 [[中文表达修订与论文科普转述：诊断、证据与叙事]]。
- 调查长片、白板与共享工序分别登记；火柴人导演需要“先提案→人工确认→生成片段提示词”；相关事实链和时间预算方法已融入 [[AI内容规模化生产：调查长片、火柴人与儿童绘本]]。
- gbro-cover-design 当前只生成 3:4 竖版提示词，dbskill 是多技能合集。安装状态仅表示本库收藏，不代表本机可用。
- 使用前应审查项目代码、外部 API、凭据权限、素材授权和端到端测试。用户未要求安装时不自动运行。

具体入口与状态见 [[Skill收藏与安装清单]]。

## 2026-10-09：从重复工作流制作可验证的 Codex Skill

来源文章不是一个可安装的 Skill，而是**如何制作 Skill**的教程，因此并入本页，不录入「已安装技能」栏。

### 选择：不是所有 Prompt 都需要升级

同一任务如果经常重复、有稳定输入输出、必须遵循固定流程/规则、换一个 Agent 仍需重新解释，才值得固化为 Skill。一次性问题或没边界的「全能助手」先不做。以「每周复盘」这种窄任务为例，可以明确启动条件、输入、步骤、异常与完成标准。

### 实施八步

1. 写工作流卡片：名称、触发场景、用户输入、处理步骤、最终输出、验收标准、异常处理。
2. 准备三类真实触发语：明确点名、自然语言请求、信息不足的边界案例；补一个**不应该触发**的负例。
3. 从最小结构开始：**SKILL.md 必需**；长背景放 references/；稳定脚本放 scripts/；真实交付模板放 assets/；需要时再增加 agents/openai.yaml，不建立空目录。
4. 用 skill-creator 或手动初始化：名称小写字母/数字/连字符，文件夹与 name 对应；检查当前官方规范。
5. YAML 描述回答「做什么、什么时候用」；正文写工作步骤、输入约束、错误处理、输出格式、验收标准。不要往正文堆全部聊天历史。
6. 运行结构校验：命名、frontmatter 和必要文件；**格式通过不等于任务成功**。
7. 用真实资料测试点名、自动触发、缺信息、错误输入和不应触发的情况；记录误触发、漏触发、数据虚构与输出偏差，迭代后回归测试。
8. 上传 GitHub 前检查：无密钥、账号、私人路径、客户材料或未授权模板；README 说清安装、输入、依赖、限制、测试记录和版本；公开仓库不暗示已审计。

### 一张可复制的工作流卡

~~~text
工作流名称：
什么时候启用：
输入与信息来源：
必须执行的步骤：
1.
2.
3.
输出文件/字段：
合格标准与测试样本：
缺失输入时怎么办：
禁止访问、写入、发布的范围：
不应该触发的情景：
~~~

优先以「能稳定做一件事」而不是「覆盖几十类任务」作为好 Skill 的标准。作者示例中的本机安装目录和配置是历史经验；部署时以本机工具当前约定及官方文档核对。

来源：Adrian Punk，《如何把一套工作流沉淀成自己的 Codex Skill：从 0 到上传 GitHub》，2026-07-30；用户 Markdown 于 2026-10-09 阅读，逐步法、工作流卡、触发案例、目录分层、验证安装和 GitHub 安全检查已归入本节。https://x.com/AdrianPunk115/article/2082706843466633354

## 2026-10-09：中文内容 Skills 从选题到发布的组合方式

《Codex 中文创作者 10 个顶级 Skills》的独立价值不是“十个越多越好”，而是把内容生产拆成**可检验的五个关口**：

| 关口 | 可考虑的 Skill | 必须由人判断的内容 |
| --- | --- | --- |
| 题目和 Hook | dbskill（多技能包） | 是否有真实受众、问题和独特证据 |
| 研究与写作 | content-research-writer、notebooklm-skill、khazix-skills（技能合集） | 来源是否可信、当前、适用，引用是否准确 |
| 表达修订 | stop-slop 或现有辞达 | 改掉套话但不扭曲中文语气、事实和作者风格 |
| 封面与卡片 | Punk-Skill 中的 punk-cover、guizang-social-card-skill、ian-xiaohei-illustrations | 图片版权、中文文字、人物真实性、展示效果 |
| 信息图与发布形态 | baoyu-skills（合集）、HTML Anything（编辑工具＋模板合集） | 信息结构是否准确、平台规格是否匹配 |

每个关口都应有明确输入、可审查输出和失败回退。研究阶段没有真实证据时不能靠“去 AI 味”润色掩盖事实空白；图像步骤不能擅自改变引用和定量结论；平台发布内容须按平台形态改写，而非把同一稿件机械复制到 X、公众号和小红书。

**资源与安装注意：**

- **dbskill、khazix-skills、baoyu-skills、Punk-Skill、HTML Anything** 含多个实际技能或工作流，不能按单个技能重复计数；HTML Anything 首先是一套本地编辑与导出工具，也附带多个 SKILL.md 模板。
- **NotebookLM Skill** 原仓库于 2026-10-09 处于 archived 状态；它使用浏览器自动化查询个人 NotebookLM，必须确认账户授权、依赖以及后续兼容性。其“更少幻觉”是设计目标，不是无错误保证。
- **Punk-Skill** 核查了 punk-cover、punk-avatar 与个人使用许可；当前仓库 PERSONAL 许可明确排除商业营销、客户工作、变现账号等。用在商业内容前需另行核对商业授权，不能以开源可读推导自由商用。
- **ian-xiaohei-illustrations** 先给正文配图策略，再按用户确实要生成时出图；不是所有段落都适合平均分配一张图。
- 源文所给的 npx skills add 命令属于工具安装方式示例，本次资料吸收**没有安装任何技能**，也未验证本机执行环境。

最小工作流建议只先选一条完整链路——例如“问题和证据 → 研究/写作 → 人工核查 → 修订 → 封面 → 发布 → 数据复盘”。依赖、模型、图像/声音额度与服务条款发生变化时，逐项复核项目上游而不是沿用文章中的排名。

来源：SakuAI（@JackQi82772），《Codex 中文创作者 10 个顶级 Skills》，2026-06-24，https://x.com/JackQi82772/article/2069599178926522741 。本轮核对了五个先前未收录或未明确登记项目的公开目录/实际 SKILL.md，已归并到 [[Skill收藏与安装清单]]；原有技能不重复登记。
 
## X 收藏补充：视频 Skills 来源核对（2026-10-09 第二轮）

来源：[8 个视频 Skills 清单，@lxfater](https://x.com/lxfater/status/2102235224952410287)。**已核实各个候选仓库中对应的 Skill 文件，不等于已经证明它们就是原作者当时指向的全部八个具体来源，更不代表实际运行或安装成功**。

| 原清单名称 | 可核实的实际文件 / 归类 | 处理边界 |
|---|---|---|
| `video-use` | [video-use/SKILL.md](https://github.com/browser-use/video-use/blob/main/SKILL.md) | 已在原 Skill 收藏中，不重复计数 |
| `HyperFrames` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 主要是代码视频框架及内置技能体系，已作为工具归档，不按一个泛称 Skill 计数 |
| `talking-head-editor` | [Speclip 实际 SKILL.md](https://github.com/linyqh/speclip-skills/blob/main/talking-head-editor/SKILL.md) | 口播字幕/逐句稿驱动的精剪方案；与完整自动剪辑不是同一承诺 |
| `caption-clip` | [awesome-omni-skill 实际 SKILL.md](https://github.com/diegosouzapw/awesome-omni-skill/blob/main/skills/tools/caption-clip/SKILL.md) | 依赖 yt-dlp、FFmpeg、Deepgram；需素材使用权限、环境和 API Key，未运行 |
| `claude-shorts` | [AgriciDaniel/claude-shorts/SKILL.md](https://github.com/AgriciDaniel/claude-shorts/blob/main/SKILL.md) | 仓库名 claude-shorts，Skill `name: shorts`，不能按两个技能计数 |
| `video-wrapper` | [Video-Wrapper-Skills/SKILL.md](https://github.com/op7418/Video-Wrapper-Skills/blob/main/SKILL.md) | 视频字幕解析与综艺式视觉包装，执行前需要用户审稿 |
| `product-launch-video` | [EveryInc 的 Skill](https://github.com/EveryInc/product-launch-video/blob/main/.claude/skills/product-launch-video/SKILL.md)；[HyperFrames 的同名 Skill](https://github.com/heygen-com/hyperframes/blob/main/skills/product-launch-video/SKILL.md) | **存在同名不同实现**，不能仅凭技能名称确定原帖归属或合并为同一个项目 |
| `Claude Video` | [bradautomates/claude-video](https://github.com/bradautomates/claude-video) 项目内的 [watch/SKILL.md](https://github.com/bradautomates/claude-video/blob/main/skills/watch/SKILL.md) | claude-video 是项目名；`watch` 是实际 Skill 名称。不能证明原帖特指此项目 |

共核对八个**名称/类别线索**；在项目结构中能定位对应实现，原作者的指向关系、运行可用性、许可证和商业使用条件仍须分别判断。主清单只登记确实找到的 `SKILL.md` 和其最新未安装状态。不要把这八个名称写成“八个均已安装”或“八条经过实操验证的生产线”。

来源与可迁移的工程原则仍见 [[代码生成视频：确定性逐帧渲染、音画统一时间线与Agent工作流]]，以及 [2026-10-09 X 收藏覆盖记录](../../.github/audits/2026-10-09-x-67.md)。

