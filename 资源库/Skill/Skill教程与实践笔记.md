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



## 视频制作 Skills 不是数量竞赛：从 55 项清单到可验收生产线（2026-10-09）

来源：[雪踏乌云《我的 55 个 AI视频 Skill 全部开源》](https://x.com/Pluvio9yte/status/2081648099680743554)；[可读正文](https://www.jxxy.net/ai/articles/pluvio9yte-55-ai-video-skills/)；[作者源代码](https://github.com/Pluviobyte/rnskill)。已按文章的十二个功能层逐项理解，并查验作者 README、总许可及多个实际 SKILL.md。

### 数量与权利先校正

- “55”指文章发表时作者自己的工作流数量结构，不等于 55 个由我们独立安装运行验证的单功能工具，也不全是视频专用技能；作者当时将第十二组的 22 个 dbs 商业诊断 Skill 算入。
- 2026-10-09 查看作者上游 README，显示 **61 个顶层 Skill 目录（含兼容别名）**；递归目录可定位 **65 份 SKILL.md**，包含嵌套技能。顶层/递归/历史文章属于不同统计口径，不应比较涨跌来暗示质量变化。
- 其中部分内容来自独立上游，如 video-use、dbskill、乘风口播剪辑，不得统一称为作者原创。总仓库 LICENSE 为 **CC BY-NC 4.0**，个别子目录另有 MIT、AGPL 等单独声明；用途、商业再分发及派生修改要按相应文件核验，不能因公开可克隆就认定“随便商用”。
- 作者自述“月投入不足十小时、三十条成片、涨粉与商单”属于个案，未复现生产费用、设备负担、声音/人物授权、编辑返工和市场效果。

### 12 个功能层与真正要保存的工序

| 层次 | 原文章功能与范围 | 仓库内可复用的输入、输出和验收 |
|---|---|---|
| 1. 选题策划（4） | 选题卡生命周期、实操长片策划、Hook 选型、标题候选 | 输入受众问题/来源→选题卡+证据→人工确定方向；Hook 的选择与质量诊断分工 |
| 2. 内容创作（5） | 视频链接到逐字稿/改写/多重质量门，公众号来源提取 | 先核对素材使用权限、来源与原始事实；出可审查脚本和交接稿。**不能靠隐藏来源、“洗稿”规避版权、署名或事实核查** |
| 3. 下载（2） | 多平台下载、字幕和音频准备 | 使用拥有或获许可的素材；站点下载权、内容复用权与公开发布权分别判断，工具存在不代表可合法去除水印 |
| 4. 配音（1） | 本地 IndexTTS2 与语音清单 | 音频试听、声线授权、参考文件哈希、速度与失败记录；不用未经批准的云端 fallback |
| 5. 数字人（1） | HeyGen 数字人 | 先确认音频与人物授权再付费生成；音频修改会使先前试听确认失效 |
| 6. 视频编辑（3） | 口播粗剪、video-use 通用剪辑、FCPXML 交接 | ASR 词句与源片抽查→人确认删减→EDL/可编辑工程→切点 QC。口播和通用多机位是不同任务 |
| 7. 字幕（2） | 真实音轨转词级时间戳，再应用字幕样式 | 最终音轨→词级 JSON/分句 JSON/SRT→阅读速度、孤立碎片和重叠检测→代表帧试烧录；**禁止按字数估计最终字幕时间** |
| 8. 视觉封面（6） | IP 画风、点阵封面、拼贴动效和 SVG | 固定项目视觉规则与字体→候选封面/图层/可编辑资产→缩略图可读性、文字、版权和实际渲染检查 |
| 9. 图文制作（1） | Markdown 文章分页为图文 | 文章结构→分页和 3:4 图文→人工查缺行、溢出、事实一致、平台规格 |
| 10. 调度与质检（2） | 总导演 + 发布复盘 | 交接稿 Frontmatter 为**唯一执行合同**；状态从待制作→制作中→已制作；交付画幅、音画流、抽帧和文件清单，再做数据复盘 |
| 11. HyperFrames 动效（原标 6） | 动效导演、复刻、SaaS 短片、打字开场、复刻 QC | 将参考只当风格分析依据，形成原创可编辑工程；原文章正文此组只显示 **5 个具体名称**，第六项暂不臆造 |
| 12. dbs 工具箱（原标 22） | 商业/内容问题、Hook、共鸣、诊断、复盘 | 与外部 [dbskill](https://github.com/dontbesilent2025/dbskill) 去重：它是独立上游项目，当前 README 为 34 个当前业务 Skill + 2 个兼容旧入口 + 1 个更新入口；部分旧 Hook 入口已迁移 |

这十二层回答的是 **谁接收材料、谁作判断、谁执行、谁验收、谁存证**，不是让一个 Agent “下载五十多个 Skill”就能自动变现。Skill 可能只含指令，也可能依赖真实脚本、浏览器、模型 API、用户素材和付费额度。仓库找到路径只证明文件存在，不证明运行成功。

### 两条生产线与交接协议

**A. 已有视频素材 → 合规再创作**

1. 接收用户拥有/许可范围内的源片；保存来源、素材权属与禁止改动事实。
2. 转录→对照原画面查错→形成新脚本/评论/分析/原创结构。若仅替换词语、隐藏来源而实质重现原作，不视为得到新的再发布许可。
3. 让人先确认内容与声线，再建生产队列；原素材与字幕保留必要内部追溯，不把敏感素材上传公共仓库。
4. 产生剪辑决策与可编辑工程，音频锁定后生成真实字幕时间戳。
5. 首先预览短段，再整片渲染；验收音画同步、文本事实、授权、版权标识及输出文件。
6. 发布后按内容主题、受众、留存、评论问题和来源证据复盘，不能用单次涨粉替代归因。

**B. 从知识脚本 → 动效或数字人视频**

1. 事实表和观点表拆开；决定动画/讲解/数字人形式。
2. 编写分镜与画面/时间合同；先确认参考视觉风格及素材来源。
3. 生成/录制授权语音；试听确认后锁定最终音频版本，留 `voice_manifest`。
4. 按最终音频生成字幕；不要在配音变更后继续沿用旧字幕。
5. 在代码动效环境中小段试渲染、人工逐镜审查，再批量渲染。
6. 输出 MP4、SRT、素材出处、可编辑工程、测试结果；无需实际运行的项目不宣称出片成功。

可引用作者真实源码：[总导演](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-video-production-director/SKILL.md)、[视频准备调度](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-video-wash-pipeline/SKILL.md)、[音轨转字幕](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-audio-to-subtitles/SKILL.md)。原项目含作者个性化工作台路径、模型、参考人声、账户授权；它们不是跨设备通用默认值。

## 另一个十项清单：先排安全，再按真实任务触发（2026-10-09）

来源：[宋宋《别再装了就忘：十个用得上的 SKILL》](https://imsongsong.com/articles/2084966880616566843)（作者自有网页，2026-08-05；[X 入口](https://x.com/songsong/status/2084966880616566843)）。本文列出的**十个对象并非十份互不相关的 SKILL.md**：前三项是安全扫描器，其中 AgentSeal 本身主要是 CLI 安全工具；Voicebox 是完整的本地语音应用。

### 原文十项的独立判断

| 原文项目 | 实际身份及应用价值 | 主要使用风险或去重结果 |
|---|---|---|
| [SkillSpector](https://github.com/NVIDIA/SkillSpector) | NVIDIA 技能安全扫描器，另提供 `skill-inspector` 真实技能入口；可做静态分析和可选 LLM 辅助分析 | 静态规则可能误报，LLM 模式可能发送被扫描内容；当前 README 是 17 类 71 模式，原文 68 是历史数字 |
| [AgentSeal](https://github.com/getagentseal/agentseal) | Agent/MCP/Skill 配置审查与链路风险工具（CLI），不按单一 Skill 计数 | 本地扫描报告可能包含敏感配置；许可证是 FSL 类限制，不等于 Apache-2.0 自由使用 |
| [Semia](https://github.com/berabuddies/Semia) | 只读检查 Skill 指令可执行能力与来源行，提供不同 Agent 环境下真实 Semia Skill | CLI 合成可能使用已配置 LLM；`repair` 会改文件，须先看差异；作者称“无 Key”只适用于特定宿主方式 |
| [last30days](https://github.com/mvanhorn/last30days-skill) | 带来源健康检查的近期多平台研究 Skill | 本库**已收藏**，不重复；各平台覆盖依赖当前可用后端和授权，Cookie 与社媒账号敏感 |
| [humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | 英文表达风格/结构改稿 Skill，保留证据与原意 | **不同于**本机已有 `humanizer-zh`，不能继承安装状态；避免把作者个性全删除 |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | 前端设计技能合集，真实主技能 `design-taste-frontend` | 本库**已收藏**，重点是落地页和作品集，不默认适配数据仪表盘和后台复杂页面 |
| [dashi-ppt](https://github.com/chuspeeism/dashi-ppt-skill) | 模板约束的 HTML 演示与 PPTX/PDF 交付 Skill | 本库**已收藏**；最新源码技能版本与作者旧 0.4.4 不同，PPTX 导出仍依赖本地服务 |
| [workbuddy-xhs-skills](https://github.com/jackbauerxu/workbuddy-xhs-skills) | 含 **10 个真实 SKILL.md** 的小红书定位、写作、视觉与复盘集合 | 集合中的视觉/内容技术和 dbskill 等有来源关联；不把一次运营案例当涨粉保证；根目录未见 LICENSE，禁止擅定再分发许可 |
| [ecommerce-visual-copywriting](https://github.com/feichanggege/ecommerce-visual-copywriting-skill/blob/main/SKILL.md) | 单个电商视觉方案 Skill，含证据账本→视觉策略→分镜→交接/核查 | 最有价值的是先锁真实商品事实，再做画面；合规规则需随国家、平台和类目复核 |
| [Voicebox](https://github.com/jamiepine/voicebox) | 本地 TTS、语音录入、授权声线和 Agent 接口的**独立应用** | 不列入 Skill 安装计数；本地处理不等于天然免风险，需确认声线与模型许可、储存/共享和实际部署 |

原文的风格测试、产品示例、星标/分叉、软件大小和主观打分是**作者当时的观察**；不能作为仓库现时版本与质量保证。第三方工具“免费、无密钥、低风险”的陈述必须落在具体命令和运行模式上才成立。

### Skill 安装前的防护与“装完即忘”治理

**安全门不是把三个扫描器结果简单投票。**每份报告先检查证据路径、可被触发的权限、潜在数据流，区分已触发行为与静态可疑字符串。合理步骤：

1. 先确定是否有实际工作需要；重复已有能力时先用旧 Skill。没有用户明确授权，不替用户安装、配置常驻监控或修改任何系统安全策略。
2. 按文件/版本锁定来源，先浏览 `SKILL.md`、`scripts/`、依赖、安装脚本和许可证；来源可读不代表发行包等同于源代码。
3. 在隔离环境执行**不运行目标技能**的静态审查。凡可能将本地资料/账号/Prompt 上传云模型、远程扫描或平台遥测的模式，必须先知情确认；涉及私有资料默认本地优先。
4. 审查误报的证据行。示例：`API_KEY` 变量名出现在 README 并不能证明仓库含真实密钥；发现可疑访问凭据时应止步并阻止泄漏。
5. 严格审查安装时/运行时权限：文件、网络、Shell、Cookie、发布和覆盖写入；生产账号保持最小权限，不自动授予浏览器完整会话。
6. 安装/更新后可以检查锁定版本、文件哈希、运行日志和实际触发任务；扫描器通过不等于执行无害。对高风险或无法解释的操作选择不安装。
7. 让已有 Skill 绑定**明确适用触发和不触发案例**。例如“写完一篇长文→按事实保真做一次风格检查”；“要做前端落地页→先产设计风格，再代码实现”，而不是对任何任务静默强制调用几十个工具。
8. 每月只复核一次真正用过/失败的技能：任务、成功或失败证据、是否仍有独立价值、依赖更新和最低运行权限。不用不代表低价值，但不能将“已收藏”写成“已部署”。

以下交接卡可用于视频、研究或电商 Skill 的日常工作：

~~~text
触发任务：
输入与素材/账号授权：
当前实际版本和 Skill 路径：
读取的来源和事实证据：
生成的计划/可编辑产物：
人工确认点：
自动化脚本与真实运行结果：
失败情况与回退策略：
不能自动执行的发布/付费/安装动作：
复核和再次使用条件：
~~~

**重要纠错**：作者提供的“跨智能体三重扫描自动门卫”是一份建议性的 Prompt，它本身不能证明已安装守护进程、跨工具规则生效、后台监控已部署、开机自启有效或扫描器实际运行。应用到 NoIT 时仅保留上述**可执行、有证据、受控权限**的安全流程，不把无法执行的后台承诺固化为已完成工作。

