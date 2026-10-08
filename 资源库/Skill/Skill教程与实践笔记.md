---
title: Skill 教程与实践笔记
date: 2026-10-01
updated: 2026-10-08
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

### 7. 本次核验的外部 Skill 资源

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
- OpenAI《Rethinking skills and prompts for GPT-6 Astra》：https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- 外部资源核验日期：2026-10-03。
