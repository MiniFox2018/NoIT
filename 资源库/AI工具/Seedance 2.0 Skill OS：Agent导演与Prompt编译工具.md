---
title: Seedance 2.0 Skill OS：Agent导演与Prompt编译工具
aliases:
  - Emily2040 seedance-2.0
  - seedance-20
  - Seedance Skill OS
tags:
  - AI工具
  - Seedance
  - AI视频
  - Agent Skill
  - Prompt工程
type: resource
status: active
updated: 2026-10-03
---

# Seedance 2.0 Skill OS：Agent导演与Prompt编译工具

## 资源定位

`Emily2040/seedance-2.0` 不是模型本身，也不是简单提示词合集。

它是一个面向 AI Agent 的 **Seedance 2.0 Skill OS**，把视频创作流程拆成多个可以按任务加载的 Skill 和 Reference。

主要目标是：

- 把模糊创意转成可执行镜头；
- 为参考图片、视频、音频分配明确职责；
- 规划多镜头；
- 管理长序列；
- 基于真实已生成素材继续下一段；
- 诊断失败 Take；
- 控制返工和生成成本；
- 处理版权、真人、品牌与 moderation 风险；
- 对 API / 价格 / 模型 ID 等易变化事实进行来源核验。

官方仓库：

https://github.com/Emily2040/seedance-2.0

许可证：MIT。

核验于 2026-10-03 时：

- README 标记版本：v6.7.0；
- `SKILL.md` metadata：v6.7.0；
- 最近公开 commit：2026-09-26；
- 仓库体量约 33 MB；
- 根目录包含 28 个左右的 active sub-skills、references、schemas、evals、validators、examples 等完整工程结构。

---

## 一、它解决的不是“帮我写一句Prompt”

核心路由覆盖：

- 模糊创意访谈；
- 标准 Prompt；
- 短 Prompt；
- Sequence；
- Continuation；
- Reference workflow；
- First/Last Frame；
- Director Engine；
- Retake；
- Troubleshoot；
- Copyright / moderation；
- Professional filmmaking；
- API / pricing / provider facts。

也就是说，它更像：

> **AI 视频生成的 Agent 工作流操作系统。**

---

## 二、最值得用的几个模块

### seedance-prompt

把已经明确的场景编译为 production-ready Prompt。

### seedance-sequence

长故事拆成连续 Clip，并维护项目状态。

### seedance-continuation

根据已经接受的上一段视频或最后一帧继续，而不是只依赖原计划。

### reference-workflow

给图片、视频、音频参考分配具体角色。

### shot-table

多人 / 多镜头时，先检查空间几何，再写 Prompt。

### retake-protocol

把失败后的下一步分成：

- Keep；
- Fix in post；
- Edit；
- Re-roll；
- Rewrite；
- Stop / change approach。

### directing-engine

把“cinematic”等抽象愿望转换成：

- 镜头；
- 光线；
-表演；
- Blocking；
- 声音；

并要求这些选择共同服务一个明确意图。

---

## 三、它最成熟的地方：不仅写Prompt，还维护状态

长序列中，它维护：

- Project State；
- Clip Contract；
- accepted / rejected 状态；
- observed end state；
- completed beats；
- reserved future beats；
- continuity locks；
- Take history；
- reference registry。

这使下一镜不再只是：

> “接着上一段继续。”

而是：

> 从已经接受的上一段真实结束状态继续，明确哪些动作已经发生、哪些未来 Beat 还不能提前发生。

---

## 四、它非常强调“来源事实”和“创作启发式”分离

仓库专门维护：

- api-status；
- source-registry；
- platform-surface-matrix；
- evidence notes。

同时明确：

- 平台价格会变；
- API 会变；
- 模型 ID 会变；
- provider 暴露能力不同；
- 2.0 和 2.5 不能混用参数；
- 作者自己的启发式规则不等于官方限制。

这是一个非常值得参考的 AI Skill 设计标准。

---

## 五、证据边界

这个仓库不能理解为“所有规则都已经通过大规模生成实测”。

README 明确说明：

- Repository checks 只验证路由、结构、打包、来源元数据等；
- 这些检查**不是 rendered-quality verdict**；
- live model score 和 rendered pilot 仍有部分 pending；
- 多语言虽然已覆盖，但 independent review 仍未全部完成。

此外，一些规则来自少量真实 Take：

- Shot Table；
- camera side；
- reaction reverse；
- room crossing；
- secondary character idle business；

这些经验很有价值，但样本还不足以把它们当成模型科学定律。

---

## 六、版本与时效风险

该项目迭代非常快。

核验时发现：

- README / root skill 已是 v6.7.0；
- `V6_SEQUENCE_PROMPT_COMPILER_MANIFEST.md` 仍写 active package v6.6.0。

说明部分文档可能存在短暂版本漂移。

因此真正使用前，应优先：

1. 看 root `SKILL.md`；
2. 看 CHANGELOG；
3. 查看最近 commit；
4. 再读取当前任务对应的具体 reference；
5. 对 API、价格、模型限制回到当前官方资料核验。

---

## 七、Seedance 2.0与2.5边界

这个工具明确是 **Seedance 2.0 Skill**。

截至 2026-10-03，字节官方已经有 Seedance 2.5。Seedance 2.5 支持最长 30 秒单次生成，并强化长叙事、参考和编辑。citeturn928000search0turn928000search2

因此：

### 可以跨版本借鉴

- Shot Table；
- Director's Read；
- reference role map；
- continuity state；
- retake decision；
- Prompt Compiler；
- accepted footage overrides planned state。

### 不能直接跨版本照搬

- 时长；
- Shot timing 行为；
- provider model ID；
- 上传数量；
- API 字段；
- resolution；
- edit / extend 暴露方式。

---

## 八、是否值得使用

**值得保留，并且属于高价值候选工具。**

最适合：

- 经常用 Seedance 2.0；
- 使用 Codex / Claude Code / Cursor 等 Agent；
- 想把 Prompt 写作变成系统工作流；
- 有连续多镜头项目；
- 需要对失败 Take 做结构化返工；
- 需要跨会话保存项目状态。

如果只是偶尔生成一个简单短视频，完整安装可能过重，直接使用其中的简化方法即可：

- Director intent；
- Shot Table；
- Reference role；
- Retake protocol。

---

## 九、与NoIT知识的关系

完整方法论已吸收到：

[[AI视频导演式Prompt编译：镜头表、参考权、连续性与返工]]

并与：

- [[AI短片资产化制作工作流：角色、场景、道具与逐镜头生成]]
- [[AI长片规模化制作：Prompt规范、连续性与工程档案]]
- [[参考视频动作迁移与白模控制]]

共同组成 AI 视频生产知识体系。

---

## 来源与状态

- GitHub：Emily2040/seedance-2.0  
  https://github.com/Emily2040/seedance-2.0
- 根 README / SKILL.md：核验于 2026-10-03
- License：MIT
- 当前主要版本标记：v6.7.0
