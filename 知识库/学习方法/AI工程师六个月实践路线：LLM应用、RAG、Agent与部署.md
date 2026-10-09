---
title: AI工程师六个月实践路线：LLM应用、RAG、Agent与部署
tags:
  - 学习方法
  - AI工程
  - Python
  - RAG
  - Agent
status: active
updated: 2026-10-09
---

# AI工程师六个月实践路线：LLM应用、RAG、Agent与部署

这是一条**面向应用型 AI 工程**的项目驱动路线，不是六个月速成基础模型研究员的承诺。目标是能够开发、测试、部署、观察并维护利用现成模型的真实应用。时间安排仅是训练节奏；能力和就业结果因个人基础、投入与市场而异。

## 共同训练法

每月都交付一个可运行的小项目，留下代码、README、测试用例、失败记录和可复查的演示。学习时必须动手执行，不把看完视频当作掌握；遇到问题优先定位输入、状态、API、工具调用、数据和环境中的具体故障。所有练习密钥走环境变量，不提交到公开仓库。开发采用最小权限、可复现环境和版本控制。

## 第一个月：编程、命令行与 Web/API 基础

**目标**：能独立实现 Python 脚本、调用 API、读写文件和 JSON、理解异常、提交到 GitHub，并启动 FastAPI 服务。

| 学习模块 | 必须实际做会 | 最小练习 |
| --- | --- | --- |
| Python | 数据类型、循环、函数、容器、文件、JSON、异常、基础 OOP、venv 与包管理 | 本地 JSON 收支记录或公开 API 数据整理 |
| Git/GitHub | init/add/commit/push/pull、分支、冲突、.gitignore、README | 将每次练习建立独立版本历史 |
| Terminal | 目录导航、文件查看、grep、运行脚本、环境变量与 PATH | 不依靠图形界面完成安装与运行 |
| HTTP/JSON/异步 | GET/POST、状态码、鉴权、请求超时、async/await | 请求公共数据 API 并格式化输出 |
| SQL/pandas | SELECT/WHERE/JOIN/GROUP BY、CSV 清洗与聚合 | 用 SQLite + pandas 输出简单报表 |
| FastAPI | 路由、参数、请求体、Pydantic、uvicorn、/docs | GET/POST API 与有效输入校验 |

参考：[CS50P](https://cs50.harvard.edu/python/)、[Python 官方教程](https://docs.python.org/3/tutorial/)、[GitHub Skills](https://skills.github.com/)、[Learn Git Branching](https://learngitbranching.js.org/)、[MIT Missing Semester](https://missing.csail.mit.edu/)、[MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)、[SQLBolt](https://sqlbolt.com/)、[pandas](https://pandas.pydata.org/docs/getting_started/index.html)、[FastAPI](https://fastapi.tiangolo.com/tutorial/)。

**月末验收**：从终端运行带错误处理的 Python 程序，能调用第三方 API、持久化结果并提交一个基础 FastAPI 仓库。

## 第二个月：LLM 应用工程

**目标**：用真实模型 API 完成可解析、可追踪、会处理失败的多轮应用。

1. **提示词与上下文**：写清目标、输入边界、示例、固定输出格式、未知时如何回应。对同一任务对比不同提示词的实际误差，不迷信特定咒语。
2. **结构化输出**：用 JSON Schema/Pydantic 定义结果；校验类型、缺失字段、拒答、异常值；区分 JSON 文本与受 schema 约束的输出。
3. **工具调用**：给工具清楚的名称、参数和权限，接收模型工具意图，由可信代码执行并将结果回填；处理「无需调用」与失败分支。
4. **流式响应**：处理分块输出与最终聚合；断流、超时和客户端取消时不能误记已成功。
5. **对话状态**：保存角色与轮次，控制上下文长度，支持重置与摘要策略；避免跨用户串数据。
6. **成本与延迟**：记录每次请求的 token、费用、时间、模型版本，设计预算和退化路径。
7. **失败恢复**：429、超时、服务不可用、解析失败分别处理；退避重试设上限，关键副作用确保幂等。
8. **注入与安全**：外部文档和网页是数据，不是系统指令；对工具设置最小权限，模型输出必须验证。

练习顺序：发票/收据结构化抽取 → 带天气、计算与笔记搜索工具的助手 → 支持 /reset 的 CLI 多轮聊天 → 接 FastAPI 并加入超时和日志。

参考：[OpenAI Prompting](https://platform.openai.com/docs/guides/prompt-engineering)、[Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)、[Function Calling](https://platform.openai.com/docs/guides/function-calling)、[Conversation State](https://platform.openai.com/docs/guides/conversation-state)、[Anthropic Tool Use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)、[Tenacity](https://tenacity.readthedocs.io/)、[OWASP Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)。

**月末验收**：一个可调用工具并输出结构化结果的服务；故障、拒答与恶意输入至少有可复现测试。API 文档路径与模型支持能力使用时重新核实。

## 第三个月：检索增强生成（RAG）

**目标**：构建有引用且能够测量检索质量的问答系统，而不只是把文档塞进向量库。

1. **Embedding**：理解向量、相似度、不同模型的空间不兼容；用 20 句话做最近邻检索。
2. **Chunking**：比较固定长度、递归和语义切片；记录源文件、页码、标题、时间；检查跨段落断裂。
3. **向量库**：使用 Chroma、Qdrant 或 pgvector 写入向量和元数据、按 top-k 搜索；设计增量更新和删除。
4. **元数据过滤**：按日期、用户权限、主题、文件版本过滤，避免返回错范围文本。
5. **Rerank**：先召回更多候选、再重排少量文本，测量延迟与正确证据命中率。
6. **检索失败诊断**：语义偏移、错误 chunk 边界、top-k 太小、缺少元数据、知识根本没被索引，分别处理。
7. **幻觉控制**：回答必须有证据，缺失时明确说无法确认；引用精确指向文档位置而不凭空构造。
8. **框架选择**：先实现最小原生管道，再根据需要引入 LangChain 或 LlamaIndex，不让框架概念取代数据与测试。

实践：索引 50—100 页合法可用的公开文档 → 含来源的问答 → 手工设定正确证据问题 → 对比切块、过滤、重排策略。

参考：[Chroma](https://docs.trychroma.com/)、[Qdrant](https://qdrant.tech/documentation/)、[pgvector](https://github.com/pgvector/pgvector)、[Google Embeddings](https://developers.google.com/machine-learning/crash-course/embeddings)、[LlamaIndex](https://docs.llamaindex.ai/)。

**月末验收**：能指出一个失败案例究竟是召回失败、证据误用还是回答生成错误，并可重复测量改善。

## 第四个月：Agent、工作流与评测

**目标**：明确什么时候要 Agent，什么时候固定流程更好；让工具调用受控、过程可观察。

- Agent loop：目标 → 选择动作 → 工具结果 → 更新状态 → 停止；设置最大步数、预算与退出条件。
- Tool selection：区分只读与有副作用工具；破坏性操作审批，不在提示词里授予高危权限。
- State：任务检查点、数据库与可恢复状态，跨进程时不依赖一次会话记忆。
- Retry：按错误类型退避/重试，保证幂等，不让 Agent 无限循环。
- Workflow：确定性阶段用程序编排；仅在需要推理和选择时调用模型。
- Evals：构建 30 组来自真实文档的问答；分别测任务完成、工具正确、引用正确、费用、延迟、人工干预率。
- Human-in-the-loop：重要决策与外部写操作需要人工批准，记录被拒绝或回滚的原因。

**月末项目**：在第三个月 RAG 应用之上构建离线 eval harness 与多步骤工具链，保存基线、回归样本、失败分类和前后结果。详见 [[工程Agent工作流：从任务边界到可审查交付]]、[[AI产品工程：评测、上下文与系统优化]]。

## 第五个月：部署、可靠性与产品工程

**目标**：把实验变成能安全运行、定位错误和控制费用的服务。

| 模块 | 交付要求 |
| --- | --- |
| FastAPI 生产配置 | 明确服务启动、健康检查、CORS、连接生命周期，负载前先测试；不照搬旧版本部署命令 |
| Docker | Dockerfile、Compose、环境变量、镜像大小和本地重建 |
| 后台任务 | 长任务队列、重试、超时、任务状态、失败补偿 |
| 身份与密钥 | 鉴权、权限、速率限制、秘钥轮换与泄漏检查 |
| 观测 | 结构化日志、trace、每一步模型及工具耗时/成本、错误率 |
| Prompt 版本 | 模板、模型、配置、样本版本化；升级能回滚 |
| 成本控制 | 花费上限、缓存、模型路由、重复请求去重、拒绝异常高成本任务 |
| 缓存 | 精确缓存与语义缓存需区别；设置失效和内容更新策略 |

实操：用 Docker Compose 部署 FastAPI + RAG 数据库 + 缓存，提供健康探针、访问控制、日志、监控、费用边界和回滚记录。

参考：[Docker Getting Started](https://docs.docker.com/get-started/)、[FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)、[Celery](https://docs.celeryq.dev/)、[Langfuse](https://langfuse.com/docs/)、[Redis](https://redis.io/docs/)、[OWASP API Security](https://owasp.org/API-Security/)。

## 第六个月：选择一个方向并完成作品集

**方向 A：AI 产品工程师**。LLM 应用、RAG、Agent、后端部署与 UX。做一个有实际用户流程、失败状态和使用说明的端到端产品，尽量测试真实用户完成率。可参考 Vercel AI SDK、Streamlit、Gradio 与 Google PAIR。

**方向 B：应用 ML / LLM 工程师**。在「提示词、RAG、微调」之间选择手段，学习 JSONL 数据质量、LoRA/QLoRA、开源模型、量化与推理优化。比较基线、数据成本、推理耗时和质量，不把微调视作默认答案。参考 [Transformers](https://huggingface.co/docs/transformers/training)、[Unsloth](https://github.com/unslothai/unsloth)、[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)、[vLLM](https://github.com/vllm-project/vllm)。

**方向 C：AI 自动化工程师**。流程编排、CRM/文档/邮件/客服集成，保留业务异常、人审、合规、安全与结果审计。实践一个从授权输入的线索表读取 → 补足企业公开信息 → 按 ICP 评分 → 生成人工审批草稿 → 写回 CRM/表格的流程。不能自动发垃圾营销或未经授权获取个人信息。参考 [n8n](https://docs.n8n.io/)、[Temporal](https://docs.temporal.io/)、[OpenAI Cookbook](https://github.com/openai/openai-cookbook)。

**最终验收**：至少 1 个端到端作品、6 个月项目进阶记录、README 演示、失败案例、测试与成本记录。能对别人解释「为什么选这个方案」「替代方案是什么」「线上出了故障如何定位」。就业、接单和薪酬属于独立的市场验证，不凭原作者的薪酬区间推断个人结果。

## 六个月连续项目路线

1. 月 1：CLI 数据脚本 + SQLite + FastAPI。
2. 月 2：模型 API 的结构化提取、工具调用与可靠性。
3. 月 3：有元数据和引用的 RAG。
4. 月 4：Agent 工作流与可复现 eval。
5. 月 5：容器部署、权限、日志、缓存和成本上限。
6. 月 6：面向一类真实用户的产品／ML 优化／企业自动化作品集。

## 来源与版本记录

- Ronin (@DeRonin_)：《如何在 6 个月内成为人工智能工程师（资源）》，X，2026-03-17；用户提供的中英混排 Markdown，2026-10-09 完整读取 6 个月分段和第六个月三条专攻路线，并重构为中文可执行路线。https://x.com/DeRonin_/article/2033587293064204349
- 文章包含大量外链及个别格式错乱的地址；上文只保留代表性学习入口，**不代表对原文全部外部链接逐一联网验活**。使用前以各项目当前官方文档为准。
- 原文结尾工资、招聘增幅、自由职业时薪以及六个月内成为可雇用工程师的效果属于未经本次独立核验的市场数字和作者判断，不纳入稳态知识。
- 与 [[AI辅助的系统化学习与输出工作流]]、[[工程Agent工作流：从任务边界到可审查交付]] 互相补充；未来 NoIT 与 Study 合并时再统一目录。
