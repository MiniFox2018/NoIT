---
title: Skill 收藏与安装清单
date: 2026-10-01
updated: 2026-10-09
tags:
  - Skill
type: resource-index
status: active
---

# Skill 收藏与安装清单

> 本页由用户既有 Skill 收藏与安装清单迁移整理。用途与安装状态以原清单 2026-10-01 的核对结果为基线；后续更新某一 Skill 时，应重新核对来源与当前状态。
>
> 为保证 NoIT 仓库可跨设备使用，原清单中的本机 `file://` 说明路径不写入仓库。存在公开仓库或官方链接时保留公开链接；仅有本机说明路径的已安装 Skill 保留名称、用途和安装状态快照。

## Codex 与技能管理

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 查询 Codex 设置、技能、自动化及 OpenAI API 的官方说明；强调官方来源核对，适合配置解释、产品使用与故障排查。 | `openai-docs` | 已安装 |
| 只读审查指定代码变更，覆盖未提交修改、分支差异或某次提交；优先找实际缺陷，并返回可执行的修复意见。 | `review-agent` | 已安装 |
| 创建或更新 Codex Skill，明确任务范围、触发条件和执行指引，并补充所需资源；适合把重复工作整理成可复用技能。 | `skill-creator` | 已安装 |
| 面向 Claude 的 Agent Skill 创建、修改、触发描述优化和评测，包含测试与验证流程；这是 Anthropic 官方示例版，现有同名 Codex `skill-creator` 安装记录不等于已安装该来源。 | [skill-creator（Anthropic）](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) · [官方项目](https://github.com/anthropics/skills) | 未核实（仅收藏官方版本；同名安装状态不直接继承） |
| 列出可安装技能，或从精选目录、GitHub 仓库路径安装到 Codex 技能目录；支持来自私有仓库的技能。 | `skill-installer` | 已安装 |
| 发现可安装的 Agent Skills：先理解用户需要的能力，再通过开放技能目录 / CLI 搜索候选，并在推荐前检查真实来源与实际 SKILL.md；适合“有没有某类 Skill”“帮我找技能”等任务。 | [find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md) · [仓库](https://github.com/vercel-labs/skills) | 未安装 |
| 约束 AI 编码行为，突出先说明假设、保持实现简单、仅修改必要代码及定义可验证的成功标准；适合写代码、审查和重构。本仓库虽同时提供 CLAUDE.md，但已核实含独立的 karpathy-guidelines 技能。 | [karpathy-guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md) · [仓库](https://github.com/multica-ai/andrej-karpathy-skills) | 未安装 |
| 调整编码助手的输出方式：把下一步行动放在首行，多步骤用编号，跨轮重述当前状态，减少旁支并展示进展；显式调用后在会话中持续生效，直到用户关闭。属于输出与任务呈现规则，不是医疗诊断或治疗工具。 | [i-have-adhd](https://github.com/ayghri/i-have-adhd/blob/main/skills/i-have-adhd/SKILL.md) · [仓库](https://github.com/ayghri/i-have-adhd) | 未安装 |
| 创建和迭代优化 Agent、系统、开发者提示词及可复用模板；先确定任务契约、输出、约束和失败案例，再用评估检查改动，支持 OpenAI、Claude、Gemini 提示词迁移。 | [prompt-optimizer](https://github.com/getsentry/skills/blob/main/skills/prompt-optimizer/SKILL.md) · [仓库](https://github.com/getsentry/skills) | 未安装 |
| 通过 Skills Manager CLI 管理共享技能库，支持安装、更新、移除、按 Agent 部署、预设、标签、搜索及接管已有技能；保留来源与跨工具部署状态，依赖可用的 skills-manager-cli。仓库主体是桌面管理应用，本条记录其独立 manage-skills 技能。 | [manage-skills](https://github.com/xingkongliang/skills-manager/blob/main/skills/manage-skills/SKILL.md) · [仓库](https://github.com/xingkongliang/skills-manager) | 未安装 |

## 图片与公众号

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 使用文稿、用途、平台比例和明确的视觉风格生成中文封面提示词与图片；两项实际技能分别为 punk-cover 与 punk-avatar，共用可复用风格库。**个人非商业用途与客户/变现用途的许可不同，商用前需逐项查看 LICENSE。** | [punk-cover](https://github.com/adrianpunk/Punk-Skill/blob/main/skills/punk-cover/SKILL.md) · [punk-avatar](https://github.com/adrianpunk/Punk-Skill/blob/main/skills/punk-avatar/SKILL.md) · [仓库](https://github.com/adrianpunk/Punk-Skill) | 未安装（2026-10-09 核对实际 SKILL.md 与个人用途许可） |
| 读取中文文章先生成画面方案，把关键概念、结构和隐喻做成白底“小黑”手绘正文配图；含风格 DNA、原创构图要求和人工质量检查，默认不平均给每段配图。 | [ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/main/ian-xiaohei-illustrations/SKILL.md) · [仓库](https://github.com/helloianneo/ian-xiaohei-illustrations) | 未安装（2026-10-09 核对 SKILL.md；未试运行） |
| 按文字描述生成图片，或编辑现有图片、制作参考图变体与透明背景素材；适合照片、插画、纹理和精灵等位图资产。 | `imagegen` | 已安装 |
| 通过已配置的图片 API 和保存的提示词生成图片；支持多种供应商与批量提示词，适合需要指定提供商或控制 API 的任务。 | `baoyu-image-gen` | 已安装 |
| 将 Markdown、纯文本或粗糙笔记转成微信兼容的内联样式 HTML；可选主题并复制到后台，封面生成和草稿推送是可选步骤。 | `xiaohu-wechat-format` | 已安装 |
| 根据文章路径或主题生成公众号封面图；适合已有文章需要配套封面，或先给主题直接出图。 | `xiaohu-wechat-cover` | 已安装 |
| 从文章、脚本、截图、产品笔记、照片或视频制作小红书图文轮播与社交卡片，支持瑞士风和杂志风；可制作公众号 21:9 与 1:1 配套封面，以及基于视频素材的短 Live Photo 动态卡片和拼图。 | [guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill/blob/main/SKILL.md) · [仓库](https://github.com/op7418/guizang-social-card-skill) | 未安装 |
| **封面设计提示词**：按文章内容、风格选择、人物参考图与其他素材生成生图提示词；当前技能固定 3:4 竖版，只输出提示词，不直接生成封面。 | [gbro-cover-design](https://github.com/pyang5166/gbro-cover-design/blob/main/SKILL.md) | 未核实（仅收藏；未执行安装） |
| **小红书图文视觉导演**：先梳理内容目标、受众、页面节奏和统一视觉母版，再规划 3:4 多页图文、图像提示词与发布文案；完整项目需先确认样图。带 docs、templates 和 examples，不应把规划当成已出图。 | [xhs-visual-director](https://github.com/ziguishian/xhs-visual-director-skill/blob/main/skill/SKILL.md) · [仓库](https://github.com/ziguishian/xhs-visual-director-skill) | 未安装（仅收藏，2026-10-09 核验 Skill 文件） |

## 中文写作与表达

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 把研究、提纲、引用、段落写作、Hook 与逐节审稿组织成协作工作流；实际包含 content-research-writer/SKILL.md，适合行业长文和技术文章，不替代对来源的交叉核验。 | [content-research-writer](https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer/SKILL.md) | 未安装（2026-10-09 核对 SKILL.md） |
| **辞达**：中文写作、重写、口述成文、平台适配与文体校准；先检查意义逻辑，再修结构、语气、节奏与措辞，不把工整本身视为问题。 | [cida / 辞达](https://github.com/mizzlelover/cida/blob/main/SKILL.md) | 未核实（仅收藏；未执行安装） |

## 检索与网页内容

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 通过浏览器自动化访问用户自己的 NotebookLM 笔记本、管理资料并进行基于笔记的问答，依赖登录状态与浏览器运行环境；**上游仓库 2026-10-09 已归档**，不把宣传的“减少幻觉”当作性能证明。 | [notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill/blob/master/SKILL.md) · [仓库](https://github.com/PleasePrompto/notebooklm-skill) | 未安装（已归档；2026-10-09 核对仓库与 SKILL.md） |
| 通过 Defuddle CLI 将普通网页提取成干净的 Markdown，去除导航和页面杂项；适合读取文章、博客和在线文档。 | `defuddle` | 已安装 |
| 检索论文、收集研究资料并核对科学信息；按任务选用 Parallel 网页搜索、深度研究或 Perplexity 学术搜索后端。 | `research-lookup` | 已安装 |
| 检索最新且指定版本的框架、SDK 与 API 文档并用于代码生成。Context7 主要是文档检索 MCP 服务，也提供 `context7-cli`、`context7-mcp` 与 `find-docs` 三个实际 Skill；可依使用环境选择 CLI / MCP，文档仍须按版本和来源复核。 | [context7-cli](https://github.com/upstash/context7/blob/master/skills/context7-cli/SKILL.md) · [context7-mcp](https://github.com/upstash/context7/blob/master/skills/context7-mcp/SKILL.md) · [find-docs](https://github.com/upstash/context7/blob/master/skills/find-docs/SKILL.md) · [仓库](https://github.com/upstash/context7) | 未核实（仅收藏；未安装、未运行） |
| 按平台选择 OpenCLI、专用 CLI 或 API 获取互联网内容，覆盖社交平台、招聘、视频和网页等；侧重内容获取与多后端路由，复杂平台先体检可用后端，不负责后续写作或分析加工。 | [agent-reach](https://github.com/Panniantong/Agent-Reach/blob/main/agent_reach/skill/SKILL.md) · [仓库](https://github.com/Panniantong/Agent-Reach) | 已安装 |
| 围绕主题检索最近 30 天的讨论与互动信号，覆盖 Reddit、X、YouTube、TikTok、Hacker News、Polymarket、GitHub 和网页；综合近期用户观点并提供来源健康检查，实际覆盖取决于可用后端与配置。 | [last30days](https://github.com/mvanhorn/last30days-skill/blob/main/skills/last30days/SKILL.md) · [仓库](https://github.com/mvanhorn/last30days-skill) | 未安装 |
| 通过浏览器采集小红书搜索框的联想词，从词根到一级建议词再做第二层扩展，逐次截图并保留排序、来源路径和 JSON 检查点；按行业转化目标评估相对商业意图，交付 Excel、JSON 与截图。评分不代表搜索量或成交额，适合关键词拓展，不用于笔记热度或账号排名分析。 | [yao-geo-xiaohongshu](https://github.com/yaojingang/yao-geo-skills/blob/main/skills/yao-geo-xiaohongshu/SKILL.md) · [技能目录](https://github.com/yaojingang/yao-geo-skills/tree/main/skills/yao-geo-xiaohongshu) | 未安装 |
| 在豆包工作中通过真实浏览器采集抖音公开主页/视频的标题、文案、互动、日期与完整逐字稿；支持飞书多维表或本地 Markdown/JSON，并包含长文本分页完整性、去重、受控标签与写后校验。仅处理有权访问和使用的内容，需遵守平台规则与法律要求。 | [douyin-transcript-exporter](https://github.com/jinchenma94/social-media-data-tools/blob/main/skills/douyin-transcript-exporter/SKILL.md) · [仓库](https://github.com/jinchenma94/social-media-data-tools) | 未安装（2026-10-03 已核验仓库与 SKILL.md） |
| **多阶段互联网研究路由**：将跨平台发现、原文核验、范围限定的归档/转写和证据综合分开；总技能需与 yichen-unified-search、yichen-content-archive、yichen-bookmarks-export、yichen-asr 四个子 Skill 配套，后端另行配置；单阶段搜索直接选子技能。私人书签与下载不能隐式授权，原仓库标注个人非商业使用限制。 | [yichen-web-research](https://github.com/mcncarl/yichen-skills/blob/main/yichen-web-research/SKILL.md) · [说明](https://github.com/mcncarl/yichen-skills/blob/main/yichen-web-research/README.md) | 未安装（仅收藏，2026-10-09 核验） |
| **生活决策检索**：从《高性价比人生指南》正文检索具体章节与条目，对比成本、收益、证据等级及适用例外；不能凭记忆补医学数字、法条或政策，不取代医生、律师或理财专业判断。需要能够访问原书全文。 | [life-decision-guide](https://github.com/eternity4719/HowToLiveBetter/blob/main/skills/life-decision-guide/SKILL.md) · [书库](https://github.com/eternity4719/HowToLiveBetter) | 未安装（仅收藏，2026-10-09 核验） |

## 学术研究流程

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 自适应苏格拉底式学习：每轮一问、12 关键词结构、视觉黑板及按需生成离线 HTML；STE 启发文字输出不等于正式标准认证。 | [qiaomu-learning](https://github.com/joeseesun/qiaomu-learning) · [Skill 仓库与安装说明](https://github.com/joeseesun/qiaomu-learning#安装) | 未安装（2026-10-09 已核对 README） |
| 支持论文规划、大纲、摘要、正文、修改和引用检查等模式；包含风格校准与写作质量检查，可输出双语摘要及 LaTeX、DOCX、PDF。 | `academic-paper` | 已安装 |
| 模拟主编、三名同行审稿人和反方审阅者，从不同角色评估论文；支持快速评估、方法专项审阅、修改后复审与审阅校准。 | `academic-paper-reviewer` | 已安装 |
| 串联研究、写作、完整性检查、审稿和多轮修订，协调相关学术技能；特点是将完整性核验和两阶段审稿纳入完整流程。 | `academic-pipeline` | 已安装 |
| 提供适配 Codex 的学术研究入口，覆盖研究、写作、审阅、实验规划和统计解释；内含角色提示、模板与交接规范，支持 ARS 命令别名。 | `academic-research-suite` | 已安装 |
| 围绕研究问题开展文献检索、来源核验、跨来源综合和偏倚评估；提供完整研究、快速简报、事实核查及系统综述等模式，可按需进行元分析。 | `deep-research` | 已安装 |

## 文献与引用

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 检索 Google Scholar、PubMed 并核验文献元数据；支持 DOI 转 BibTeX 与引用格式整理，适合检查参考文献是否准确。 | `citation-management` | 已安装 |
| 跨 PubMed、arXiv、Semantic Scholar 等数据库进行系统文献检索与证据综合；可形成带核验引用的 Markdown 或 PDF 综述，并支持多种引用格式。 | `literature-review` | 已安装 |
| 查询 OpenAlex 的论文、作者、机构和主题等信息；支持 DOI 查询、开放获取 PDF 下载及引用等文献计量数据汇总。 | `literature-search-openalex` | 已安装 |
| 通过 PubMed、CrossRef、arXiv 等 MCP 工具协调多步骤文献检索；支持 MeSH 检索策略、引用核验及 NBIB、RIS、BibTeX 格式转换。 | `nature-academic-search` | 已安装 |
| 把论文长段落拆成可引用的论述，按时间范围匹配 Nature、Science、Cell 系列指定刊物；输出文本与文献对应关系及可导入文献管理器的引用文件。 | `nature-citation` | 已安装 |
| 检索 PubMed 文献并获取摘要、全文，支持引用匹配和批量缓存；还能关联基因、蛋白质及 PubChem 等数据库的信息。 | `pubmed-database` | 已安装 |
| 通过 Python 客户端和 Zotero Web API 管理文献条目、分类、标签与附件；支持检索、导出引用、上传 PDF 和自动化文献工作流。 | `pyzotero` | 已安装 |

## 科学方法与统计

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 按疾病、药物、地点、阶段和招募状态查询 ClinicalTrials.gov；支持 NCT 编号详情、纳入条件查看及试验数量和申办方项目统计。 | `clinical-trials-database` | 已安装 |
| 在采集数据前规划实验设计、分组、随机化与区组安排；覆盖析因、交叉、重复测量等设计，重点处理混杂和重复单位问题。 | `experimental-design` | 已安装 |
| 评估科学论断的证据强弱，检查实验设计、偏差和混杂因素；可使用 GRADE、Cochrane 偏倚评估等框架，适合理解证据与发现漏洞。 | `scientific-critical-thinking` | 已安装 |
| 根据数据和研究问题选择统计检验，检查方法假设并讨论功效；侧重分析指导和按 APA 格式报告结果。 | `statistical-analysis` | 已安装 |

## 科学写作与审稿

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 把论文做成有来源定位的中英文对照 Markdown 阅读稿；保留图表与相关正文的位置，适合全文翻译解读而非只看摘要。 | `nature-reader` | 已安装 |
| 根据审稿意见、编辑决定或已有回复草稿，撰写、核对和修改逐点回复信；面向 Nature 系列论文修回与大修、小修回应。 | `nature-response` | 已安装 |
| 从审稿人视角评估创新性、重要性与技术可靠性；依照本地 Nature 审稿依据输出三份模拟报告和综合意见，适合投稿前自审。 | `nature-reviewer` | 已安装 |
| 依据作者提供的论点、结果、图表或中文草稿，规划和重组论文论证；可撰写标题、摘要、引言、结果和讨论等 Nature 风格章节。 | `nature-writing` | 已安装 |
| 按检查清单审阅论文或基金申请，评估方法、统计有效性与 CONSORT、STROBE 等报告规范；形成可用于正式评审和修订的建设性意见。 | `peer-review` | 已安装 |
| 先用检索资料搭建章节提纲，再写成连贯段落；遵循 IMRAD 论文结构，处理引用、图表及 CONSORT、STROBE、PRISMA 等报告规范。 | `scientific-writing` | 已安装 |

## 科学绘图与地理

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 提供遥感、GIS、空间分析与地球观测机器学习的方法和代码参考；覆盖卫星影像、矢量与栅格、空间统计、点云和云端地理数据工作流。 | `geomaster` | 已安装 |
| 用 Python 或 R 制作、修改和审阅投稿级科学图表；先明确图的结论与证据逻辑，支持多面板和 SVG、PDF、TIFF 等期刊输出。 | `nature-figure` | 已安装 |
| 协调 matplotlib、seaborn、plotly 制作发表用图；重点处理多面板、显著性标记、误差线、色盲友好配色和期刊格式。 | `scientific-visualization` | 已安装 |
| 按 figures4papers 的出版样式制作 Matplotlib 论文、报告与演示图，覆盖柱状、趋势、散点、热图和多面板；提供配色、字体、图例、排版与 PDF/SVG/高分辨率导出规范，并可对照仓库示例。不是通用交互可视化技能，也不以 3D 或 GIS 为主。 | [scientific-figure-making](https://github.com/ChenLiu-1996/figures4papers/blob/main/scientific-figure-making/SKILL.md) · [仓库](https://github.com/ChenLiu-1996/figures4papers) · [原短链](https://t.co/R47oklr7St) | 未安装 |

## 技术图与可视化

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 将架构、流程、时序、数据流或状态关系做成可浏览的独立 HTML 图；支持明暗主题、多种图像导出及 Mermaid 转换，反映代码时核对仓库证据。 | [archify](https://github.com/tt-a1i/archify) | 已安装 |
| 将技术系统或流程说明绘制为架构图、流程图、时序图、数据流图和概念图；以 SVG 与 PNG 作为导出成果。 | [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | 已安装 |
| 将 JSON 配置渲染成持续运行风格的动态架构图或 Agent 关系面板：固定布局中呈现连线数据流、日志、计数器和状态变化；支持深色终端与浅色图解、MP4 视频或独立网页。包含真实 `SKILL.md`、渲染脚本和逐帧检查；依赖 Python 3.8+、Chrome/Chromium 与 ffmpeg，非实时遥测或可编辑交互图。复用示例设计须保留相应署名；仅核验公开源码说明，未安装、未运行。 | [live-panel](https://github.com/ythx-101/live-panel-skill/blob/main/SKILL.md) · [仓库](https://github.com/ythx-101/live-panel-skill) | 未核实（仅收藏） |
| 提供 Markdown 科学报告和 Mermaid 图表的写作规范；内含多种图表参考与文档模板，适合用可编辑文本表达结构与流程。 | `markdown-mermaid-writing` | 已安装 |
| 直接在对话中制作交互图表、模拟、地图或原型；适合比较方案、探索变量变化以及演示“改变条件会怎样”。 | `visualize:visualize` | 已安装 |
| 按品牌设计规范制作架构、流程、时序、状态、ER、数据流及多种图表，输出含内联 SVG 的独立 HTML，并支持 SVG、PNG 与 drawio、Excalidraw 导入；首次使用先确认项目风格，突出编辑式版面与品牌一致性。 | [diagram-design](https://github.com/cathrynlavery/diagram-design/blob/main/skills/diagram-design/SKILL.md) · [仓库](https://github.com/cathrynlavery/diagram-design) | 未安装 |
| 用最小而清楚的视觉视图解释当前主题，按问题选择伪代码、调用树、组件树、文件树、差异片段或 Mermaid；复杂视觉问题可生成聚焦的 HTML，图与短说明放在一起，适合解释代码结构、流程与改动。 | [show-me](https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md) · [仓库](https://github.com/humanlayer/skills) | 未安装 |

## 网站与界面设计

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 为网页视觉设计提供字体、间距、阴影、卡片和动画等具体规范；重点改善通用模板感，适合需要更精细视觉表达的界面。 | `high-end-visual-design` | 已安装 |
| 设计、审阅和改进网站及应用前端，覆盖信息层级、排版、响应式、无障碍和交互；还处理性能、错误状态、国际化与设计系统。 | [impeccable](https://github.com/pbakaus/impeccable) | 已安装 |
| 审查现有网站或应用的设计，识别通用 AI 设计模式并改进视觉；强调保留原有功能，支持不同 CSS 框架与原生 CSS。 | `redesign-existing-projects` | 已安装 |
| 通过 Sites 创建完整网站，如作品集、仪表盘、门户和内部工具；也用于修改已有的 Sites 网站。 | `sites:sites-building` | 已安装 |
| 将 Sites 构建的网站或修改版本发布到 Sites，并管理托管；适合网站部署和发布，范围不包括 npm 包发布。 | `sites:sites-hosting` | 已安装 |
| 构建或更新由 Site 托管的 MCP 服务器，并帮助用户通过该 Site 的插件在 ChatGPT 或 Codex 中调用其工具。 | `sites:sites-mcp` | 已安装 |
| 诊断和恢复 Sites 构建后的受监督预览失败；专用于 managed-linux 执行环境，便携式预览不属于其适用范围。 | `sites:sites-preview-troubleshooting` | 已安装 |
| 用于新页面设计、现有界面审查与改版，也可从截图或 URL 提取设计特征；强调页面结构差异，而非只给相同模板换颜色。audit 模式只返回问题清单，redesign 模式保留已有实现边界。 | [hallmark](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md) · [仓库](https://github.com/Nutlope/hallmark) | 未安装 |
| 用 HTML 制作高保真原型、幻灯片、动画和可视化，并提供设计评审与 MP4/GIF 导出流程；新设计要求先出三个方向初稿供选择。面向视觉制品，生产级 Web App 或需要后端的系统不适用。 | [huashu-design](https://github.com/alchaincyf/huashu-design/blob/master/SKILL.md) · [仓库](https://github.com/alchaincyf/huashu-design) | 未安装 |
| 为网页、移动端和桌面界面的设计、实现与审查提供可搜索的本地指导库；包含风格、配色、字体组合、UX 规范、图表与技术栈建议，重点覆盖无障碍、交互、响应式布局和设计系统。 | [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md) · [仓库](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 未安装 |
| 根据受众、内容、视觉方向、字体和布局进行差异化网页 / 界面设计，强调避免通用模板感；为 Anthropic 独立 `frontend-design` Skill，不与 Taste 同名混并。 | [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) · [官方仓库](https://github.com/anthropics/skills) | 未核实（仅收藏） |
| 用 React、TypeScript、Tailwind 等创建复杂的 Claude 交互式 Web Artifacts，使用项目脚本打包 HTML；依赖其所设定的运行环境，不等于所有前端项目可直接通用。 | [web-artifacts-builder](https://github.com/anthropics/skills/blob/main/skills/web-artifacts-builder/SKILL.md) · [官方仓库](https://github.com/anthropics/skills) | 未核实（仅收藏） |
| 将 **Anthropic 自身品牌**的色彩、字体与视觉样式应用到文档和其他视觉成品；它是专用品牌规范，而不是任意公司可照用的通用指南。 | [brand-guidelines](https://github.com/anthropics/skills/blob/main/skills/brand-guidelines/SKILL.md) · [官方仓库](https://github.com/anthropics/skills) | 未核实（仅收藏） |
| 利用 Python Playwright 验证本地 Web 应用的交互、截图及浏览器日志，并配合启动测试服务器的脚本；需具备对应浏览器、Python 等运行依赖。 | [webapp-testing](https://github.com/anthropics/skills/blob/main/skills/webapp-testing/SKILL.md) · [官方仓库](https://github.com/anthropics/skills) | 未核实（仅收藏；未运行测试） |
| 为菜单、对话框、卡片、页面切换和加载提示等界面使用可复用 CSS 过渡；项目既是可交互的动效展示 / CLI，也是实际 Agent Skill，含无障碍减少动效的处理。 | [transitions-dev](https://github.com/Jakubantalik/transitions.dev/blob/main/skills/transitions-dev/SKILL.md) · [网站](https://transitions.dev/) · [仓库](https://github.com/Jakubantalik/transitions.dev) | 未核实（仅收藏） |
| 审核已有界面的动效时长、缓动、位移、延迟与设计令牌，专门优化已有过渡；与新增 CSS 模板的 `transitions-dev` 是同仓库不同技能。 | [transitions-polish](https://github.com/Jakubantalik/transitions.dev/blob/main/skills/transitions-polish/SKILL.md) · [仓库](https://github.com/Jakubantalik/transitions.dev) | 未核实（仅收藏） |
| 按 Emil Kowalski 的设计工程方法打磨组件、交互与动画决策；强调默认行为和细节共同形成的体验，审查 UI 代码时以 Before/After 表格呈现建议，适合前端体验精修。 | [emil-design-eng](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md) · [仓库](https://github.com/emilkowalski/skills) | 未安装 |
| 专门审查动画与动效代码，检查动作目的、触发频率、时长、缓动、运动起点、性能及无障碍；输出问题与通过条件。范围是动效审查，不能将其概括为自动改写动画或通用代码审查。 | [review-animations](https://github.com/emilkowalski/skills/blob/main/skills/review-animations/SKILL.md) · [仓库](https://github.com/emilkowalski/skills) | 未安装 |
| 为 React 网页接入会跟随鼠标转头、点击后切换表情的吉祥物；可选已有角色，或用图像工具及参考照片生成新角色，制作两张各含九个方向或表情的精灵图并检查对齐。通过 CSS 背景位置切换画面，无需逐帧 JavaScript 或动画库；这是网页组件技能，与 ChatGPT Work 动画宠物不同。 | [page-mascot](https://github.com/nilbuild/page-mascot/blob/main/skills/page-mascot/SKILL.md) · [仓库](https://github.com/nilbuild/page-mascot) | 未安装 |

## 文档与 PDF

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 创建、读取和修改 Word 文档，处理目录、页码、表格与图片等内容；支持修订、批注、文本替换和多份文档的内容整理。 | `docx` | 已安装 |
| 检查并改写中文里的夸张表达、模糊归因、机械排比和过多连接词等 AI 写作模式；适合让已有文字表达自然、具体。 | [humanizer-zh](https://github.com/op7418/Humanizer-zh) | 已安装 |
| 将 PDF、Word、PPT、表格、网页及多种数据文件转换为 Markdown；还支持图片 OCR、音频转写和 EPUB 等输入形式。 | `markitdown` | 已安装 |
| 通过 officecli CLI 创建、检查和修改 DOCX、XLSX、PPTX；适合 Office 文件内容分析、格式问题检查及图表添加。 | `officecli` | 已安装 |
| 读取、创建和审阅 PDF，兼顾文字提取与页面布局；使用 Poppler 渲染及 Python PDF 工具检查实际页面效果。 | `pdf` | 已安装 |
| 创建、编辑、修订和批注 Word 类文档；要求把文档渲染成页面图片进行视觉检查，适合需要核对排版的正式文档。 | `documents:documents` | 已安装 |
| 读取、创建和验证 PDF，包含可填写的 AcroForm 表单；通过 Poppler 页面渲染与 Python 工具同时检查内容和布局。 | `pdf:pdf` | 已安装 |
| 用于起草、编辑或审阅文章，删除空泛开场、套话和公式化修辞；强调主动语态、具体表述、句长变化及直接传达事实，并从直接性、节奏、真实性等维度评分。源文件的风格约束较强，需结合目标文体使用。 | [stop-slop](https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md) · [仓库](https://github.com/hardikpandya/stop-slop) | 未安装 |

## 演示与 PPT

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 从精选模板库制作英文 HTML 演示文稿；先预览并选择标题页风格，再形成可在浏览器展示的完整演示。 | `beautiful-html-templates` | 已安装 |
| 生成单文件、横向翻页的网页 PPT，包含 WebGL 背景、章节页和图片网格；提供电子杂志与瑞士国际主义两种明确视觉风格。 | [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) | 已安装 |
| 将原始素材整理成以听众理解变化为核心的 AST 演示大纲，逐页决定图片、图表或视频，并给下游渲染技能生成制作说明；成稿后检查每页能否支撑讲述，侧重演讲结构，本身不渲染幻灯片。 | [humanize-ppt](https://github.com/LearnPrompt/humanize-ppt) | 已安装 |
| 生成可编辑 PPTX、重建参考页面、填充模板并美化现有演示；支持复用品牌与版式工作空间，以及演示配音和动画相关任务。 | [ppt-master](https://github.com/hugohe3/ppt-master) | 已安装 |
| 读取、制作和修改 PPTX，包含文字提取、合并拆分、模板、版式、备注与批注；适合围绕 PowerPoint 文件进行内容处理。 | `pptx` | 已安装 |
| 读取、创建或编辑 PowerPoint 和 Google Slides 演示文稿；适合以这两类演示成果为目标的制作与修改任务。 | `presentations:Presentations` | 已安装 |
| 将需求整理成 JSON 计划，使用预置视觉主题生成可离线打开、可在浏览器编辑的横向 HTML 演示，支持导出 PPTX 和 PDF；每个逻辑页提供三个模板方案和一个定制方案，模板方案保留版式结构、主要替换文案。 | [dashi-ppt](https://github.com/chuspeeism/dashi-ppt-skill/blob/main/skills/dashi-ppt/SKILL.md) · [仓库](https://github.com/chuspeeism/dashi-ppt-skill) | 未安装 |

## 电子表格

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 通过 ChatGPT 加载项或已连接会话操作正在打开的 Excel 工作簿；适用于实时 Excel 会话，独立表格文件由其他技能处理。 | `spreadsheets:excel-live-control` | 已安装 |
| 制作、修改和分析 XLSX、XLS、CSV、TSV 或 Google Sheets；覆盖公式、格式、图表、表格与重算，适合文件和在线表格任务。 | `spreadsheets:Spreadsheets` | 已安装 |

## LaTeX

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 编译 TeX 项目，简单项目先尝试内置 Tectonic，必要时使用检测到的 TeX Live 或 MacTeX；适合已有 TeX 工程的编译任务。 | `latex:latex-compile` | 已安装 |
| 检测内置 Tectonic、TeX Live 或 MacTeX 是否可用，报告缺失工具并运行小型编译测试；适合排查 LaTeX 环境问题。 | `latex:latex-doctor` | 已安装 |
| 先检测本机是否已有 TeX Live 或 MacTeX；仅在未发现现有安装时，按需安装由 Codex 管理的完整 TeX Live 环境。 | `latex:texlive-runtime-installer` | 已安装 |

## Obsidian

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 创建和修改 Obsidian 的 Canvas 文件，处理节点、连线、分组及连接关系；适合思维导图、流程图和可视化笔记画布。 | `json-canvas` | 已安装 |
| 创建和修改 Obsidian Base 文件，设置视图、过滤、公式和汇总；适合把笔记组织成可筛选的表格或卡片数据库。 | `obsidian-bases` | 已安装 |
| 通过 Obsidian CLI 读取、搜索和管理笔记、任务及属性；还支持插件与主题调试，包括重载、错误检查、截图和 DOM 查看。 | `obsidian-cli` | 已安装 |
| 编写和编辑 Obsidian 专用 Markdown，正确处理双链、嵌入、callout、属性和标签；适合需要与笔记库结构连接的文档。 | `obsidian-markdown` | 已安装 |

## 飞书

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 读取和编辑飞书云文档及思维笔记，支持创建文档与图片附件操作；可提取内嵌表格、Base、画板的 token，具体数据操作交给对应技能。 | `lark-doc` | 已安装 |
| 查看、创建、上传、编辑和比较飞书 Markdown 文件，支持局部修改；操作对象是 Markdown 文件，导入在线文档和云盘管理另有技能。 | `lark-markdown` | 已安装 |
| 配置 lark-cli 并处理登录、退出、身份和权限问题；可区分用户与机器人身份、检查业务域授权并处理缺失权限提示。 | `lark-shared` | 已安装 |
| 查询和编辑飞书文档里的画板，导出预览图片或原始节点结构；支持用多种格式更新画板内容。 | `lark-whiteboard` | 已安装 |
| 管理飞书知识空间、成员和文档节点层级，支持查找、创建、移动或复制节点；用于知识库组织，文档正文编辑由 lark-doc 处理。 | `lark-wiki` | 已安装 |

## Notion

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 把对话和决策整理为结构化 Notion 页面，如知识库条目、操作指南或 FAQ；强调建立相关页面之间的链接。 | `notion:notion-knowledge-capture` | 已安装 |
| 结合 Notion 里的背景资料与补充研究准备会议议程和预读材料；根据参会人员调整内容与重点。 | `notion:notion-meeting-intelligence` | 已安装 |
| 跨多个 Notion 来源收集资料并综合成简报、对比或报告；保留引用，适合从已有工作空间提炼结论。 | `notion:notion-research-documentation` | 已安装 |
| 将 Notion 需求或 PRD 转成实现计划、任务与进度跟踪；适合把文档中的规格落到可执行工作。 | `notion:notion-spec-to-implementation` | 已安装 |

## 视频制作

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 在 Apple Silicon Mac 上连接另行安装的 Jianying Headless 核心，编译语义剪辑计划，默认交付可编辑剪映草稿；支持适配版本的原生导出；需合法的剪映安装、核心、相关版本匹配与许可。 | [yichen-jianying-edit](https://github.com/mcncarl/yichen-skills/blob/main/yichen-jianying-edit/SKILL.md) · [核心项目](https://github.com/mcncarl/jianying-headless) | 未安装（2026-10-09 核对 SKILL.md；未执行） |
| 作为 video-production 的 Remotion 兼容入口，用于明确指定 Remotion、React 视频组件或旧技能名称的任务；实际制作流程沿用主视频技能。 | `remotion-video-production` | 已安装 |
| 提供 Remotion 与 React 程序化视频开发方法，覆盖动画、时序、字幕、3D、转场和素材处理；支持命令行、Node.js 及云端渲染。 | `remotion-video-toolkit` | 已安装 |
| 规划并执行代码、模板或混合方式的视频制作流程；适合批量短视频、个性化视频、字幕与本地化版本及数据驱动视频。 | `video-production` | 已安装 |
| 下载用户自有或已获授权的抖音原视频，单条可提取并校对 Markdown 逐字稿与 SRT；博主作品可批量归档原片、机器稿、公开指标、标签和封面文字，支持续跑及已有资料库的口播改写。收藏指向 feat/creator-batch-offline 开发分支；批量机器稿未经逐篇听音校对，不能擦除原片已烧录的标识。 | [ah-douyin-clean-downloader](https://github.com/ahang008/ah-douyin-clean-downloader/blob/feat/creator-batch-offline/SKILL.md) · [收藏分支](https://github.com/ahang008/ah-douyin-clean-downloader/tree/feat/creator-batch-offline) · [原短链](https://t.co/BObnXwyvIU) | 未安装 |
| Remotion 官方技能的路由入口，按任务引导到视频创建、React 画面、地图、多媒体处理、Studio 交互与渲染等参考；保留用户已有修改，新视频默认先展示交互预览，不自动等同于导出视频。 | [remotion-best-practices](https://github.com/remotion-dev/skills/blob/main/skills/remotion-best-practices/SKILL.md) · [仓库](https://github.com/remotion-dev/skills) | 未安装 |
| 用 Hypit 编写和执行视频制作工作流，支持从需求、模板或参考视频组织画面、字幕、B-roll、声音和效果，并组合生成素材与用户提供的素材；包含 SVML/SVS/SVRun 编写、运行环境与服务连接指导。以语义和词语锚点组织时间，生成模型可选，宣传播放量不作为效果保证。 | [hypit](https://github.com/hypit-ai/hypit/blob/main/skills/hypit/SKILL.md) · [仓库](https://github.com/hypit-ai/hypit) · [原短链](https://t.co/TK1gBwFYqP) | 未安装 |
| 把 SRT 字幕转换成暖米黄纸张底的白板手绘 MP4；按字幕叙事做分镜、统一线稿与区域标注，再通过连续笔迹先落墨后上色，并保护后续区域不提前露出。预览台可调整顺序与时序，分镜、线稿、标注和渲染等阶段逐步等待确认。 | [srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation/blob/main/SKILL.md) · [仓库](https://github.com/geeklee/srt-whiteboard-animation) | 未安装 |
| **调查长片制作**：从事实链、来源台账、口播稿、素材覆盖表到火山 TTS、Remotion 与多平台发布；需人工审片和素材授权。原 simontalk-investigation 已迁移至 simon-skills。 | [investigation-video](https://github.com/trustfuture/simon-skills/tree/master/skills/investigation-video) | 未核实（仅收藏；未执行安装） |
| **白板视频讲解**：逐笔绘制、贴纸、字幕与封面，适合信息说明；与调查长片工具共用 video-common。 | [whiteboard-video](https://github.com/trustfuture/simon-skills/blob/master/skills/whiteboard-video/SKILL.md) | 未安装（2026-10-09 核对实际 SKILL.md；未执行） |
| **视频共用工序**：提供事实核查、来源台账、版权与发布前验收；本身不负责独立制作完整长片。 | [video-common](https://github.com/trustfuture/simon-skills/tree/master/skills/video-common) | 未核实（仅收藏；未执行安装） |
| **火柴人导演**：先产出 Phase A 导演提案并等待批准，再输出 Phase B 按时长分段的生视频提示词；默认 60 秒 6 段，仍需外部生成服务与后期合成。 | [directing-stickman-videos](https://github.com/kaomei/stickman-video-director/blob/main/skills/directing-stickman-videos/SKILL.md) | 未核实（仅收藏；未执行安装） |
| **实拍素材的 Agent 视频剪辑**：逐词转写与按需画面采样→人工确认策略→生成剪辑决策表（EDL）→FFmpeg 剪辑、字幕和动画→切点校验。需要本地运行环境、FFmpeg、ElevenLabs 等，不是生成式视频模型或免配置一键云服务。 | [video-use](https://github.com/browser-use/video-use/blob/main/SKILL.md) · [仓库](https://github.com/browser-use/video-use) | 未安装（仅收藏，2026-10-09 核验） |
| **Seedance 2.0 中文 Prompt**：依据文字/图片/视频/音频参考、@素材引用、运镜、续片、一镜到底、音乐卡点等生成结构化视频提示词；不直接生成视频。仓库内 2.0 的模型参数不能自动当作 2.5 的最新限制；与 Emily2040 的 Seedance Skill OS 是不同项目。 | [seedance](https://github.com/songguoxs/seedance-prompt-skill/blob/master/.claude/skills/seedance/SKILL.md) · [仓库](https://github.com/songguoxs/seedance-prompt-skill) | 未安装（仅收藏，2026-10-09 核验） |

## 浏览器、插件与模板

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 通过终端控制真实浏览器，执行导航、表单填写、截图、数据提取和界面流程调试；使用 playwright-cli 或配套封装脚本。 | `playwright` | 已安装 |
| 发现和推荐插件，查看应用权限与依赖，并管理连接或移除；适合需要外部服务能力或排查插件接入问题的任务。 | `plugin-management:plugin-management` | 已安装 |
| 从参考文档、演示、表格或其他制品创建可复用的个人模板 Skill，也可更新已有模板技能；适合保存版式与制作规则供后续复用。 | `template-creator:template-creator` | 已安装 |
| 通过 playwright-cli 快照与元素引用控制真实浏览器，支持导航、表单、文件上传、截图及 Playwright 测试工作。与本机已安装的 playwright 技能用途相近，但本条是 Microsoft 仓库中的独立 Skill，不将两者混记为已安装。 | [playwright-cli](https://github.com/microsoft/playwright-cli/blob/main/skills/playwright-cli/SKILL.md) · [仓库](https://github.com/microsoft/playwright-cli) | 未安装 |
| 为当前任务创建或更新 PR，用一句变更原因、少量注意事项和可视化结构大纲帮助审阅者理解实现；可展示调用树、组件或文件结构及差异。仅在明确点名时使用，流程可能涉及提交、推送和发布 PR 描述。 | [visual-pr](https://github.com/humanlayer/skills/blob/main/plugins/visual-pr/skills/visual-pr/SKILL.md) · [仓库](https://github.com/humanlayer/skills) | 未安装 |
| **真实浏览器自动化**：Tencent BrowserSkill 通过 bsk CLI、守护进程及 Chrome/Edge 扩展在独立 Agent Window 中操作已登录网页、表单和网络调试；借用用户标签页需明确授权，页面指令不可信。安装 Skill 不等于已有 CLI/扩展，也不可提取凭据与 Cookie。 | [browser-skill](https://github.com/Tencent/BrowserSkill/blob/main/crates/bsk-cli/skill/SKILL.md) · [仓库](https://github.com/Tencent/BrowserSkill) | 未安装（仅收藏，2026-10-09 核验） |

## 动画宠物

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 根据角色设定、品牌线索或参考图创建 ChatGPT Work 动画宠物；支持制作、修复、验证、预览、上传和启用，涉及九种动画状态与十六个视角。 | `work-pets:create-pet` | 已安装 |
| 查看、选择、下载或删除 ChatGPT Work 中的动画宠物；用于管理已存在的宠物库条目。 | `work-pets:pets` | 已安装 |
| 检查、验证和修复 ChatGPT Work 自定义动画宠物，更新名称、说明或精灵图；适合修改已有宠物。 | `work-pets:update-pet` | 已安装 |

## 游戏与 3D 制作

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 以真实已发行游戏截图建立锁定参考和 Visual Bar，按 Orchestrator → Planner → Builder → Critic → Diagnoser 的分离角色循环制作、审查并持续打磨可玩的致敬型游戏或垂直切片；可玩只是底线，视觉对标通过才结束。要求宿主能提供独立子 Agent / 新鲜上下文，并需要可查看全分辨率图片的 Critic；不用于普通 App 脚手架或只验证玩法的原型。 | [game-builder](https://github.com/ericzakariasson/skills/blob/main/skills/game-builder/SKILL.md) · [仓库](https://github.com/ericzakariasson/skills) | 未安装 |
| 作为 game-builder 的 3D 资产伴随技能，只在锁定参考确实需要 3D 时，为主角、第一人称武器、车辆等镜头关键资产在 Blender 中独立建模、UV、简单绑定并导出 GLB；每个关键资产交给独立 specialist，并在接入游戏前做 turnaround gate。2D、像素风或不需要 3D 的参考应跳过；运行依赖 Blender 和可读取 glTF 2.0 GLB 的引擎/渲染器。 | [game-builder-blender-assets](https://github.com/ericzakariasson/skills/blob/main/skills/game-builder-blender-assets/SKILL.md) · [仓库](https://github.com/ericzakariasson/skills) | 未安装 |

## 软件规格与代码设计

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 把 Vibe Coding 中的口语化需求改写成可直接发给 Agent 的准确表达，并在开发任务里主动提示最相关的 1–3 个 UI、网页、软件、Git、AI 或设计术语；先从上下文推断少量候选，再通过 bundled resolver 向 VibeHub 批量验证名称和链接。保留用户原意，不擅自增加框架、参数或实现方案；需要 Node.js 20+ 与联网，无需账号或 API Key，查询前会去除代码块、密钥、URL、邮箱、本地路径等敏感内容。 | [vibehub](https://github.com/oil-oil/vibe-hub-skill/blob/main/skills/vibehub/SKILL.md) · [仓库](https://github.com/oil-oil/vibe-hub-skill) | 未安装 |
| 将想法、PRD、会议转录或混合笔记压缩成规格核心与配套文件；核心明确原因、能力、约束、非目标和成功信号，供后续 BMad 技能实现，也支持更新与验证已有规格，依赖项目的 BMad 配置。 | [bmad-spec](https://github.com/bmad-code-org/bmad-method/blob/main/skills/bmad-spec/SKILL.md) · [仓库](https://github.com/bmad-code-org/bmad-method) | 未安装 |
| 澄清项目的领域术语、概念边界和关系，用具体边界场景检验模型并核对代码；将确定的术语写入 GLOSSARY.md、设计决策记入 ADR，适合建立或修改领域模型。 | [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md) · [仓库](https://github.com/mattpocock/skills) | 未安装 |
| 用“小接口承载大量行为”的深模块原则设计代码，明确接口、实现、可替换接缝和适配器；重点改善模块封装、可测试性和代码导航，并非只规划文件夹结构。 | [codebase-design](https://github.com/mattpocock/skills/blob/main/skills/engineering/codebase-design/SKILL.md) · [仓库](https://github.com/mattpocock/skills) | 未安装 |
| 通过调用 grilling 对计划、设计或决策进行分轮追问，将相关决策组织成设计树；每轮先讨论已具备前提的决策，给出问题与推荐答案，等待回答后继续，直到明确共同理解。grill-me 本身是短入口，实际流程由 grilling 执行。 | [grill-me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) · [仓库](https://github.com/mattpocock/skills) | 未安装 |
| 组合 grilling 与 domain-modeling，一边用分轮访谈检验计划和设计，一边澄清领域术语并记录 GLOSSARY.md 与 ADR；适合需要把讨论结论落成项目文档的设计澄清任务。 | [grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) · [仓库](https://github.com/mattpocock/skills) | 未安装 |

## Agent 开发

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 在 Claude Code 项目中建立可审阅的 Eval，使用独立未见集逐次改善 Prompt/工具配置与成本；build-eval 与 hillclimb 为同一 claude-api Skill 的子功能，不计作两个独立 Skill。 | [claude-api](https://github.com/anthropics/skills/tree/main/skills/claude-api) · [官方教程](https://claude.dev/blog/automating-eval-design-and-hillclimbing/) | 未安装（仅记录官方来源） |
| Google Agents CLI 的开发流程入口，串联脚手架、构建、评估、部署、发布与观测；默认面向 ADK Agent，提供代码保留与排障规则，并按阶段调用对应技能，需 agents-cli 环境。 | [google-agents-cli-workflow](https://github.com/google/agents-cli/blob/main/skills/google-agents-cli-workflow/SKILL.md) · [仓库](https://github.com/google/agents-cli) | 未安装 |
| 指导设计与实现 MCP Server，涵盖外部服务接口、工具 schema、研究、错误处理与验证；可针对 Python FastMCP 和 TypeScript SDK，属于构建 MCP 的 Skill，本身不是 MCP 服务。 | [mcp-builder](https://github.com/anthropics/skills/blob/main/skills/mcp-builder/SKILL.md) · [官方仓库](https://github.com/anthropics/skills) | 未核实（仅收藏） |
| 为 ADK Agent 编码提供 API 模式与示例，覆盖 Agent 类型、工具、回调、状态管理和图式工作流；按 Python 或 Go 查阅参考，要求先有脚手架项目，部署由其他技能处理。 | [google-agents-cli-adk-code](https://github.com/google/agents-cli/blob/main/skills/google-agents-cli-adk-code/SKILL.md) · [仓库](https://github.com/google/agents-cli) | 未安装 |
| 指导使用 Mastra 构建 Agent、工作流、工具、记忆、工作空间与存储；优先核对已安装包内文档和当前 API，覆盖 TypeScript 项目设置、常见错误、迁移及 mastra api CLI 操作。 | [mastra](https://github.com/mastra-ai/skills/blob/main/skills/mastra/SKILL.md) · [仓库](https://github.com/mastra-ai/skills) | 未安装 |
| 使用 TypeSafe 的 System One API，将自然语言与应用状态转成代码可组合的类型化判断和概率；适合路由、排序、提取与验证。实际技能名为 typesafe-ai，是特定服务的集成指导，并非通用类型安全规范。 | [typesafe-ai](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) · [仓库](https://github.com/typesafe-ai/skills) | 未安装 |

## 后端与数据库

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 指导 Fastify 的 Node.js 后端和 REST API 开发，覆盖路由、插件封装、JSON Schema 校验、钩子、序列化、日志与错误处理；还提供认证、数据库、WebSocket、性能及 inject 测试模式。 | [fastify-best-practices](https://github.com/mcollina/skills/blob/main/skills/fastify/SKILL.md) · [仓库](https://github.com/mcollina/skills) | 未安装 |
| 指导 Neon 上 Postgres 的连接池与直连、迁移、分支、自动扩缩、恢复、只读副本和检索；优先复用已有 DATABASE_URL，适合已有数据库、SQL 与 schema 工作，认证等能力交给相关技能。 | [neon-postgres](https://github.com/neondatabase/agent-skills/blob/main/skills/neon-postgres/SKILL.md) · [仓库](https://github.com/neondatabase/agent-skills) | 未安装 |
| 已弃用的兼容名称，当前仅转交 prisma-orm-setup，本身不含数据库设置方案；实际接入与连接修复由替代技能处理，涵盖 Prisma 6、7、8，并按已有应用版本选择配置。 | [prisma-database-setup](https://github.com/prisma/skills/blob/main/prisma-database-setup/SKILL.md) · [仓库](https://github.com/prisma/skills) · [替代技能](https://github.com/prisma/skills/blob/main/prisma-orm-setup/SKILL.md) | 未安装 |

## 认证与产品邮件

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 为 B2B 和多租户应用接入 Clerk Organizations，覆盖组织切换、成员邀请、角色权限、组织级路由、域名验证和企业 SSO；适合团队工作空间与租户隔离，需先启用组织功能并确定成员模式。 | [clerk-orgs](https://github.com/clerk/skills/blob/main/skills/clerk-orgs/SKILL.md) · [仓库](https://github.com/clerk/skills) | 未安装 |
| 指导产品邮件的送达与使用体验，覆盖 SPF/DKIM/DMARC、订阅与同意记录、退信和投诉处理、webhook、幂等重试及无障碍；帮助区分事务邮件与营销邮件，并提供相关合规检查参考。 | [email-best-practices](https://github.com/resend/resend-skills/blob/main/skills/email-best-practices/SKILL.md) · [仓库](https://github.com/resend/resend-skills) | 未安装 |

## 监控分析与代码安全

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| 用 Semgrep 进行基于代码模式的静态分析，查找漏洞、缺陷或规范违规，并编写自定义 YAML 检测规则；可使用内置规则集和污点分析，有 MCP 时优先通过工具，否则使用 CLI。 | [semgrep](https://github.com/semgrep/skills/blob/main/skills/semgrep/SKILL.md) · [仓库](https://github.com/semgrep/skills) | 未安装 |
| 通过 Sentry MCP 查找并分析生产问题，结合堆栈、breadcrumbs、trace 与代码定位根因并修复；需连接 Sentry 且具有项目访问权限，事件数据只作为证据，修复前核对其与源码是否一致。 | [sentry-fix-issues](https://github.com/getsentry/sentry-agent-skills/blob/main/skills/sentry-fix-issues/SKILL.md) · [仓库](https://github.com/getsentry/sentry-agent-skills) | 未安装 |
| 为新增或修改功能添加 PostHog 行为事件，识别有业务价值的操作、事件属性和用户身份，并保持客户端与服务端事件关联；未接入时指导 SDK 初始化，已有埋点则补充而不重复，适合功能完成或 PR 审查后的追踪检查。 | [instrument-product-analytics](https://github.com/posthog/skills/blob/main/skills/omnibus/instrument-product-analytics/SKILL.md) · [仓库](https://github.com/posthog/skills) | 未安装 |

## 收藏的技能合集

每行是一个含实际 `SKILL.md` 的合集或技能包，不计为单个技能。安装状态按本机技能目录和当前会话清单核对；后续若只安装其中一部分，应拆出已安装的具体技能。

| 用途 | Skill · 点击查看说明 | 安装状态 |
|---|---|---|
| **HTML Anything 既是本地优先的 HTML 编辑/导出应用，也包含多个实际 SKILL.md 模板**，可将 Markdown 与结构化内容转为文章、卡片、演示、简历、信息图、网页及视频；其 README 的数量和 CLI 支持是版本快照，不能将一整个项目误记为单个已安装 Skill。 | [nexu-io/html-anything](https://github.com/nexu-io/html-anything) · [模板目录](https://github.com/nexu-io/html-anything/tree/main/next/src/lib/templates/skills) | 未安装（2026-10-09 核对 README 和多项 SKILL.md 路径） |
| 面向高完成度游戏视觉制作的两技能合集：game-builder 用锁定真实参考、分离 Planner/Builder/Critic/Diagnoser 和多轮视觉硬门槛打磨可玩作品；game-builder-blender-assets 在确需 3D 时把镜头关键模型交给 Blender specialist 制作并以 GLB 接入。两个实际 Skill 已分别登记，收藏合集不代表已安装或已运行验证。 | [ericzakariasson/skills](https://github.com/ericzakariasson/skills) | 未安装 |
| 面向软件开发全过程的技能合集，覆盖需求澄清、规格与计划、增量实现、测试、调试、审查和发布；还包含接口设计、性能、安全及上下文工程。按开发阶段选择技能，强调质量门槛与验证。 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 未安装 |
| 包含六个技能：leader 编写目标任务书，neat-freak 做项目知识收尾，hv-analysis 做历史与竞品双轴研究，khazix-writer 写公众号长文，aihot 获取 AI 资讯，storage-analyzer 分析磁盘空间。 | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) | 未安装 |
| 以小而可组合的工程技能组织需求访谈、规格、任务拆分、实现、TDD、调试、代码审查和交接；可按需选择和修改。目录另含 in-progress 技能，收藏合集不等于所有条目都已成熟。 | [mattpocock/skills](https://github.com/mattpocock/skills) | 未安装 |
| 面向独立开发者和一人公司的业务技能合集，覆盖用户需求研究、SEO/GEO、域名筛选比价、Logo 与横幅生成，以及 Product Hunt、Reddit、X 等信息获取；部分技能依赖专用 CLI、登录或 API。 | [ReScienceLab/opc-skills](https://github.com/ReScienceLab/opc-skills) | 未安装 |
| 以 PUA/PIP 角色话术配合系统化排障和主动执行规则的技能包；针对连续失败、重复尝试或过早放弃，要求改变方法、读取证据并验证结果。提供 Codex 适配；宣传中的效率提升不作为已验证效果。 | [tanweai/pua](https://github.com/tanweai/pua) | 未安装 |
| 包含五个技能：网页设计、可录制的网页视频演示、图片生成、本地知识库检索和文章制作。网页设计侧重设计系统与视觉前端，知识库检索采用分层索引并按文件类型处理资料。 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) | 未安装 |
| 中文增强的编程工作流技能合集，覆盖头脑风暴、计划执行、TDD、系统调试、代码审查、Git worktree 和完成验证；另含中文提交、文档与 Git 流程，以及 MCP 构建和工作流执行技能。 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | 未安装 |
| Superpowers 上游原版：把需求澄清、设计确认、Git worktree、实现计划、TDD、分阶段 Review 与完成分支组织成可自动触发的组合式软件工程工作流；当前 README 明确支持 Codex App / CLI 等多种 Agent 环境。与 superpowers-zh 分开登记，避免把中文增强版误当上游原版。 | [obra/superpowers](https://github.com/obra/superpowers) | 未安装（上游原版） |
| 宝玉维护的内容创作、AI 生成与日常效率技能合集，包含 20+ Skill，覆盖文章配图、社交图文、公众号发布、网页转 Markdown、字幕、AI 生图等；README 明确建议按需安装而非全量导入，以减少上下文负担。现有清单已有 baoyu-image-gen 安装记录，但不能据此认定整个合集已安装。 | [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) · [示例技能](https://github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-image-gen/SKILL.md) | 未核验完整合集（已有相关技能安装记录） |
| 前端视觉设计技能合集，覆盖版式、字体、动效、不同设计风格及参考图生成。主技能实际名为 design-taste-frontend，侧重落地页、作品集和改版，先判断需求与受众、改版前先审查；主技能明确不用于仪表盘、数据表或多步骤产品界面。 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · [主技能说明](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md) | 未安装 |
| 科学研究技能合集，涵盖生物、化学、医学、物理、工程、地球科学、数据分析及科学写作；为专门库、数据库和工作流提供操作指引与验证要求。本机已有 geomaster、literature-review、pyzotero 等对应技能，未安装完整合集；同名 Office 技能不自动视为同一来源。 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 已安装（部分） |
| 独立社区维护的网络安全技能库，覆盖安全监控、事件响应、取证、云与应用安全及授权测试；技能包含步骤、前置条件和相关安全框架映射。虽然名称含 Anthropic，README 明确说明并非 Anthropic 官方项目。 | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 未安装 |
| 产品管理技能与串联工作流合集，覆盖用户发现、需求与假设验证、产品战略、PRD、优先级、发布增长及数据分析；按产品领域分组为插件，单个技能提供模板或分析框架，工作流可组合多个技能。 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 未安装 |
| 学术研究到论文定稿的流程合集，由 deep-research、academic-paper、academic-paper-reviewer 和 academic-pipeline 四个核心技能组成；覆盖检索、写作、完整性核查、模拟审稿和修订，强调研究者阶段确认。本机已安装四个核心技能及可追溯至此仓库的 academic-research-suite Codex 适配版，未核验为上游最新版本。 | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 已安装（Codex适配版） |
| 科研技能合集，覆盖论文阅读、写作与润色、引用核验、科研绘图、统计、实验记录及论文转演示等任务，并提供共享支持包。本机已有 nature-academic-search、nature-citation、nature-figure、nature-reader、nature-response、nature-reviewer、nature-writing 七项对应技能；未安装完整合集，现有版本与当前上游内容有差异。 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 已安装（部分） |
| 面向技术营销人员和创始人的营销技能合集，覆盖转化率优化、文案、SEO 与 AI 搜索优化、广告、数据分析、用户研究、定价、发布及留存增长；以 product-marketing 建立共享的产品、受众与定位背景，各技能据此开展专项任务并相互衔接。 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 未安装 |
| 花叔开源技能的总目录，既索引独立的旗舰与人物视角技能仓库，也包含可直接使用的内置 SKILL.md；覆盖选题、大纲、审校、研究、设计、配图、文档转换等任务，并提供机器可读 skills.json 和更新检查入口。已单独收藏的 huashu-design 保留为独立条目，不视为已安装整个合集。 | [alchaincyf/huashu-skills](https://github.com/alchaincyf/huashu-skills) | 未安装 |
| 面向电影、电视剧和舞台剧的编剧技能合集，覆盖故事前提、结构、人物冲突、对白、场景、剧集开发与不同创作传统；sw-workflow 按项目阶段调度具体技能，把结论与下一步记入 story-bible.md，支持跨会话续写。技能正文以中文维护，输出语言随用户问题调整。 | [jtydhr88/screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) · [流程技能](https://github.com/jtydhr88/screenwriting-skills/blob/main/plugins/screenwriting/skills/sw-workflow/SKILL.md) · [原短链](https://t.co/dkpi73y6o8) | 未安装 |
| 面向 Cursor 工程开发的插件与技能包，包含架构设计、需求追问、TDD、根因排查、验证、技术写作及并行工作等流程；poteto-mode 按任务选择 playbook，setup-pstack 配置角色与模型。已核实位于 Cursor 官方插件仓库，跨工具使用仍需核对 Cursor 规则和运行机制。 | [pstack](https://github.com/cursor/plugins/tree/main/pstack) · [说明](https://github.com/cursor/plugins/blob/main/pstack/README.md) | 未安装 |
| HumanLayer 的开发技能合集，包含 show-me 可视化解释、visual-pr 结构化 PR 描述、CLAUDE.md 指令整理、React 属性类型收窄，以及迭代 Agent 工作流与控制回路设计；每个技能职责独立，实际动作与运行依赖需按具体技能核对。 | [humanlayer/skills](https://github.com/humanlayer/skills) | 未安装 |
| 面向设计师与工程师的界面技能合集，覆盖 UI 细节、动画创建与审查、全代码库动效改进计划、动效术语、原型和原生移动界面；重点帮助选择合适的缓动、时长与交互细节。已单独收藏 emil-design-eng 和 review-animations，本行记录整个合集。 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | 未安装 |
| 内容创作技能工具箱，包含公众号、小红书与视频三组独立技能，覆盖公开内容搜索、账号与热门内容分析、定位选题、标题正文、配图排版及视频脚本、字幕、剪辑和配乐。根技能 creator-buddy 主要调度搜索与分析；成品制作由对应子技能处理，平台访问依赖可用后端，不承诺流量或账号增长。 | [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) · [总控技能](https://github.com/SpaceZephyr/creator-buddy/blob/main/SKILL.md) | 未安装 |
| 手绘风格与图像提示词技能包，以 handdraw-style-prompter 为总入口，结合编号风格、画廊参考、版式与主题色生成中英双语提示词；子技能覆盖文章配图规划、封面、海报、IP、风格融合与自定义素材管理。默认只制作提示词，实际出图需明确请求并具备图像工具，安装需保留根目录参考资产。 | [yang0/handraw-style](https://github.com/yang0/handraw-style) · [总入口](https://github.com/yang0/handraw-style/blob/master/SKILL.md) | 未安装 |
| Anthropic 官方 Agent Skills 示例合集，含开发、设计、企业工作流与文档处理的多个真实 `SKILL.md`；本轮涉及的六个具体技能已归入上方各用途分类。部分文档能力仅开放源码供参考，并非所有文件都采用相同的开放许可。 | [anthropics/skills](https://github.com/anthropics/skills) · [技能目录](https://github.com/anthropics/skills/tree/main/skills) | 未核实（仅收藏；未安装整套） |
| 社交媒体方向的 17 个实际 Skill，覆盖声音风格、LinkedIn 帖子 / 主页优化、短视频脚本、YouTube 缩略图、轮播图、内容矩阵、主题研究与数据回顾；部分流程依赖第三方 API、账号和授权，不保证自动发布或引流效果。 | [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) · [技能目录](https://github.com/charlie947/social-media-skills/tree/main/skills) | 未核实（仅收藏；未安装整套） |
| **Claude Cowork Finance 插件包（非单个 Skill）**：辅助记账分录、对账、损益表、差异分析及 SOX 工作底稿，通常需接入账务 / 表格来源；结果需要财务专业人士复核。原帖“8 个技能”不作为当前核实的定量结论。 | [Finance 官方插件](https://claude.com/plugins/finance) | 未核实（仅收藏；未执行安装） |
| **Claude Cowork Small Business 插件包（非单个 Skill）**：涵盖现金流、工资规划、月底关账、逾期账款、营销与客户跟进；目前官方插件页介绍 43 个可执行工作流（不等于 43 个独立 Skill）；不能将原帖“31 个技能”当作已核验数量，涉及资金或客户操作需审批。 | [Small Business 官方插件](https://claude.com/plugins/small-business) | 未核实（仅收藏；未执行安装） |
| **Claude Cowork Legal 插件包（非单个 Skill）**：合同审阅、NDA 分流、供应商核查、法律简报和模板化回应；须配置团队合同条款与升级规则，结果应由有资格的法律专业人士审核。原帖“9 个技能”未独立核实。 | [Legal 官方插件](https://claude.com/plugins/legal) | 未核实（仅收藏；未执行安装） |
| **调查与白板视频合集**：包含 investigation-video、whiteboard-video、video-common 三个实际 Skill，条目已分别登记；安装时须正确处理彼此依赖。 | [trustfuture/simon-skills](https://github.com/trustfuture/simon-skills) | 未核实（仅收藏；未执行安装） |
| **内容运营多技能包**：含 dbs-xhs-title、dbs-content、dbs-hook 等多个实际 Skill，适合标题、脚本与传播内容诊断；不作为单一技能统计。 | [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | 未核实（仅收藏；未执行安装） |
| **李继刚中文认知与知识表达技能合集**：2026-10-09 核对 master 分支包含 26 个实际 SKILL.md，覆盖概念解剖、机制研究、论文/书籍解读、写作、知识地图、长图卡片、九宫格商业模式与演讲。master 默认 Org-mode、md 分支便于 Markdown；图卡依赖 Bun 和浏览器；按需挑选。 | [lijigang/ljg-skills](https://github.com/lijigang/ljg-skills) | 未安装（仅收藏合集；未运行） |
| **Chubby Skills 内容素材库合集**：仓库现有 14 个实际 SKILL.md，配套 chubby CLI 做视频/播客/文章/本地文档的 Markdown 导入、带出处检索、资料包、订阅发现与可选 MCP。平台支持状态、ASR 依赖、会话凭据及版权限制需逐项核验；采集不等于事实查证。 | [chubbyguan/chubbyskills](https://github.com/chubbyguan/chubbyskills) | 未安装（仅收藏合集；2026-10-09 核验结构） |

## 2026-10-09 新一批 11 个资源归档说明

- 六个具体 Skill：yichen-web-research、video-use、seedance、browser-skill、life-decision-guide、xhs-visual-director；两个合集：ljg-skills、chubbyskills。合集不按单个 Skill 计数。
- CardDown 为 Markdown 排版渲染 CLI；ENGSENCE 为英语播客学习 App；grokbot-field-notes 为 Agent 工程经验资料，均不误列为 Skill。
- 本批仅核对公开源文件、部分配套说明和结构，**没有安装、执行、登录授权或验证实际效果**；其软件工具属性与方法论分别进入既有工具索引和知识主题。

## 2026-10-09 外部清单校核

- 本批来源为用户提供的 [@0xluffy_eth](https://x.com/0xluffy_eth) 整理文字；缺少单条原帖的明确 URL。原帖按“一人公司职能部门”归类，仅是资源组合视角，不能由此认定已有可直接运行的一体化公司系统。
- 原帖将 `Frontend Design` 误指向 Taste 仓库：Taste 沿用已有记录，新增 Anthropic 官方 `frontend-design` 独立记录。Anthropic `skill-creator` 与本库已有 Codex 同名 Skill 不自动判定为同一安装来源。
- 已存在 `obra/superpowers`、`nextlevelbuilder/ui-ux-pro-max-skill`、`Leonxlnx/taste-skill`、`coreyhaines31/marketingskills` 等条目，仅复用而不重复新建。Anthropic 六项 Skill 同源不同文件；Transitions 两项同源不同技能；Context7 既包含 MCP，也包含多个 Skill。
- 本轮核验公开项目、部分 README、实际 Skill 文件和官方插件说明。没有安装、运行、授权或验证效果。动态技能数量以再次核查具体版本为准，不把博主宣传数量当作固定事实。


## 2026-10-09 批量资料关联项目校核

- 已核查 cida、simon-skills、directing-stickman-videos、gbro-cover-design、dbskill 的 GitHub 目录和实际技能入口；未进行安装、授权与效果测试。
- 更名迁移的调查视频项目只保留最新 simon-skills 入口。gbro-cover-design 当前固定 3:4 竖版；火柴人需要人工确认 Phase A 提案后生成 Phase B 提示词。
- 方法和生产经验见 [[AI内容规模化生产：调查长片、火柴人与儿童绘本]] 和 [[中文表达修订与论文科普转述：诊断、证据与叙事]]。

## 播客文字稿提取 Skill 候选（2026-10-09）

- 项目：[podcast-transcript-txt-skill](https://github.com/KingJing1/podcast-transcript-txt-skill)。
- 类型：Agent Skill；用于从播客链接、平台字幕、已有官方文字稿或本地转写流程获取 Transcript。
- 适用：为「严肃听英文播客」提供上游完整稿件；最终中文学习文章仍应人工审阅。
- 状态：**已登记为候选，未安装、未运行，不声称已通过安全审计或实际兼容所有播客平台**。
- 同类入口：Scripod 网页服务、Longhai Podscript（Obsidian 插件）。三者按工作环境择一使用。
- 知识关联：[[AI辅助的系统化学习与输出工作流]]。

来源：龙海《写在严肃阅读之后：我是如何“严肃听播客”》，2026-09-22，https://x.com/longhaiqwe123/article/2102261485837967482 。


## 2026-10-09 中文创作者十技能清单核对

- 原文《Codex 中文创作者 10 个顶级 Skills》（@JackQi82772，2026-06-24，https://x.com/JackQi82772/article/2069599178926522741 ）中的 10 个候选均已处理。stop-slop、guizang-social-card-skill 及 KKKKhazix/khazix-skills 原已收录，本次不重复；dbskill 原已作为多技能包收藏；baoyu-skills 原已作为合集并有部分独立技能安装记录，未扩大为“全套已安装”。
- 新增：content-research-writer、notebooklm-skill、punk-cover、punk-avatar、ian-xiaohei-illustrations；HTML Anything 同时是编辑工具与模板合集，见 [[内容创作、设计与发布工具]]。Punk-Skill 的商用许可约束和 NotebookLM 仓库归档状态不可省略。
- 文中“前十”“首选三个”是作者面向中文创作者的排序意见，不是独立测试结论，也不是默认安装授权。读者需依据自己的产出类型选少量技能形成流程。
