---
title: BRAIN.md：项目级持久化记忆层
aliases:
  - projectbrain.md
  - brain.md
  - Project Brain
tags:
  - AI工具
  - Agent
  - 项目记忆
  - Markdown
  - Git
type: resource
status: active
updated: 2026-10-03
---

# BRAIN.md：项目级持久化记忆层

## 资源定位

BRAIN.md 是 MindMux 团队维护的一套**项目级持久化记忆规范与 CLI 工具**。

它解决的问题非常具体：

> AI Agent 可以读取代码和当前文档，但“为什么当初做这个决定”“哪些方案已经被否决”“当前有哪些长期约束”经常只存在于旧聊天或人的脑中。

BRAIN.md 把这类“决策级上下文”保存成仓库中的普通 Markdown，使新的 Agent、机器或会话都能重新读取。

官方把它定位为：

- repo-native；
- agent-agnostic；
- Git-native；
- plain Markdown；
- 不依赖长期运行服务；
- 通过 CLI 约束写入格式。

官方网站：
https://projectbrain.md/

官方仓库：
https://github.com/mindmuxai/brain.md

许可证：Apache-2.0。

---

## 一、它和 README、AGENTS.md 分别解决什么

BRAIN.md 最值得借鉴的是把三种文档职责拆开。

| 文件 | 面向对象 | 核心职责 |
| --- | --- | --- |
| README.md | 人 | 项目是什么、怎么使用 |
| AGENTS.md | AI Agent | Agent 应该怎样工作、遵守什么规则 |
| BRAIN.md + brain/ | 人与 Agent | 项目当前“为什么这样做”、已确认决策、约束和历史依据 |

例如：

README 可以告诉你：

> 这个项目使用 SQLite。

AGENTS.md 可以告诉 Agent：

> 修改数据库相关代码前必须先跑测试。

Brain 则应该记录：

> 为什么选择 SQLite 而不是 PostgreSQL；当时有哪些约束；哪些方案已经讨论并否决；什么条件变化后可能重新评估。

这三种信息不要混在一起。

---

## 二、BRAIN.md本身不是“把所有聊天存下来”

官方强调它保存的是 **decision-grade knowledge**。

也就是：

- 已经形成明确结论；
- 会影响后续任务；
- 六个月后仍可能重要；
- 无法轻易从代码本身重新推导。

不应该进入 Brain 的内容包括：

- 临时闲聊；
- 可直接从代码读出的实现细节；
- 每一次尝试过程；
- 没有沉淀价值的中间输出；
- 完整原始聊天记录。

这是一个重要原则：

> 持久化记忆的价值来自筛选，不来自“什么都记”。

---

## 三、核心结构

初始化后，项目会拥有一个 `BRAIN.md` 入口和一个 `brain/` 目录。

官方当前固定提供六个项目级视图：

- background：项目为什么存在；
- architecture：整体架构；
- flow：关键端到端流程；
- mindmap：功能或概念关系；
- stack：技术选型；
- roadmap：里程碑和顺序。

此外，`brain/pages/*.md` 保存更细粒度的知识单元。

页面类别包括：

- decision；
- concept；
- project；
- person；
- reference。

这种结构明显偏向**软件项目与项目决策记忆**，而不是通用个人知识库。

---

## 四、compiled_truth + timeline 是最值得借鉴的设计

每个细粒度页面分为两个逻辑部分。

### compiled_truth

保存“当前最可信、应该被后续 Agent 直接使用的结论”。

当理解变化时，可以重写。

### timeline

保存形成这个结论的证据链和变化历史。

条目可以是：

- decision；
- evidence；
- reversal；
- note。

例如：

```text
当前结论：
使用 PostgreSQL

历史：
2026-04：最初考虑 SQLite
2026-05：发现并发写入需求增加
2026-06：决定改用 PostgreSQL
```

新的 Agent 默认先读“当前结论”，只有需要审计时才进入时间线。

这样同时解决了两个问题：

1. 不让 Agent 每次都重读全部历史；
2. 不因为更新“当前答案”而彻底丢掉旧决策依据。

---

## 五、为什么所有写入走CLI

BRAIN.md 不鼓励 Agent 随意手工修改 `brain/`。

官方提供一个零运行时依赖的 Node CLI，让结构化写入通过固定命令完成。

核心思想是 **correct by construction**：

- Frontmatter 由工具生成；
- 修改 current truth 时必须同时留下 timeline；
- 链接可以统一检查；
- 不允许某个 Agent 随手写出不符合规范的页面。

这和普通 Markdown Wiki 的差异在于：

> Markdown 是数据格式，但 CLI 充当“数据库约束层”。

对于多人或多 Agent 长期维护的项目，这能降低结构漂移。

---

## 六、跨Agent工作方式

截至 2026-10-03，官方说明其 Skills 可以与多种 Agent 环境配合，包括：

- Claude Code；
- Codex；
- Cursor；
- Pi；
- OpenCode。

任何能够读取文件的 Agent，即使没有专用 Skill，理论上也可以通过根目录 `BRAIN.md` 理解协议。

这也是它的主要设计价值：

> 项目记忆不属于某个模型账户，而属于项目仓库。

换模型、换客户端、换机器时，长期上下文仍然存在。

---

## 七、Git为什么很适合做这一层

Brain 本身就是 Markdown 文件，因此 Git 天然提供：

- diff；
- commit；
- blame；
- revert；
- branch；
- 历史审计。

timeline 负责提供“人能快速读懂的决策历史”，Git 则保存完整文件级变化。

两者作用不同：

- Timeline：语义历史；
- Git：文件历史。

---

## 八、什么时候适合用

更适合：

### 长周期软件项目

存在很多“为什么这样设计”的决策。

### 多Agent协作

Claude Code、Codex、Cursor 等交替处理同一仓库。

### 经常跨会话继续工作

不希望每次重新解释项目背景。

### 决策经常变化

不仅要知道当前结论，还想保留曾经为什么反转。

### 规则和上下文比代码更难恢复

代码可以重新读，但项目意图和决策背景很难从代码完全重建。

---

## 九、不适合把它当成什么

### 不是聊天记录数据库

它不是为了保存每次对话。

### 不是向量数据库

核心不是语义搜索，而是维护经过筛选的项目事实。

### 不是RAG服务器

不需要 MCP 或长期服务才能存在。

### 不是README替代品

README 服务人类快速理解；Brain 服务长期项目判断。

### 不是AGENTS.md替代品

AGENTS.md 是规则，Brain 是项目事实和决策。

---

## 十、与NoIT的关系

BRAIN.md 与 NoIT 有很强的设计共鸣，但解决的问题不同。

### BRAIN.md

主要回答：

> **这个项目为什么变成现在这样？**

强调：

- 项目决策；
- 约束；
- trade-off；
- 当前事实；
- 决策时间线。

### NoIT

主要回答：

> **这个主题目前最完整、最可信的知识是什么？**

强调：

- 多来源融合；
- 知识去重；
- 独立学习；
- 时效更新；
- 来源追溯。

因此 NoIT 不适合机械照搬完整 `brain/` 结构。

但可以借鉴两点：

### 1. 当前结论与历史证据分离

对容易发生“结论反转”的知识，可以考虑：

- 正文始终保持当前最好理解；
- Git 历史保存旧版本；
- 只有重要争议或反转才显式记录变化原因。

### 2. 项目记忆和领域知识分离

NoIT 本身将来可能存在两类信息：

- “这个领域的知识是什么”；
- “我们为什么把 NoIT 设计成这样”。

第二类信息更接近 Project Brain。

目前 `PROJECT_RULES.md` 已负责长期规则，Git commit 保存大部分演变历史，所以暂时**没有必要立即引入 BRAIN.md 工具链**。

如果后续 NoIT 的架构决策明显增多，再考虑增加项目决策层，而不是现在为了工具而工具。

---

## 十一、安装与使用概览

官方当前提供 npm 包：

```bash
npm install -g @mindmux/brain-md
brain setup -y
```

项目根目录初始化：

```bash
brain init
```

然后可通过 CLI：

- list-pages；
- read-page；
- create-page；
- update-truth；
- append-timeline；
- reindex；
- lint-links。

官方还提供 Claude Code / Codex 的可选 SessionStart hooks，让新会话开始时注入页面索引。

具体命令和兼容版本可能变化，真正使用前应以官方 README 为准。

---

## 十二、资源判断

**值得保留。**

原因不是它一定要安装，而是它提供了一个很清晰的“跨 Agent 项目记忆”设计：

> 用普通 Markdown 保存经过筛选的长期事实，用规则文件定义行为，用 CLI 保证写入结构，用 Git 保留完整历史。

它尤其适合我们已经在 NoIT 中确认的原则：

- 跨 AI 平台；
- 仓库作为共同事实基准；
- 不依赖聊天记忆；
- 稳定规则写进文件；
- 当前知识和历史来源可追溯。

但现阶段更适合作为**设计参考与候选工具**，而不是立刻成为 NoIT 的基础依赖。

---

## 来源与状态

- BRAIN.md 官方网站，核验于 2026-10-03  
  https://projectbrain.md/
- mindmuxai/brain.md 官方 GitHub 仓库，核验于 2026-10-03  
  https://github.com/mindmuxai/brain.md
