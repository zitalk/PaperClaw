<div align="center">
  <img src="./docs/paperclaw-mark.svg" alt="PaperClaw 论文雷达标志" width="132" />

  <h1>PaperClaw</h1>

  <p><strong>面向多模态视觉与无人机研究的个人论文雷达</strong></p>
  <p>视觉类别广搜 · 本地规则召回 · LLM 精筛 · GitHub Issues 知识化</p>

  <p>
    <a href="https://zitalk.github.io/PaperClaw/"><img src="https://img.shields.io/badge/研究门户-在线访问-0D6B66?style=flat-square" alt="研究门户" /></a>
    <a href="https://github.com/zitalk/PaperClaw/issues"><img src="https://img.shields.io/badge/论文卡片-GitHub_Issues-24292F?style=flat-square&logo=github" alt="GitHub Issues" /></a>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/更新频率-每日-DB6B4F?style=flat-square" alt="每日更新" />
  </p>

  <p><a href="./README_EN.md">English</a> · <a href="https://zitalk.github.io/PaperClaw/">网页</a> · <a href="./daily_reports/">日报</a> · <a href="https://github.com/zitalk/PaperClaw/issues">论文库</a></p>
</div>

---

> PaperClaw 不替你囤积论文，而是把每天涌入的新工作收束成可检索、可回看、可继续追踪的研究线索。

## 这是什么

PaperClaw 是一个面向个人研究方向的自动化文献发现系统。它先对 arXiv 视觉相关类别进行广泛检索，再通过同义词和视觉上下文规则保留高召回候选，最后交给 LLM 按研究相关性精筛。

筛选结果不会变成散落在本地的 PDF：每篇论文生成一张 GitHub Issue 论文卡片，每日结果形成汇总与 Markdown 归档，并自动发布到可搜索的网页门户。

| 能力 | PaperClaw 的处理方式 |
|---|---|
| 发现 | 广搜 `cs.CV`、`eess.IV`、`cs.RO`、`cs.MM`、`eess.SP`，并用跨类别关键词补充 |
| 筛选 | 同义词扩展与视觉语境硬过滤，再由 LLM 分批精筛 |
| 阅读 | 每篇论文生成独立 Issue，整理问题、方法、结果、局限与研究启发 |
| 汇总 | 自动生成每日 Digest 和 Markdown 日报 |
| 发布 | GitHub Pages 自动构建可搜索、可分类的个人研究门户 |
| 存储 | PDF 与 arXiv 源码仅作临时分析，默认处理完成后自动清理 |

## 研究雷达

| 多模态感知 | 显著目标与小目标 | 跟踪与多视角 | 无人机视觉 |
|---|---|---|---|
| RGB-T / RGB-D / RGB-NIR | 多模态显著目标检测 | MOT 与跨相机关联 | 检测、跟踪与分割 |
| RGB-Event / 高光谱 / 音视频 | 红外与弱小目标感知 | ReID 与跨视角匹配 | 定位、导航与重建 |
| 跨模态融合与对齐 | 文本引导检测与分割 | 多视角三维感知 | 小目标与多机协同 |
| 缺失模态与鲁棒学习 | 开放词汇与零样本感知 | 时空一致性建模 | 低空场景与具身决策 |

研究范围不是静态关键词清单。PaperClaw 采用“视觉类别广搜 → 本地规则召回 → LLM 研究相关性判断”的分层策略，在保持覆盖面的同时控制噪声。

## 工作流

```mermaid
flowchart LR
    A[arXiv 视觉类别广搜] --> B[同义词与跨类别补充]
    B --> C[视觉语境硬过滤]
    C --> D[LLM 分批精筛]
    D --> E[单篇 Issue 论文卡片]
    E --> F[每日 Digest 与归档]
    F --> G[GitHub Pages 研究门户]
```

筛选配置位于：

- [`filter_keywords.json`](./skills/rs-paper-pipeline/scripts/config/filter_keywords.json)：研究主题、同义词和排除规则
- [`filter_cross_prompt.md`](./skills/rs-paper-pipeline/scripts/prompts/filter_cross_prompt.md)：LLM 相关性精筛提示词

## 在线使用

- **研究门户：** [zitalk.github.io/PaperClaw](https://zitalk.github.io/PaperClaw/)
- **论文卡片：** [GitHub Issues](https://github.com/zitalk/PaperClaw/issues)
- **每日报告：** [`daily_reports/`](./daily_reports/)

网页会在日报或论文索引推送到 `main` 后自动重新构建，不需要在仓库中保存 PDF 或论文源码。

## 本地运行

### 1. 初始化环境

```powershell
Set-Location skills/rs-paper-pipeline
.\bootstrap.ps1
```

Linux 或 macOS 可运行 `./bootstrap.sh`。

### 2. 配置密钥

复制 `.env.example` 为 `.env`，至少填写：

```dotenv
GITHUB_TOKEN=
LLM_API_KEY=
RS_GITHUB_REPO=zitalk/PaperClaw
```

`GITHUB_TOKEN` 需要目标仓库的 Issues 与 Contents 写权限；LLM 接口兼容 OpenAI Chat Completions 格式。不要提交 `.env`。

### 3. 检查与执行

```powershell
.\.venv\Scripts\python.exe scripts\cli.py doctor
.\.venv\Scripts\python.exe scripts\cli.py filter --dry-run --date YYYYMMDD
.\.venv\Scripts\python.exe scripts\cli.py run --date YYYYMMDD --no-notify
```

默认不会保留下载内容。如确需调试论文解析，可临时设置 `RS_KEEP_DOWNLOADS=true`。

## 自动化

论文检索由 GitHub Actions 远端执行，不依赖个人电脑开机。工作日北京时间 **03:00** 首次检查，若 arXiv 尚未发布候选，则在 **09:30、12:30、15:30** 继续补查；已完成日期会自动跳过。Pages 工作流会在日报更新后自动发布网站。

远程运行前，在仓库中配置：

| 类型 | 名称 | 用途 |
|---|---|---|
| Actions secret | `LLM_API_KEY` | LLM 精筛与论文分析 |
| Actions variable | `RS_GITHUB_REPO` | 目标仓库，值为 `zitalk/PaperClaw` |
| Actions variable（可选） | `LLM_MODEL`、`LLM_API_URL` | 自定义模型与兼容接口 |

仓库内写入使用 GitHub Actions 自动签发的短期 `github.token`，无需保存个人 GitHub PAT。

## 项目结构

```text
PaperClaw/
├── daily_reports/                 # 每日 Markdown 归档
├── papers/                        # Issue 与 arXiv 索引
├── site/                          # GitHub Pages 前端
├── scripts/build_pages_site.py    # 静态站点数据构建
└── skills/rs-paper-pipeline/      # 检索、筛选、分析与发布流水线
```

## 致谢

本项目起源于 [thinson/RS-PaperClaw](https://github.com/thinson/RS-PaperClaw) 的 Issue 驱动论文追踪思路，并针对个人多模态视觉、显著目标检测与无人机研究方向进行了独立重构与扩展。
