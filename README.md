# 偶然的数学 · The Mathematics of Chance

**概率论的历史、思想与数学结构**  
*The history, ideas and mathematical structures of probability*

[GitHub 仓库 / Star](https://github.com/apollo4869/chance-mathematics)

从真实的数学史问题出发，沿着概念产生的必要性，逐步建立现代概率论的原创中文数学著作。本仓库保存完整长篇工作稿、完整英译工作稿、证明专题与可离线阅读的网站工程。

An original book following the historical problems and mathematical ideas that led to modern probability. This repository contains the complete long-form Chinese working manuscripts, full English working translations, advanced proof materials, and a bilingual offline-ready website.

## 阅读 / Read

- 中文目录：[dist/index.html](dist/index.html)
- English contents: [dist/en/index.html](dist/en/index.html)
- 中文八章母稿：[chapters/](chapters/)
- Complete English manuscripts: [chapters-en/](chapters-en/)
- 进阶证明：[advanced/](advanced/) · [English advanced materials](advanced-en/)
- 配套译稿：[translations/en/](translations/en/)；逐块对应及公式核对：[manifest.json](translations/en/manifest.json)
- 下载：[完整离线双语版](dist/downloads/complete-offline.zip) · [中英文可编辑原稿](dist/downloads/editable-manuscript.zip) · [English manuscripts](dist/downloads/english-manuscript.zip)

GitHub 文件预览不会直接运行 HTML。下载并解压离线包后，打开 `index.html`；或克隆本仓库，打开 `dist/index.html`。小节 / 整章阅读、前后小节导航和语言切换均保留完整正文。

GitHub previews do not execute the HTML website. Download and extract the offline edition, then open `index.html`, or clone this repository and open `dist/index.html`.

当前[线上正式网站](https://chance-mathematics-six-chapters.goldenmath7.chatgpt.site/)仍为此前批准的六章版。公开本仓库不更新该站点，也不自动发布第七、八章或英译版。

## 内容与审阅状态 / Editorial status

现有八章和六个进阶模块完整保留，不因网站或语言入口调整而精简。英文为完整翻译工作稿，尚待作者阅读及语义终审。技术完整性检查不代表数学、史料或作者验收；四类状态分别维护于 `docs/`。

第一、二章是作者认可的叙事基准；第四章主体与结语的调整已有专项授权；第七章获整体方向认可，第八章及完整英译仍待作者进一步阅读。旧报告是相应版本的历史快照，不能当作当前全书终审结论。

The English edition is a full working translation awaiting author and semantic review. Engineering checks, mathematical review, historical verification, and author approval are independent. The reorganized Chinese working manuscripts have not been certified as identical to the earliest complete ChatGPT conversations.

## 构建 / Build

需要 Python 3.10+、Node.js 18+ 和项目依赖。在仓库根目录运行：

```sh
python -m pip install -r requirements.txt
npm install
python build.py
npm run check
npm test
```

也可按 `pnpm-lock.yaml` 使用 `pnpm install --frozen-lockfile` 安装 JavaScript 依赖。构建只生成本地文件；没有部署步骤。

Serve a local preview from the repository root:

```sh
python -m http.server 8768 --bind 127.0.0.1 --directory dist
```

打开 <http://127.0.0.1:8768/>；英文版为 <http://127.0.0.1:8768/en/>。停止服务器按 Ctrl+C。Windows 也可执行 `./preview.ps1`。

`npm run check` 核对受保护文件、翻译段落与公式对应、双语网页、相对链接、锚点及阅读单元。早期 `check-stage1.py` 面向六章迁移快照，不作为当前八章双语版本的统一入口。

## 工程结构 / Project structure

| 目录或文件 | 用途 |
| --- | --- |
| `chapters/`, `chapters-en/` | 八章独立 Markdown 内容单元 |
| `advanced/`, `advanced-en/` | 完整保留的进阶证明材料 |
| `translations/en/` | 英译配套材料、逐块清单及语言标签 |
| `assets/` | 独立图片与原创封面 SVG |
| `provenance/`, `archives/` | 构建所需图表数据与章节清单、完整旧第四章快照 |
| `tools/`, `build.py`, `build-chapters.py` | 渲染、拆页、内容核对与打包 |
| `site-links.json` | GitHub 仓库与语言入口配置 |
| `dist/` | 可直接离线阅读的完整双语网站及下载包 |
| `docs/`, `reports/` | 写作决定、独立审阅状态及历史检查结果 |

正文以 Markdown / LaTeX 为母稿，网站为展示层。正文实质修改应先取得作者批准并记录差异；不要为通过构建而重置 `baseline-manuscript.json`。

图片、引文与史料来源见[引用与配图来源](引用与配图来源.md)。仓库未另行选择通用开源许可；公开可读不等于放弃作者权利或第三方素材权利。

公开副本只包含教材原稿与工程。早期聊天、来源对照档案和本机审计快照留在作者本地，不随原稿下载包公开。所有现行中英文正文、证明与图片完整保留；公开保护清单沿用相应原始文件哈希。
