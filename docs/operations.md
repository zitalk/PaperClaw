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

论文检索由 GitHub Actions 远端在工作日执行，不依赖个人电脑开机。北京时间周一至周五 **03:00、09:30、12:30、15:30、18:30、21:30、23:30** 分批检索，已有论文的日期也继续补扫。周一每轮依次检查上周五、周六、周日，周二至周五每轮检查前一天；周末不启动任务。GitHub 调度可能排队，时间为计划触发时间，不保证准点完成。Pages 工作流会在日报更新后自动发布网站。

**增量追加，不覆盖已收录论文。** 每轮重新查询目标日期的候选；通过当前刊会门槛、已有合格卡片的候选复用匹配结果，不重复调用 LLM 筛选或分析。新候选才进行精筛与处理。日报合并“本轮成功论文＋此前日报正式列表中的有效论文”，按 Issue 去重；关闭、删除、已不符合白名单的旧卡片不恢复，只有日期标签而未正式入报的记录不自动混入。若没有新增且无需刷新卡片，仅更新日报统计及运行状态，保留原概括，不额外调用 LLM 写日报。

**统计分清本轮和累计。** 日报展示本轮候选、本轮 LLM 新筛中、复用匹配、本轮新增入报和目标日累计收录量，不把多轮候选数简单相加。零结果或部分来源不可用，不会让此前收录的论文从日报中消失。工作日的多次检索依然限定同一个目标日期，不是历史论文回填；若记录隔天以后才入库，当前日期窗口不保证补回，也不宣称一次检索或全天补扫能穷尽所有来源。

**没有新论文也发布日报。** 目标日期累计仍为零篇时，更新同一日期的日报 Issue、归档和网页，展示统计、实际检查时间，并附一句简短鼓励；空日报使用固定模板，不额外调用 LLM 写作。日报日期仍指论文的目标日期，不是执行日期。后续补扫更新同一日报，不重复建 Issue。

**零结果与故障分开显示。** 部分来源不可用、LLM 解析降级或论文处理失败，会标注异常；缺失密钥会列为未参与来源，不计作成功检索。主流程在检索或 LLM 调用时直接报错，则 Actions 保持失败，不生成虚假的成功日报。历史日报没有来源健康记录，不倒填“运行正常”；清理后变成零篇的历史日报仍展示清理说明。

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
