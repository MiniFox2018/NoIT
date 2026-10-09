---
title: HTML、CSS与JavaScript入门：从页面结构到Agent建站验收
tags:
  - 独立开发
  - HTML
  - CSS
  - JavaScript
  - Agent
status: active
updated: 2026-10-09
---

# HTML、CSS与JavaScript入门：从页面结构到Agent建站验收

## 学完能做什么

能建立一个可在浏览器打开的三文件静态网页；知道 HTML/CSS/JavaScript 的分工、相对路径和常见故障；能给编码 Agent 下达**只修改某个范围**的任务，并检查桌面端、移动端和 GitHub Pages 发布结果。不会把“Agent 说已完成”当成用户可用的网页，也不会将作者个人主页的身份、品牌和图片复刻为自己的作品。

原文按“网页结构→手写最小页→真实路径与互动→对标设计→Agent实现→浏览器验收→部署/域名”展开。本文保留这一学习顺序，重建**可独立运行的原创最小示例**并纠正原网页代码显示的缺口。只要理解这些约束，不必为了做一页静态主页先引入 React、构建框架和复杂服务端。

## 一、网页、网站和 Web 应用并不等同

- **网页（page）**：浏览器加载的一个页面资源及其关联样式、脚本、图片。
- **网站（site）**：通常是一组具有导航、统一域名和内容组织的网页。
- **Web 应用（application）**：强调输入、业务状态、持久化和交互，例如任务管理、数据查询、账号系统。它仍然通过网页呈现，但不能只用文件数量判断是否是应用。

一个简单个人主页可以全用静态文件完成；加联系表单、账号、私有数据后，就应明确后端、存储、鉴权、防滥用和隐私规则。

## 二、目录、文件与职责

建议的新手项目形态：

~~~text
my-first-site/
├── index.html        # 语义结构、内容、资源引用
├── css/
│   └── style.css     # 布局、颜色、响应式
├── js/
│   └── script.js     # 点击事件、状态变化
├── images/
│   └── avatar.jpg    # 有权使用的头像
└── README.md         # 项目目标、运行与部署说明
~~~

**项目根目录**是以上文件的共同父级。`index.html` 通常是静态主入口；但开发平台、路由与发布目录均可能改变入口规则，不能无限推广为“所有服务器必须从根目录找 index.html”。

| 内容/问题 | 首先检查 | 相关技术 |
|---|---|---|
| 标题、结构、表单、图片说明 | 语义标签、`src`、`href` | HTML |
| 字体、布局、头像大小、手机单列 | 选择器、层叠、盒模型和 media query | CSS |
| 点击事件无反馈 | DOM 元素 ID、脚本加载、控制台报错 | JavaScript |
| 图片裂开或样式不出现 | 相对路径、大小写、文件后缀和服务器根目录 | URL 路径 |
| 本机能看、上线 404 | 发布根目录、资源前缀与 Pages 设置 | 部署 |

不要从视觉截图直接推断文件名；先检查真正的目录树。

## 三、语义 HTML：先让内容完整，后做视觉

最小可交互个人页的 `index.html` 如下。先自行准备合法可用的 `images/avatar.jpg`，或者临时删掉头像行；二者必须一致，否则会出现断图。

~~~html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="一个由我维护的个人项目展示页">
  <title>我的网页实验</title>
  <link rel="stylesheet" href="css/style.css">
  <script src="js/script.js" defer></script>
</head>
<body>
  <header class="site-header">
    <a href="#home">首页</a>
    <nav aria-label="页面导航">
      <a href="#projects">作品</a>
      <a href="#contact">联系</a>
    </nav>
  </header>

  <main id="home">
    <section class="hero" aria-labelledby="intro-title">
      <div>
        <h1 id="intro-title">你好，这是我的个人主页</h1>
        <p>我正在学习网页结构、设计和可交互的前端代码。</p>
        <button id="hello-button" type="button">打个招呼</button>
        <p id="message" role="status" aria-live="polite"></p>
      </div>
      <img src="images/avatar.jpg"
           alt="我的头像，面带微笑面对镜头"
           width="320" height="320">
    </section>

    <section id="projects" aria-labelledby="projects-title">
      <h2 id="projects-title">作品</h2>
      <p>这里将展示我独立完成的项目。</p>
    </section>
    <section id="contact" aria-labelledby="contact-title">
      <h2 id="contact-title">联系</h2>
      <p>正式发布前，再填写准备公开的联系方式。</p>
    </section>
  </main>
  <footer>个人网页练习 · 可以继续修改</footer>
</body>
</html>
~~~

- `head` 配置文档信息、语言编码和视口；`body` 是页面内容；`header/main/section/footer` 帮助建立语义区域。
- 用 `h1` 作为主标题，`h2` 表达区块层级。图片的 `alt` 要描述真实图片；当前示例是占位语义，换图片时应同步改。
- 点击行为由唯一 `id="hello-button"` 与脚本对应；`role="status"` 让反馈可被辅助技术感知。
- 使用 `defer` 加载外部脚本意味着待 HTML 解析后执行，不必机械要求把脚本只能放在 `body` 结束前。该方式同样适用于本例。

## 四、CSS：选择器、盒模型和响应式

`css/style.css` 的原创建议如下：

~~~css
:root {
  color-scheme: light;
  font-family: system-ui, "PingFang SC", sans-serif;
  color: #1c1c1c;
  background: #fff9e6;
}
* { box-sizing: border-box; }
body { margin: 0; }
a { color: inherit; }
.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  padding: 24px max(24px, calc((100% - 1100px) / 2));
}
nav { display: flex; gap: 20px; }
main { max-width: 1100px; margin: 0 auto; padding: 40px 24px 80px; }
.hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(230px, 320px);
  align-items: center;
  gap: 48px;
}
h1 { font-size: clamp(2rem, 5vw, 3.5rem); line-height: 1.2; }
p { line-height: 1.7; }
.hero img { display: block; width: 100%; height: auto; border-radius: 24px; }
button {
  padding: 12px 20px;
  border: 0;
  border-radius: 12px;
  background: #245edb;
  color: #fff;
  cursor: pointer;
}
button:focus-visible, a:focus-visible {
  outline: 3px solid #d35700;
  outline-offset: 3px;
}
section + section { margin-top: 72px; }
footer { padding: 30px 24px; text-align: center; }
@media (max-width: 700px) {
  .site-header { flex-wrap: wrap; }
  .hero { grid-template-columns: 1fr; gap: 24px; }
  .hero img { max-width: 320px; }
}
~~~

最容易出错的一处：**`48px` 是有效尺寸，`48 px`（数字与单位分开）在标准 CSS 中无效**。原文网页转存的示例将部分值显示成 `48 px`、`240 px` 等，应改成紧邻的数字与单位，而不是照抄并误以为 CSS 起作用。样式不生效还可能是选择器没选中、优先级被覆盖、资源加载失败或浏览器缓存。可在开发者工具查看 Computed Styles/Network，不能一概归因于 CSS “有 bug”。

响应式不仅是缩小字号：还要关注导航是否溢出、触控目标是否太小、图片是否变形、是否出现横向滚动，以及用户是否设置了减少动画偏好。以上示例用窄屏单列布局做最小回应，复杂产品还需逐组件测试。

## 五、JavaScript：真实 DOM 反馈，而不是静态按钮

`js/script.js`：

~~~javascript
const button = document.querySelector("#hello-button");
const message = document.querySelector("#message");

if (button && message) {
  button.addEventListener("click", () => {
    message.textContent = "谢谢来访！这个按钮的交互已经连接成功。";
  });
}
~~~

测试应满足：按钮点击前反馈为空，点击后页面出现对应文字，控制台没有错误。如果报 `Cannot read properties of null`，先检查 HTML 是否具有一致的 ID、脚本是否指向正确路径、代码运行时 DOM 是否已构建。与原文只使用弹窗相比，更新页面上的反馈更容易被截图或自动化用例验证，也便于无障碍访问。

注意 `textContent` 用于显示普通字符串；不要为输出不可信用户输入随意拼接 `innerHTML`，以免引入脚本注入风险。

## 六、相对路径与部署路径

从根目录的 `index.html` 引用 `css/style.css`、`js/script.js`、`images/avatar.jpg` 表示从当前文档位置查找对应子目录；`../` 表示上一层。路径大小写和真实扩展名必须匹配。**不要在项目迁移后把本机绝对路径或个人设备目录写进正式文件**。

部署到 GitHub Pages 的“项目页面”时，站点通常有仓库名前缀。只要站点从根目录页面加载相对资源且路径布局保持不变，`css/style.css` 等可以正常工作；以斜杠开头的绝对网站路径则可能误指向域名根目录，造成断图。若采用构建框架或自定义域名，以实际站点的 base path 配置为准。

## 七、学习和排错闭环

每次修改只围绕一个可测试的目标，执行：**说明修改范围 → 检查文件差异 → 保存 → 浏览器刷新 → 点击/观察 → 记录结果**。

| 现象 | 优先证据 | 可能措施 |
|---|---|---|
| 浏览器显示源代码而不是页面 | 实际后缀与 MIME 类型 | 检查是否误保存为 \`.html.txt\`、预览服务配置 |
| CSS 改了无效果 | Network 的 CSS 请求、Computed 属性 | 修路径、缓存、选择器和 CSS 单位 |
| JS 点击没反应 | Console、元素 ID、事件绑定时机 | 校准 ID、`defer`、网络请求和报错 |
| 图片空白 | Network 状态、文件名、大小写和实际图片类型 | 更正相对路径及扩展名、提供合法素材 |
| 手机端横向溢出 | 视口宽度、固定宽度元素、网格 min-width | 改单列、约束图片和内容宽度 |
| 发布后才坏 | Pages URL、仓库前缀、部署选项与资源响应 | 比较线上与本地 Network，修正 base path |

用最小页面学习时，可直接打开 HTML 文件；涉及 Fetch、模块、路由或与线上一致的资源访问时，应使用本地 HTTP 服务，例如在**项目根目录**运行：

~~~bash
python3 -m http.server 8000
~~~

然后访问 `http://localhost:8000/`。它只是本机开发服务，不能当成对外公开或具有鉴权的生产服务器。

## 八、Agent 建站：先抽取参考设计规则，再允许写入

这部分是原作者以“黄色 Punk 个人主页”演示的可迁移方法，**不保留他人的具体身份、图片、品牌和完整 Prompt**。适用步骤：

1. **先定义自己的目标**：真实姓名/昵称是否公开、作品类型、站点用户、必备 CTA 和联系方式；图片和文案必须有授权。
2. **最多选两份设计参考**：记录要借鉴的主色、字体层级、左右结构、留白、封面/按钮节奏和移动端变化。对标分析只提设计规律，不索取他人网页源码、Logo 或图片。
3. **分析模式只读**：让 Agent 根据真实可访问的网页或用户提供的截图/录屏，产出“设计 DNA”——布局比例、颜色的 HEX 近似值、字号层级、组件、交互、动效、响应式差异。若看不到网页/动态效果，标记未知，不能凭网址名字推测。
4. **确认设计**：选一个主参考、少量辅助细节，写出具体“保留”和“禁止复制”的项目约束。
5. **制作模式可写**：只修改当前目标目录，用原生 HTML/CSS/JS 或用户确定的技术栈；保留已存在的文件，提供变更计划；输出真正的文件而不是仅聊天里的代码块。
6. **浏览器验收**：桌面端（例如 1440×900）、窄屏（例如 390×844）逐项检查标题截断、图片保持比例、链接/按钮、触控操作、CSS/JS 加载、控制台与横向滚动。对于高保真互动原型还应测试空态、数据持久化和回退。
7. **返工限定范围**：例如只调整头像尺寸，保留文字与 JS 不变；修改后重新测相同案例。不要用“更高级点”替代可定位的验收条件。

可复用的一轮任务示例（先仅规划）：

~~~text
先只读分析我的现有个人主页和两份参考。
请列出：页面区块、宽度比例、标题层级、颜色用途、按钮状态、手机端差异。
不创建/修改文件，不照抄外部品牌或图片。
输出一个准备采用的设计规则表及需要我确认的差异。
如无法访问参考，请标记缺失，不自行猜测。
~~~

设计确认后的制作任务：

~~~text
目标：完成单页个人作品网站。
输入：上一轮确认的设计规则、我提供的文案与合法素材。
范围：仅本项目的 index.html、css/style.css、js/script.js、images/。
功能：导航可跳转、欢迎按钮可操作、电脑端双列、手机端单列。
边界：不复制参考网站素材、不安装不必要依赖、不覆盖仓库外文件。
验收：浏览器两种尺寸截图、按钮逐项点击、Network/Console 检查。
交付：实际修改文件、未覆盖项、错误及修复证据。失败时准确说明。
~~~

## 九、从本机预览到 GitHub Pages 和域名

静态站点上线的顺序通常是：① 检查文件和敏感信息 → ② 选择仓库与发布方式 → ③ 上传 `index.html` 和所需资源 → ④ 在仓库 Pages 设置按当前官方流程选择分支或 Actions 构建 → ⑤ 等待成功部署 → ⑥ 打开**真实公开 URL** 再验证。**Git 提交成功不等于部署成功**，本地 `localhost` 能看不等于公网可用。不同套餐和隐私方案影响源仓库的可见性，但 Pages 发布的网站通常面向公众。

域名是可选的后续步骤：在域名提供商配置 DNS，按 GitHub Pages 当前说明设置自定义域名，并检查 HTTPS 与证书状态。DNS 生效和证书准备可能需要时间；不要把“购买域名”列为静态主页能发布的强制条件。

上线前检查：个人住址/私人联系方式、账号密钥、客户材料、未授权照片与设计资源、所有第三方统计脚本和可访问性。上线后需要重新访问公开域名做回归，不能拿本地截图代替公网验收。

## 十、完成标准与学习路线

- **文件层**：目录与引用一致；`index.html`、`css/style.css`、`js/script.js` 均存在；头像依说明有真实素材；README 写清如何本地运行。
- **体验层**：文字正常、按钮能交互、电脑/手机阅读清楚、无横向溢出、键盘能找到导航与交互。
- **工程层**：控制台无阻断错误、没有误引用外部私有资源、敏感信息未入库、可回滚。
- **部署层**：如果要求上线，真实访问公开 URL 并测试；没实际部署时只能说“已准备部署”。
- **思维层**：知道需要让 Agent **修改什么**、**不要改什么**、**成功长什么样**，并能给出复查证据。

关联：[[Git与GitHub实践：版本控制、协作、自动化与安全]]（Git/Pages）、[[工程Agent工作流：从任务边界到可审查交付]]（限定权限和测试）、[[小程序八类任务界面：信息顺序、交互状态与结果反馈]]（状态和交互设计）。静态个人网页与小程序不能直接共享所有 API 或部署方式，仅复用产品交互和验收原则。

## 来源与版本记录

- Adrian Punk（@AdrianPunk115），《人人都能用 Agent 做网页：从想法到上线》，原帖 https://x.com/AdrianPunk115/status/2083832138462605504 ，[带示例的可读网页](https://www.jxxy.net/ai/articles/AdrianPunk115-2083832138462605504/)，2026-10-09 阅读可见的十五个主题部分，覆盖网页/网站区别、目录结构、常用标签、独立 HTML 页、CSS、JS、路径、改动循环、本地预览、设计分析、生成、迭代、验收、Pages、域名。作者网页部分内嵌代码被 HTML 转换器切断或出现空白，示例 `48 px` 不是正确 CSS；本教程以可读原理和另写的连贯可执行示例替代，**没有声称逐字提取原作者全部代码或素材图片**。
- CSS 语法和视口响应式的常见约定参考 MDN：https://developer.mozilla.org/zh-CN/docs/Web/CSS ；HTML 元素参考：https://developer.mozilla.org/zh-CN/docs/Web/HTML ；JavaScript DOM 参考：https://developer.mozilla.org/zh-CN/docs/Web/API/Document ；GitHub Pages 官方：https://docs.github.com/en/pages 。本篇为静态示例和工程方法整理，**未实际运行浏览器验收、部署网站或绑定域名**，后续执行时须以目标环境实测为准。
