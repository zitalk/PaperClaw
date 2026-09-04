# 配置与维护

日常检索已在 GitHub Actions 远端运行，本地运行仅用于可选调试。研究范围见 [README](../README.md#研究雷达)。

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
OPENALEX_API_KEY=
SEMANTIC_SCHOLAR_API_KEY=
IEEE_API_KEY=
ELSEVIER_API_KEY=
SPRINGER_NATURE_API_KEY=
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

论文检索由 GitHub Actions 远端在工作日执行，不依赖个人电脑开机。北京时间周一至周五 **03:00** 首次检查：周一依次补扫上周五、周六、周日，周二至周五检查前一天；若来源尚未发布候选，则在 **09:30、12:30、15:30** 继续补查。周末不启动任务，已完成日期会自动跳过；无候选或 LLM 未筛中论文时，不生成空日报。Pages 工作流会在日报更新后自动发布网站。

远程运行前，在仓库中配置：

| 类型 | 名称 | 用途 |
|---|---|---|
| Actions secret | `LLM_API_KEY` | LLM 精筛与论文分析 |
| Actions secret | `OPENALEX_API_KEY` | OpenAlex 元数据检索 |
| Actions secret | `SEMANTIC_SCHOLAR_API_KEY` | Semantic Scholar 元数据检索（全局严格 ≤ 1 请求/秒） |
| Actions secret | `IEEE_API_KEY` | IEEE Xplore 元数据检索；未审批时自动跳过 |
| Actions secret | `ELSEVIER_API_KEY` | Elsevier Scopus 默认 `STANDARD` 元数据接口；不要求 Institutional Token |
| Actions secret | `SPRINGER_NATURE_API_KEY` | Springer Nature 元数据检索 |
| Actions variable | `RS_GITHUB_REPO` | 目标仓库，值为 `zitalk/PaperClaw` |
| Actions variable（可选） | `LLM_MODEL`、`LLM_API_URL` | 自定义模型与兼容接口 |

仓库内写入使用 GitHub Actions 自动签发的短期 `github.token`，无需保存个人 GitHub PAT。

每个来源独立降级：单个接口未授权、限流或临时故障不会阻断其他来源。候选按 arXiv ID、DOI 与规范化标题合并；Semantic Scholar 请求之间至少间隔 1.1 秒，Elsevier 使用默认开放额度下的 Scopus `STANDARD` 元数据视图，不调用需要机构授权的 ScienceDirect 全文接口。

## 项目结构

```text
PaperClaw/
├── daily_reports/                 # 每日 Markdown 归档
├── papers/                        # Issue 与统一论文索引
├── site/                          # GitHub Pages 前端
├── scripts/build_pages_site.py    # 静态站点数据构建
└── skills/rs-paper-pipeline/      # 检索、筛选、分析与发布流水线
```
