# 2026-10-09｜两个 Skill 长文：12 层、10 个对象和源码目录的独立覆盖记录

## 来源、权益与证据等级

- 来源 A：[雪踏乌云：我的 55 个 AI视频 Skill 全部开源](https://x.com/Pluvio9yte/status/2081648099680743554)，可读网页：https://www.jxxy.net/ai/articles/pluvio9yte-55-ai-video-skills/ ，[Pluviobyte/rnskill](https://github.com/Pluviobyte/rnskill) 源仓库。
- 来源 B：[宋宋：别再装了就忘：十个用得上的 Skill](https://x.com/songsong/status/2084966880616566843)，[作者自己的完整网页](https://imsongsong.com/articles/2084966880616566843)。
- **来源 A 全部可见的 12 个功能组与示例工作流均已阅读，来源 B 全部可见的 10 个对象、流程演示和风险提醒均已阅读**，并与相应仓库实际 README / 目录 / 部分 SKILL.md 对照。网页图片中的表格或未提供的底层资产不冒充已读取。
- rnskill 顶层 [LICENSE](https://github.com/Pluviobyte/rnskill/blob/main/LICENSE) 为 **CC BY-NC 4.0**；第三方嵌入子技能需依其原许可。dbskill 亦为 CC BY-NC 4.0；未经商用授权，不以“GitHub 公开”推导免费再分发和商业使用。
- 作者报告的涨粉、制作耗时、盈利、技能安全扫描结果属个人案例；**本次仅完成资料阅读与 GitHub 文件结构/部分说明核验，没有安装、执行、授权账号、下载视频或安全扫描。**

## A. “55”数字的真实结构

原文章 12 组数量合计 **4+5+2+1+1+3+2+6+1+2+6+22=55**。第 11 组标“6”但可见正文只给出 5 个具体名称，第 12 组的“22 个 dbs”只有图片分类，不能据此编造完整名录。

2026-10-09 读取上游当前 README：标注 **61 个顶层 Skill 目录（含别名）**；递归 GitHub 树发现 **65 个 SKILL.md**，其中顶层直接位置 **60** 个、嵌套 **5** 个。两套统计不是同一口径；本轮保留当前文件清单供后续对照，**不等于 65 份说明全文均已读取**。

### 十二层逐项处理

| 层 | 作者原始数量 | 原文内容 | 最终去向和独立判断 |
|---|---:|---|---|
| 1 选题与策划 | 4 | 选题卡、实操策划、Hook 选型、标题候选 | Skill教程与实践笔记.md：视频制作12层 |
| 2 内容创作 | 5 | 视频准备调度、转写、脚本、中文表达与公众号提取 | 视频生产线与版权准入 |
| 3 下载 | 2 | 多平台下载、音频与字幕文件准备 | 版权与平台许可核验 |
| 4 配音 | 1 | IndexTTS2 参考声线、音频版本与试听 | 最终音频作为字幕依赖 |
| 5 数字人 | 1 | HeyGen 形象/音频确认与付费关口 | 影像与声线授权 |
| 6 剪辑 | 3 | 口播精剪、video-use、另一口播工具/FCPXML | 工程/切点验收 |
| 7 字幕 | 2 | 音频真实转写、字幕样式、分句/SRT 与 QC | 不按字数伪造时码 |
| 8 视觉封面 | 6 | 手绘 IP、点阵、拼贴、视觉风格、封面 SVG | 保持可编辑资产及来源 |
| 9 图文制作 | 1 | Markdown 拆页、HTML 排版、图文截图 | 文字与页面完整性 |
| 10 总调度与复盘 | 2 | 唯一交接合同、制作队列、最终 QC 与数据归档 | 幂等、人工验收与回退 |
| 11 HyperFrames | 6（原文标注） | 动效导演、复刻、暗色SaaS、打字机、复刻 QC | 文章正文只列出5个具体名称；第6个不能补猜 |
| 12 dbs | 22（文章版本） | Hook/内容/决策/运营等跨场景商业与创作技能 | 独立上游 dbskill，当前项目不是22固定值 |

**落地**：[Skill 资源与方法](../../资源库/Skill/Skill教程与实践笔记.md) 补十二层的输入输出、授权风险及两条可复用生产线；[视频工程知识](../../知识库/AI视频/代码生成视频：确定性逐帧渲染、音画统一时间线与Agent工作流.md) 补交接稿、异步幂等、人工关口、音频版本与字幕 QC；[Skill 收藏表](../../资源库/Skill/Skill收藏与安装清单.md) 收录一个上游合集入口，不在主收藏表里机械扩为 55 个同类项目。

**明确修订**：旧“55”不能作为当前真实技能数量；项目内 `video-use` 与 Browser Use 上游实际实现/维护分开追溯；`dbs` 当前有独立项目和版本；“洗稿隐藏来源、去水印”不取得二次发布的权利；“每月不到10小时”和作者固定声线不构成通用结果。缺失第 11 组第 6 个名称及第 12 组图片里的逐项说明，在本轮保持待补状态。

## B. “十个用得上的”完整对象对账

| # | 原文项目 | 可核验官方仓库 | 正确分类 | 处理结果 |
|---:|---|---|---|---|
| 1 | SkillSpector | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 安全扫描器；带真实 skill-inspector 技能 | 独立新条目；可能远程 LLM；未执行 |
| 2 | AgentSeal | [getagentseal/agentseal](https://github.com/getagentseal/agentseal) | Agent/MCP配置与安全扫描 CLI | 工具库，不冒充 SKILL.md；未执行 |
| 3 | Semia | [berabuddies/Semia](https://github.com/berabuddies/Semia) | Skill 源文件效果分析及证据行 | 独立新条目；CLI模型/repair改写有风险；未执行 |
| 4 | last30days | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 多平台近期讨论检索 Skill | 原已收藏；不重复 |
| 5 | humanizer | [blader/humanizer](https://github.com/blader/humanizer) | 英文语言结构诊断 Skill | 新增；区别既有 humanizer-zh |
| 6 | taste-skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 前端设计多技能合集 | 原已收藏；不重复 |
| 7 | Dashi PPT | [chuspeeism/dashi-ppt-skill](https://github.com/chuspeeism/dashi-ppt-skill) | 静态HTML演示及可编辑PPTX | 原已收藏；当前技能版本与旧文章不同 |
| 8 | workbuddy-xhs-skills | [jackbauerxu/workbuddy-xhs-skills](https://github.com/jackbauerxu/workbuddy-xhs-skills) | 10份XHS内容/视觉运营真实Skill | 新合集；未在顶层看到明确License |
| 9 | ecommerce-visual-copywriting | [feichanggege/ecommerce-visual-copywriting-skill](https://github.com/feichanggege/ecommerce-visual-copywriting-skill) | 电商证据/视觉/分镜单技能 | 新增；未实际合成图片 |
| 10 | Voicebox | [jamiepine/voicebox](https://github.com/jamiepine/voicebox) | 本地语音应用，非普通Skill | 工具库；声线授权、模型依赖 |

**价值并非“十个都安装”**。文章最可取的是：先做来源与安全扫描、明确输入授权、按实际任务触发（研究→写作→设计→幻灯片/电商→图文运营→声音），并为每个 Skill 记录反例、不触发情况、最小权限和明确交付。SkillSpector 的最新 README 是 17 大类 **71** 个检测模式，文章的 68 属历史快照；Semia CLI 和宿主插件对 LLM 的依赖不同，AgentSeal 还支持本地 guard 但不能保证其他命令也无数据外传。作者的“自动跨平台三审门卫”只是一段建议 Prompt，不是已部署系统。

**落地**：[Skill 实践笔记](../../资源库/Skill/Skill教程与实践笔记.md) 保存十项目的真实用途、风险与长期使用流程；[工程 Agent](../../知识库/AI工作方式/工程Agent工作流：从任务边界到可审查交付.md) 提供权限、哈希、静态误报及人工执行合同；[Skill 收藏](../../资源库/Skill/Skill收藏与安装清单.md) 对 6 项新增或纠偏去重；[工具库](../../资源库/工具库/AI、办公与研究工具.md) 单独记录 AgentSeal / Voicebox，不冒充 Skill。

## C. 上游 rnskill 的当前实际 SKILL.md 路径（存在性清单）

本节依据 GitHub 递归树列出 **65 个实际文件**，用于将来逐项选装/审计。**文件存在不是功能成功、脚本安全、许可证适用或内容完整阅读的证据**。嵌套的技能不一定是可单独安装的顶层项目。

| # | 上游文件 | 大致分组 | 本次证据级别 |
|---:|---|---|---|
| 1 | [skills/ai-jian-koubo/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ai-jian-koubo/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 2 | [skills/avatar-keyframe-video/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/avatar-keyframe-video/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 3 | [skills/chengfeng-videocut-skills/剪口播/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/chengfeng-videocut-skills/%E5%89%AA%E5%8F%A3%E6%92%AD/SKILL.md) | 口播剪辑子技能 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 4 | [skills/chengfeng-videocut-skills/口播成片/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/chengfeng-videocut-skills/%E5%8F%A3%E6%92%AD%E6%88%90%E7%89%87/SKILL.md) | 口播剪辑子技能 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 5 | [skills/chengfeng-videocut-skills/口播成片/动画/ian-xiaohei-svg-motion/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/chengfeng-videocut-skills/%E5%8F%A3%E6%92%AD%E6%88%90%E7%89%87/%E5%8A%A8%E7%94%BB/ian-xiaohei-svg-motion/SKILL.md) | 口播剪辑子技能 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 6 | [skills/chengfeng-videocut-skills/自进化/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/chengfeng-videocut-skills/%E8%87%AA%E8%BF%9B%E5%8C%96/SKILL.md) | 口播剪辑子技能 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 7 | [skills/dbs-action/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-action/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 8 | [skills/dbs-agent-migration/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-agent-migration/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 9 | [skills/dbs-ai-check/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-ai-check/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 10 | [skills/dbs-benchmark/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-benchmark/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 11 | [skills/dbs-chatroom-austrian/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-chatroom-austrian/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 12 | [skills/dbs-chatroom/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-chatroom/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 13 | [skills/dbs-content-system/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-content-system/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 14 | [skills/dbs-content/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-content/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 15 | [skills/dbs-decision/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-decision/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 16 | [skills/dbs-deconstruct/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-deconstruct/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 17 | [skills/dbs-diagnosis/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-diagnosis/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 18 | [skills/dbs-goal/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-goal/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 19 | [skills/dbs-good-question/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-good-question/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 20 | [skills/dbs-hook/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-hook/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 21 | [skills/dbs-learning/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-learning/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 22 | [skills/dbs-report/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-report/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 23 | [skills/dbs-resonate/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-resonate/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 24 | [skills/dbs-restore/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-restore/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 25 | [skills/dbs-save/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-save/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 26 | [skills/dbs-slowisfast/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-slowisfast/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 27 | [skills/dbs-spread/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-spread/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 28 | [skills/dbs-xhs-title/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs-xhs-title/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 29 | [skills/dbs/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/dbs/SKILL.md) | dbs/商业分析系 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 30 | [skills/editorial-collage-motion/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/editorial-collage-motion/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 31 | [skills/editorial-dot-cover/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/editorial-dot-cover/SKILL.md) | 视觉封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 32 | [skills/grok-build-cli/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/grok-build-cli/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 33 | [skills/heygen-digital-avatar/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/heygen-digital-avatar/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 34 | [skills/ian-xiaohei-illustrations/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ian-xiaohei-illustrations/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 35 | [skills/jev-office-gate/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/jev-office-gate/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 36 | [skills/novel-distill/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/novel-distill/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 37 | [skills/ra-audio-to-subtitles/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-audio-to-subtitles/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 38 | [skills/ra-hook/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-hook/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 39 | [skills/ra-local-talking-head-cut/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-local-talking-head-cut/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 40 | [skills/ra-video-download/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-video-download/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 41 | [skills/ra-video-production-director/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-video-production-director/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 42 | [skills/ra-video-title/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-video-title/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 43 | [skills/ra-video-wash-pipeline/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-video-wash-pipeline/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 44 | [skills/ra-人话/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-%E4%BA%BA%E8%AF%9D/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 45 | [skills/ra-公众号提取/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8F%90%E5%8F%96/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 46 | [skills/ra-复盘/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-%E5%A4%8D%E7%9B%98/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 47 | [skills/ra-实操策划/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-%E5%AE%9E%E6%93%8D%E7%AD%96%E5%88%92/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 48 | [skills/ra-洗稿/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-%E6%B4%97%E7%A8%BF/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 49 | [skills/ra-选题/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-%E9%80%89%E9%A2%98/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 50 | [skills/ra-逐字稿提取skill/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/ra-%E9%80%90%E5%AD%97%E7%A8%BF%E6%8F%90%E5%8F%96skill/SKILL.md) | ra/生产流程 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 51 | [skills/rn-bw-text-opener/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/rn-bw-text-opener/SKILL.md) | rn/动效与封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 52 | [skills/rn-dark-saas-video/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/rn-dark-saas-video/SKILL.md) | rn/动效与封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 53 | [skills/rn-human-motion-extractor/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/rn-human-motion-extractor/SKILL.md) | rn/动效与封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 54 | [skills/rn-motion-director/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/rn-motion-director/SKILL.md) | rn/动效与封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 55 | [skills/rn-motion-replica/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/rn-motion-replica/SKILL.md) | rn/动效与封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 56 | [skills/rn-niulai-style-image/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/rn-niulai-style-image/SKILL.md) | rn/动效与封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 57 | [skills/rn-replica-qc/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/rn-replica-qc/SKILL.md) | rn/动效与封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 58 | [skills/skill-captions/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/skill-captions/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 59 | [skills/skill-cover/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/skill-cover/SKILL.md) | 视觉封面 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 60 | [skills/tts-skill/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/tts-skill/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 61 | [skills/video-use/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/video-use/SKILL.md) | 视频编辑子技能 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 62 | [skills/video-use/skills/manim-video/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/video-use/skills/manim-video/SKILL.md) | 视频编辑子技能 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 63 | [skills/xhs-article-to-images/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/xhs-article-to-images/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 64 | [skills/孙割/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/%E5%AD%99%E5%89%B2/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |
| 65 | [skills/孙宇晨/SKILL.md](https://github.com/Pluviobyte/rnskill/blob/main/skills/%E5%AD%99%E5%AE%87%E6%99%A8/SKILL.md) | 其他技能或兼容入口 | 已定位文件；不代表逐文件内容/脚本已完整审查或运行 |

## 待补与下一步

1. 来源 A：第 11 组文章“6 个”但正文只列 5 名，速查表及 dbs 双图片还需原始可读素材；当前上游与原文章时点可能版本不同，因此**维持部分吸收**，不补造空缺技能。
2. 来源 B：作者全文可读、十个对象均能定位到真实仓库并有明确去向；其中实际运行/成本/安全评分无独立复核，属于“**可见知识主题已吸收，实操未经验证**”。
3. 涉及 `ra-video-wash-pipeline` 或第三方账号/语音/下载的脚本，不能仅凭项目说明推导可以合规处理任意博主作品；安装、剪辑或账号授权需用户另行指定。
4. 原优先队列第 6—15 项保留待处理，不将一个批次的完结说明扩写成其余十篇也已完成。
