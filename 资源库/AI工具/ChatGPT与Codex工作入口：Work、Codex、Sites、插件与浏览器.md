---
title: ChatGPT与Codex工作入口：Work、Codex、Sites、插件与浏览器
tags:
  - ChatGPT
  - Codex
  - OpenAI
  - AI工具
  - Agent
type: resource
status: active
updated: 2026-10-09
---

# ChatGPT与Codex工作入口：Work、Codex、Sites、插件与浏览器

本页不是保存某一版产品截图，而是提供一张**可持续维护的入口地图**：遇到任务时应该选 Chat、Work、Codex、Sites、插件、Skill、MCP、内置浏览器还是 Chrome，以及哪些内容必须临时核对当前官方状态。

本页以用户提供的《ChatGPT 橙皮书》为重要来源，并在 2026-10-03 使用 OpenAI 当前官方资料重新校核。原资料自身也明确标注为非官方指南，版本 v0.2.0，最后校验日期 2026-07-13，因此凡是模型、套餐、额度、入口位置、命令参数和可用地区等内容都不直接视为永久事实。

## 一、先按“最终交付物”选工作入口

当前最稳定的选择方法不是记产品菜单，而是先问两个问题：

1. 任务主要进入什么工作现场？
2. 最终要交付什么结果？

| 入口 | 主要工作现场 | 典型交付 |
| --- | --- | --- |
| Chat | 当前对话、快速搜索与轻量文件 | 回答、解释、头脑风暴、短文本 |
| Work | 文档、网页、邮件、表格、业务资料与多步研究 | 报告、文档、表格、PPT、研究成果、Site |
| Codex | 代码仓库、项目目录、终端、Git、测试与开发工具 | 代码修改、测试结果、diff、commit、PR |
| Sites | 网站 / 轻量应用的生成、预览、发布与分享 | 可访问的网站或轻量应用 |

如果一个任务既需要研究又需要开发，可以拆成两个阶段：先在 Work 里收集和结构化业务材料，再由 Codex 把结构化需求转成经过验证的工程修改。

这比把研究、写作、设计、开发、部署全部塞进一个超大任务更容易控制质量。

## 二、Codex 的主要入口怎么选

Codex 的核心不是某一个界面，而是围绕工程任务提供多种执行入口。

### 1. ChatGPT 桌面应用中的 Codex

适合：

- 图形化管理项目与 thread；
- 同时监督多个任务；
- 查看和评论 diff；
- 使用 worktree 隔离并行任务；
- 使用内置浏览器、插件、Skill 和 Automations；
- 需要在本机项目上工作但不想长期停留在终端的用户。

OpenAI 在 2026 年把 Codex 桌面体验纳入 ChatGPT 桌面应用体系；当前桌面应用支持 macOS 与 Windows。具体可用能力仍取决于计划和工作区设置。

### 2. Codex CLI

适合：

- 已经习惯终端；
- 希望在当前项目目录里直接调用 Agent；
- 需要脚本化、CI/CD 或更细的配置；
- 经常和 Git、构建工具、测试命令一起使用。

当前官方资料仍支持通过 npm 安装 / 更新：

~~~bash
npm install -g @openai/codex@latest
codex --version
codex
~~~

Homebrew 用户也可以通过当前官方文档给出的 cask 路径安装或升级。

CLI 命令和斜杠命令会随版本演进，不应把某一版完整命令表固化成长期知识。遇到不确定命令时，以当前版本的帮助信息和官方文档为准。

### 3. IDE Extension

适合：

- 在 VS Code、Cursor 等编辑环境中边读边改；
- 希望 Agent 直接利用当前文件、选区和编辑器上下文；
- 任务主要是局部编码、解释、修复和 Review。

它与 CLI / App 不是互相排斥的替代关系。更实用的思路是按工作粒度切换入口。

### 4. Codex Cloud

适合：

- GitHub 仓库任务；
- 希望任务在 OpenAI 管理的云端环境中继续运行；
- 需要从桌面、网页或移动端继续云端任务；
- 通过分支 / PR 交付结果。

云端任务仍需要清楚的仓库授权、环境、依赖、secret 与测试配置。任务回到本地继续开发前，要先确认远端最新状态。

## 三、第一次使用的安全路径

无论使用 App、CLI 还是 IDE，第一次都不要直接把最重要的项目交给 Agent。

推荐路径：

1. 建立一个独立练习项目；
2. 初始化 Git 并形成干净基线；
3. 只授权当前工作目录；
4. 从“读项目 / 改小页面 / 修可复现 bug / 补 README”开始；
5. 任务完成后先看 diff；
6. 再运行测试、build、lint 或人工验收；
7. 确认无误后再 commit。

当前 Codex 配置文档仍提供 workspace-write 沙盒与 on-request 审批策略。对大多数本地工程任务，可以把它理解为“允许在当前工作区内干活，超出边界或敏感动作再请求确认”的安全基线。

完全访问、跳过审批、系统级安装、破坏性 Git 命令和远程脚本执行不应为了省一次点击就默认开启。

## 四、Thread、项目与 diff

### 项目

项目代表 Agent 当前工作的代码目录或仓库边界。

项目边界越准确，Agent 越不容易读取或修改无关文件。

### Thread

一个明确任务尽量对应一个 thread。比如：

- 首页实现；
- 修登录 bug；
- 优化移动端；
- 补 README。

不同任务分开可以减少上下文互相污染，也方便后续追踪和复盘。

### Diff / Review

Agent 的自然语言总结只是一层说明，真正的工程证据是实际 diff 与验证结果。

Review 时重点看：

- 改了哪些文件；
- 删除了什么；
- 是否改到无关区域；
- 是否新增依赖；
- 是否修改业务规则；
- 是否真实运行测试。

## 五、Work 与 Codex 的边界

当前 OpenAI 官方定位仍然非常清楚：

- **Work**：研究、分析信息并创建文档、表格、演示、报告或 Site；
- **Codex**：写 / 调试代码、运行测试和命令、Review 变更、围绕仓库工作。

两者都采用 Agent 式的多步执行方式，因此界面和行为会越来越像，但默认“工作现场”和“验收标准”不同。

一个实用判断：

> 最终验收主要看内容是否完整、准确、能直接使用 → Work。  
> 最终验收主要看代码是否正确、测试是否通过、diff 是否安全 → Codex。

## 六、Sites：把成果直接变成可访问的网站或轻量应用

截至 2026-10-03，ChatGPT Sites 处于公开 Beta，可用于创建、预览、编辑、发布和分享交互式网站及轻量应用。它可在 ChatGPT Web 的 Work 中使用，也可在桌面应用的 Work 或 Codex 中使用；具体可用性受计划、地区和工作区权限影响。

稳定工作流：

1. 描述网站目的、受众、页面和约束；
2. 提供需要引用的内容、文件、数据或链接；
3. 先检查私有预览；
4. 逐项修改；
5. 保存版本；
6. 选择合适的访问权限并发布；
7. 用真实访问地址再次验收。

如果 Site 使用连接应用，每个访问者仍使用自己的账号和已有权限。连接应用不会因为“做成 Site”就绕过权限控制。

自定义域名、存储额度、公开发布、企业工作区限制等会继续变化，使用前应看当前 Sites 页面。

## 七、内置浏览器与 Chrome 扩展怎么选

ChatGPT 桌面应用中的内置浏览器与 Codex Chrome 扩展解决的是不同问题。

### 内置浏览器

适合：

- 希望任务全程留在桌面应用内；
- 打开公共页面或本地开发页面；
- 多标签页调查；
- 下载文件；
- 在页面上用 annotation 指定需要修改的位置。

它使用独立的浏览器状态，不等于你的日常 Chrome Profile。

### Chrome 扩展

适合：

- 任务需要现有 Chrome Profile；
- 必须复用已经登录的网站会话；
- 需要当前已经打开的标签页；
- 需要现有 Chrome 扩展环境。

无论哪种方式，都应确认当前登录的是正确账号，并只授权任务真正需要的网站。登录凭据应输入在浏览器页面，不应粘贴进聊天消息。

## 八、Plugin、Skill 与 MCP 的当前关系

这三个概念容易被混在一起。按 2026-10-03 OpenAI 当前文档，更准确的理解是：

| 层 | 解决的问题 | 主要内容 |
| --- | --- | --- |
| Skill | “这类任务应该怎样稳定完成？” | 指令、工作流、参考、脚本、模板、资产 |
| MCP | “需要连接什么实时数据或受控动作？” | Server 提供工具、数据、授权和动作 |
| Plugin | “如何把能力包装、安装、分发给用户？” | 可包含 Skill、MCP、连接应用及其他扩展能力 |

Skill 可以独立存在，也可以围绕 MCP 工具提供调用顺序、判断点、异常处理和最终输出要求。

MCP 不负责教模型“整套业务流程应该怎么做”，它主要提供实时信息、认证、授权与动作。

Plugin 是更高一层的分发与组合单位。当前 ChatGPT 与 Codex 共享插件目录，但具体能力是否能在某个入口使用，仍取决于计划、工作区、角色、区域和连接权限。

更详细的实践规则见 [[Skill教程与实践笔记]]。

## 九、官方 Docs MCP：处理 OpenAI 变化信息的优先入口

OpenAI 当前提供只读的官方开发者文档 MCP：

https://developers.openai.com/mcp

Codex CLI 当前配置示例：

~~~bash
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
~~~

它适合在处理 OpenAI API、Codex、Plugin 等快速变化主题时检索当前官方文档，而不是依赖旧教程或模型记忆。

NoIT 已有 openai-docs Skill 安装记录。长期原则仍然是：**产品状态问题先查当前官方来源，静态笔记负责保存稳定方法和入口，不负责假装实时。**

## 十、Automations、Goal 与重复工作

教程把 Automations 作为“让 Agent 按规则定期工作”的能力，这个抽象仍然成立。

适合自动化的任务通常具备：

- 重复发生；
- 输入结构相近；
- 验收条件明确；
- 风险可控；
- 结果适合进入 Review 队列。

例如 CI 失败摘要、issue 分流、定期项目检查、发布简报等。

对于路径不确定但终点清楚的长任务，Codex 当前还提供 Goal 一类持续目标机制。其本质也是把“完成条件”与中间对话分开，让 Agent 持续围绕目标推进。具体命令和最低版本要求应以当前 Codex 文档为准。

## 十一、哪些信息不要长期硬编码

下面这些信息变化较快：

- 当前可选模型与推理档位；
- 套餐、额度和 credit 规则；
- CLI 完整命令清单；
- 斜杠命令名称；
- 插件目录中的具体插件；
- Sites 的地区与计划限制；
- App / 浏览器入口位置；
- 某项 Beta 功能是否已转正；
- 第三方模型路由兼容性。

NoIT 只保留理解和选择这些能力所需的稳定知识；真正使用前重新核验官方文档和账号实际界面。

## 十二、第三方模型与 CC Switch

《ChatGPT 橙皮书》附录使用 CC Switch + DeepSeek 演示第三方模型路由。这个方向属于**第三方扩展**，不是 OpenAI 官方 Codex 能力。

NoIT 工具库已经存在 CC Switch 条目，因此不重复创建资源文档。使用第三方路由时长期保留以下边界：

- 先确认具体 Agent 工具是否仍支持该路由方式；
- API Key 不进入代码或仓库；
- 第三方服务有独立的隐私、计费和稳定性规则；
- 工具调用、上下文长度、模型能力可能与官方路径不同；
- 重要项目先用测试仓库验证，不直接切生产项目。

## 十三、当前官方入口

建议优先使用下列当前官方资料：

- ChatGPT Work 与 Codex：https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
- Codex 计划与可用性：https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
- Codex Cloud：https://help.openai.com/en/articles/20001545-using-codex-cloud
- ChatGPT Sites：https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites
- 内置浏览器：https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app
- Plugins：https://help.openai.com/en/articles/20001256-plugins-in-chatgpt
- Plugin / Skill 架构：https://developers.openai.com/plugins/concepts/plugins
- Skills：https://developers.openai.com/plugins/concepts/skills
- Docs MCP：https://developers.openai.com/learn/docs-mcp
- Codex App：https://openai.com/index/introducing-the-codex-app/

## 十四、ChatToCodex 类第三方 Tunnel 用法：技术原理与安全边界

用户提供的 2026-09-29 剪藏描述：创建 Secure MCP Tunnel ID → 设置仅含 Tunnels Read、Tunnels Use 的 Restricted Runtime API Key → 通过第三方 ChatToCodex 本机 Host 暴露文件读取、写入和命令工具 → 从 ChatGPT MCP App 连接 → 操作本地代码项目。

**可核查与未核查内容要分开。** OpenAI 官方 [tunnel-client](https://github.com/openai/tunnel-client) 确有公开仓库和技术文档，支持将私有 MCP 服务通过出站 HTTPS 连接。第三方 ChatToCodex 的原始代码仓库链接不在该剪藏正文中，未核验其实现、更新和权限；不能将文章所述 npm 安装指令视为已审计的当前安全指南。

**重要风险**：本地 run_command、read_file、write_file 可能访问高权限数据与凭据。先确认真实代码来源、权限范围、审批机制和网络流向；Restricted Key 放系统凭据存储，不发到聊天、公开仓库或日志；先在隔离测试目录验证，再决定是否授权正式工程。

**额度问题**：“将 ChatGPT 网页额度接入 Codex”“接近翻倍”仅为博主个人体验，不代表官方额度、授权或计费规则的当前保证。应按官方文档、实际账户计量和服务条款判断。

来源：Jacky，《保姆级教程｜如何将你的Codex额度翻倍？》，X，2026-09-29：https://x.com/JackyCufe/article/2104819548851753085 。2026-10-09 核查官方 tunnel-client，未安装第三方程序或验证额度说法。

## 来源记录

主要来源：

- 用户提供文件：ChatGPT橙皮书.md
- 原资料：《ChatGPT 橙皮书：从安装到实战案例的全链路使用指南》
- 原资料版本：v0.2.0
- 原资料最后校验：2026-07-13
- 原资料在线阅读：https://bozhoudev.github.io/codex-orange-book/
- 本次重新核验日期：2026-10-03

原资料中的截图和逐点击教程没有复制进 NoIT。原因不是省略知识，而是界面会持续变化；其可长期复用的决策逻辑、工作流、安全边界和当前官方入口已经在本页及相关知识文档中吸收。

## 十五、面向初学者的 Codex 上手检查

新手先选与交付物匹配的入口，而不是先纠结模型、套餐或安装全家桶。依次做：

1. 找到官方 Codex 文档和授权入口；确认当前账号可用功能及所在地支持情况。
2. 在独立的测试项目操作，先运行只读检查（看项目、列计划、报告风险），再批准代码修改。
3. 让工具明确列出它改过的文件、执行命令、测试结果以及尚未验证的部分。
4. 使用 Git 提交或分支保护原项目，拒绝不必要的全盘文件权限和直接远程脚本执行。
5. 涉及 MCP 或外部插件时，区分只读连接、写入动作和需要人批准的对外发布操作。
6. 桌面、CLI、IDE 与云端入口是不同运行场景，不将某个截图中的菜单名视为跨版本标准。

来源：产品经理老王霸，《开源我月入10w+的Codex的使用方法（超详细教学）》，2026-07-07，用户文件处理于 2026-10-09。https://x.com/laowangbabababa/article/2074459150323769843 。文中的套餐、价格、地区注册建议、具体界面位置和命令需要对照最新 OpenAI 官方文档，不以该第三方教学断言现状。
