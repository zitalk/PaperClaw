<p align="center">
  <img src="./docs/logo-220.png" alt="PaperClaw Logo" width="120" />
</p>

# PaperClaw 🦞

Zitalk 的个人论文自动追踪与分析系统。

每天自动执行：

> arXiv 视觉类别广搜与关键词补充 → 同义词/视觉上下文硬过滤 → LLM 分批精筛 → 单篇 GitHub Issue → 每日汇总 Issue → Markdown 归档

## 研究范围

- 多模态显著目标检测：RGB-T、RGB-D、RGB-NIR、RGB-Event、音视频及其他模态组合
- 多模态视觉学习：跨模态融合、非对齐/缺失模态、不确定性、鲁棒学习和参数高效适配
- 多视角与多目标感知：MOT、跨相机关联、跨视角匹配和 ReID
- 无人机视觉：检测、跟踪、分割、定位、导航、小目标感知及多机协同视觉

筛选规则位于：

- `skills/rs-paper-pipeline/scripts/config/filter_keywords.json`
- `skills/rs-paper-pipeline/scripts/prompts/filter_cross_prompt.md`

默认广搜 `cs.CV`、`eess.IV`、`cs.RO`、`cs.MM` 和 `eess.SP`，再用跨类别关键词补充可能落在其他类别的相关论文。候选按 35 篇一批交给 LLM，避免扩大召回后单次提示过长。

PDF 和 arXiv 源码只在分析期间临时下载，Issue 与预览图上传成功后自动清理；如需保留，可在流水线 `.env` 中设置 `RS_KEEP_DOWNLOADS=true`。

## Windows 本地初始化

```powershell
Set-Location skills/rs-paper-pipeline
.\bootstrap.ps1
```

然后编辑 `skills/rs-paper-pipeline/.env`，至少配置：

```dotenv
GITHUB_TOKEN=
LLM_API_KEY=
RS_GITHUB_REPO=zitalk/PaperClaw
```

`GITHUB_TOKEN` 需要对目标仓库具有 Issues 和 Contents 写权限。模型接口支持 OpenAI-compatible Chat Completions API。

## 本地验证

```powershell
Set-Location skills/rs-paper-pipeline
.\.venv\Scripts\python.exe scripts\cli.py doctor
.\.venv\Scripts\python.exe scripts\cli.py filter --dry-run --date YYYYMMDD
.\.venv\Scripts\python.exe scripts\cli.py run --date YYYYMMDD --no-notify
```

## 自动运行

仓库保留了手动和定时 GitHub Actions 工作流。启用前需要在仓库中配置：

- Actions secret：`RS_GITHUB_TOKEN`
- Actions secret：`LLM_API_KEY`
- Actions variable：`RS_GITHUB_REPO=zitalk/PaperClaw`
- 可选 variable：`LLM_MODEL`、`LLM_API_URL`

## 致谢

本项目基于 [thinson/RS-PaperClaw](https://github.com/thinson/RS-PaperClaw) 定制，保留其 Issue 驱动的论文追踪、日报生成和 Markdown 归档设计。
