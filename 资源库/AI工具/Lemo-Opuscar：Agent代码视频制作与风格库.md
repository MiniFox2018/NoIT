---
title: Lemo-Opuscar：Agent代码视频制作与风格库
aliases:
  - lemo-opuscar
  - Opuscar
tags:
  - 资源库
  - AI工具
  - AI视频
  - Agent Skill
  - 程序化动画
  - Canvas
  - WebGL
type: resource
status: active
updated: 2026-10-03
verified: 2026-10-03
---

# Lemo-Opuscar：Agent代码视频制作与风格库

## 资源定位

Lemo-Opuscar 是一个面向 Coding Agent 的开源代码视频制作系统。

官方仓库：

https://github.com/lemomo-ai/lemo-opuscar

在线图鉴：

https://lemomo-ai.github.io/lemo-opuscar/

它不是视频生成模型，也不是 Prompt 合集。

它把短片生产拆成：

- 导演方法；
- 技术管线；
- 风格规范；
- 可运行 Demo；
- 渲染工具；
- TTS；
- ASR 检查；
- 音乐和 Foley；
- 混音；
- 字幕；
- QA；
- 一键 Build。

核心工作方式是：

> Agent 写 Canvas / WebGL / three.js 代码，逐帧渲染画面，再用程序化音乐、音效、TTS 和 FFmpeg 合成完整影片。

---

## 当前状态

核验于 2026-10-03：

- 仓库公开；
- 默认分支：main；
- README 当前列出 **43 种风格**；
- 原用户文章发布时记录为 39 种，因此风格库已经继续扩展；
- README 展示了 6 分 25 秒的 OPUSCAR 98 长样片；
- 作者明确说明当前 Style 是按 Claude Opus 5.5 调出来的，其他模型不保证同等表现；
- 软件仓库使用 MIT License；
- Demo 使用的第三方素材保留各自授权，应查看每个 Demo 的 CREDITS。

---

## 它由哪几层组成

### 1. AGENTS.md

负责 Agent 的总路由。

它规定：

- Style 和 Story 的职责边界；
- 如何找风格；
- Brief 怎么问；
- 什么时候写 Treatment；
- 什么时候看 Demo；
- 什么时候需要用户确认；
- 最终交付哪些文件。

---

### 2. DIRECTOR.md

负责导演方法：

- Brief；
- Benchmark；
- Story；
- Treatment；
- Style Frame；
- Storyboard；
- Sound；
- Rhythm；
- Camera；
- Performance；
- Failures；
- Delivery；
- Copyright。

它的核心判断是：

> 好看的单帧只是起点，成片还要看声音、节奏、镜头和导演编排。

---

### 3. TECHNIQUE.md

负责技术实现：

- 依赖；
- render(t)；
- 确定性逐帧；
- Timeline；
- TTS；
- ASR；
- Music；
- Foley；
- Loudness；
- Subtitle；
- Review；
- 3D；
- Character Rig；
- Credits。

这使项目不仅“会生成”，而且：

> 能重建、能检查、能修改。

---

### 4. STYLE.md

每一种风格都有自己的 Style Prompt。

一个典型 Style 文件会定义：

- Essence；
- What it is not；
- Material；
- Rendering；
- Colour；
- Type；
- Subtitle；
- Motion；
- Camera Grammar；
- Sound Palette；
- Native Moves；
- Pitfalls；
- Engine；
- Variation Space。

Style 负责的是：

> 风格不变量。

而不是：

> 固定故事模板。

---

### 5. Demo

每种风格有真实 Demo 和源码。

重要规则：

> Treatment 必须先写，Demo 后看。

这样 Demo 只用于学习：

- Brush Engine；
- Rig；
- Shader；
- Audio；
- Render Technique。

而不是复制：

- 故事；
- 镜头；
- 开头；
- 结尾；
- 节奏。

---

## 当前 43 种风格

### 手绘与绘画

1. 蜡笔儿童绘本
2. 水彩笔刷
3. 中国水墨
4. 油画厚涂
5. 一笔画
6. 白板讲解
7. 钢笔淡彩

### 东方传统

8. 皮影戏
9. 浮世绘
10. 红色窗花剪纸
11. 纸雕灯影

### 印刷与版画

12. Risograph 丝网印刷
13. 复古半调案卷
14. 木刻版画
15. 铜版画
16. 丝印旅行海报

### 图形与排版

17. 瑞士动态排版
18. 60s 间谍片头
19. 装饰艺术
20. 蓝图 / 工程制图
21. 彩色玻璃窗
22. 象形运动图形
23. ASCII / CRT 终端

### 信息与发布

24. 数据叙事
25. 等距信息图
26. 暗色科技发布
27. 活体实机录屏
28. 科幻全息界面

### 卡通与动画

29. 1930s 橡皮管卡通
30. 80 年代赛璐璐动画
31. 科幻情景喜剧卡通
32. 50s 扁平卡通

### 游戏

33. 16-bit 像素 RPG
34. HD-2D
35. 微游戏快闪
36. 综艺节奏扁平

### 电影与时代

37. 1920s 默片
38. 后室 / 新怪谈

### 材质与 3D

39. 积木玩具
40. 纸片立体书
41. 移轴微缩
42. 低多边形等距
43. 玻璃质感产品

---

## 最适合什么任务

特别适合：

- 产品发布片；
- 数据叙事；
- 动态排版；
- 品牌视觉；
- UI 功能演示；
- 白板解释；
- 教育视频；
- 复古片头；
- 规则化风格短片；
- 高度需要文字准确性的内容；
- 需要可重复 Build 的视频。

---

## 不太适合什么任务

相对不适合直接作为主方法的情况：

- 写实演员表演；
- 大量复杂人物互动；
- 自然摄影；
- 高度真实的布料、水、火；
- 只需要一次、没有复用价值的随机镜头；
- 用户不愿安装本地工具链。

这些任务更适合：

- 视频生成模型；
- 3D；
- 实拍；
- 混合工作流。

---

## 当前安装方式

### Claude Code Plugin

仓库 README 当前推荐：

~~~sh
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
~~~

之后 Agent 会在第一次使用时下载指南、工具和 Style。

### Clone

也可以：

~~~sh
git clone https://github.com/lemomo-ai/lemo-opuscar.git
cd lemo-opuscar
claude
~~~

### 其他 Agent

README 说明可以把 Skill 目录复制到其他 Agent 的 Skill 目录。

不同产品怎样识别 Skill，仍以其当前机制为准。

---

## 基础环境

当前文档要求：

- Node 20+；
- ffmpeg；
- Python 3.11+ 或 uv；
- 3D / Shader 较重时最好有 GPU。

当前默认：

- 1920×1080；
- 24 fps。

这些是当前项目实现，不是所有代码视频的通用要求。

---

## 一个最简单的使用方式

用户只需要给：

- 风格；
- 主题；
- 时长；
- 语言；
- 可选的人声 / 音乐 / Logo / 图片；
- 是否想先看 Storyboard。

例如：

> 用中国水墨做一支 40 秒短片，讲一家百年茶铺，中文男声，竖屏。

Agent 再自己完成：

- Treatment；
- Shot；
- Cue；
- Style Frame；
- 代码；
- 声音；
- Render；
- QA。

---

## 为什么这个资源值得长期保留

它的价值不只是“43 个风格”。

真正值得参考的是它把 AI 视频生产工程化成了：

~~~text
Director
+
Technique
+
Style
+
Demo
+
Tools
+
QA
+
Credits
~~~

这提供了一个非常完整的 Agent Skill 设计范例。

相比单个 Prompt，它更像一个：

> **可执行的小型动画工作室操作系统。**

---

## 最值得复用的设计

### 1. Style / Story 分离

风格可复用，故事必须重写。

### 2. Treatment First

先创作自己的结构，再读 Demo。

### 3. Single Timeline

画面、音乐、音效、字幕共用同一时间源。

### 4. Deterministic Render

任意帧可独立重建。

### 5. QA as Code

ASR、字幕时长、黑帧、响度、抽帧都自动检查。

### 6. Human Gates

关键阶段让人确认，不把人变成每一步的操作员。

### 7. Credits from Day One

资产一进入项目就记录授权。

---

## 风险与限制

### 模型依赖

作者当前明确表示：

- 所有样片使用 Claude Opus 5.5；
- Style 也按该模型调试；
- 其他模型没有系统测试保证。

因此不能把：

> “有这些 Markdown 就一定能复现”

理解成事实。

### 计算和时间

Agent 一支片通常需要持续写大量代码、渲染、检查和返工。

文章给出的 30–60 分钟属于作者当前机器、片长、风格和模型条件下的经验，不是性能保证。

### 3D 更重

3D 风格需要：

- three.js；
- GPU；
- HDRI；
- 后处理；
- 更大资源量。

通常比 2D 代码风格更难稳定。

### 版权

仓库自身代码为 MIT，但：

- 样片字体；
- Sample Library；
- TTS；
- HDRI；
- 其他素材；

可能有独立许可证。

必须查看 CREDITS。

---

## 与 NoIT 知识的关系

- [[代码生成视频：确定性逐帧渲染、音画统一时间线与Agent工作流]]
- [[AI视频导演式Prompt编译：镜头表、参考权、连续性与返工]]
- [[AI短片资产化制作工作流：角色、场景、道具与逐镜头生成]]
- [[AI长片规模化制作：Prompt规范、连续性与工程档案]]

---

## 来源与版本记录

- GitHub：lemomo-ai/lemo-opuscar
  https://github.com/lemomo-ai/lemo-opuscar
- Gallery：
  https://lemomo-ai.github.io/lemo-opuscar/
- 重点读取：
  - README.md
  - AGENTS.md
  - DIRECTOR.md
  - TECHNIQUE.md
  - styles/README.md
  - 多份 STYLE.md
  - MAINTAINING.md
- 当前核验：2026-10-03。
- 当前 Style 数量：43。
- License：MIT；第三方 Demo 资产按各自许可证处理。
