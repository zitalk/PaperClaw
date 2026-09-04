<div align="center">
  <img src="./docs/paperclaw-mark.svg" alt="PaperClaw 论文雷达标志" width="132" />

  <h1>PaperClaw</h1>

  <p><strong>面向多模态视觉与无人机研究的个人论文雷达</strong></p>
  <p>四个研究方向 · 交叉标签 · 每日论文卡片</p>

  <p>
    <a href="https://papers.zitalk.cn/"><img src="https://img.shields.io/badge/研究门户-在线访问-0D6B66?style=flat-square" alt="研究门户" /></a>
    <a href="https://github.com/zitalk/PaperClaw/issues"><img src="https://img.shields.io/badge/论文卡片-GitHub_Issues-24292F?style=flat-square&logo=github" alt="GitHub Issues" /></a>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+" />
    <img src="https://img.shields.io/badge/更新频率-工作日-DB6B4F?style=flat-square" alt="每日更新" />
  </p>

  <p><a href="./README_EN.md">English</a> · <a href="https://papers.zitalk.cn/">网页</a> · <a href="./daily_reports/">日报</a> · <a href="https://github.com/zitalk/PaperClaw/issues">论文库</a></p>
</div>

---

> 每天追踪值得读的新工作，让研究线索可检索、可回看，不囤积 PDF。

工作日即使没有新收录，也会更新零篇日报与检查时间；异常会单独说明，零结果不会再表现为网站“停更”。

## 研究雷达

四个主方向允许交叉，一篇论文可拥有多个方向与子方向标签，但只计为一篇。网页支持主方向、子方向、日期和关键词筛选。

### 1. 多模态视觉学习

显著目标检测（SOD）与伪装目标检测（COD）归入本方向，不单列主方向。任务分组不意味着每篇论文都使用多模态输入；保留具有方法参考价值的相关单模态工作。

| 子方向 | 代表关键词 |
|---|---|
| 显著目标检测（SOD） | multimodal saliency · RGB-T / RGB-D SOD · audio-visual saliency |
| 伪装目标检测（COD） | camouflaged object detection · concealed object detection · RGB-D COD |
| 融合与跨模态表征 | multimodal fusion · cross-modal learning · sensor fusion |
| 对齐与非对齐建模 | alignment · unaligned / misaligned · asynchronous |
| 缺失模态与鲁棒学习 | missing modality · modality completion · uncertainty / robust fusion |
| 多模态检测、分割与跟踪 | multimodal detection · multimodal segmentation · multimodal tracking |
| 视觉语言模型与高效适配 | VLM / MLLM · visual grounding · parameter-efficient adaptation / visual token pruning |

**关注模态：** RGB-T / RGB-D / RGB-NIR / RGB-Event、相机–LiDAR / 雷达、音视频、视觉–语言，以及多光谱/高光谱与其他模态的联合学习。单独使用红外或高光谱不自动等于多模态。

### 2. 多视角与多目标感知

| 子方向 | 代表关键词 |
|---|---|
| 多目标跟踪 | MOT · multi-object tracking · multi-target tracking |
| 多相机与跨相机跟踪 | MTMC · multi-camera tracking · cross-camera association |
| 跨视角匹配与重识别 | cross-view matching · ReID · person / vehicle re-identification |
| 多视角几何与三维感知 | multi-view reconstruction · multi-view stereo · point cloud registration |
| 时空关联与鲁棒感知 | data association · occlusion · identity / temporal consistency |

### 3. 无人机视觉

| 子方向 | 代表关键词 |
|---|---|
| 航拍目标检测 | UAV / aerial detection · small / tiny object · oriented detection |
| 航拍分割与场景理解 | aerial segmentation · UAV scene understanding |
| 跟踪与跨视角检索 | UAV tracking · drone ReID · drone-ground matching |
| 视觉定位、导航与建图 | visual localization / navigation · SLAM · 3D reconstruction |
| 多机协同感知 | multi-UAV perception · cooperative perception |
| 多模态与复杂环境感知 | RGB-thermal UAV · low-light / fog · cross-domain adaptation |

**范围边界：** 遥感不自动等于无人机视觉；纯通信、飞控、无线网络或无视觉贡献的路径规划不在范围内。

### 4. 免训练开放集分割

独立的免训练分割专题。须有明确“不需要下游训练或微调”的证据；零样本、无标注、CLIP 或 SAM 等词本身不足以判定。

| 子方向 | 代表关键词 |
|---|---|
| 免训练开放词汇分割 | training-free open-vocabulary segmentation |
| 免训练开放集／开放世界分割 | training-free open-set segmentation · training-free open-world segmentation |
| 冻结基础模型的分割推理 | frozen CLIP / DINO / SAM · training-free inference |
| 空间与边界细化 | dense features · attention refinement · boundary refinement |
| 上下文、原型与类别校准 | context reasoning · prototype · class calibration |
| 跨域与遥感扩展 | remote sensing · aerial / UAV · cross-domain segmentation |

### 交叉标签示例

| 研究内容 | 归属方向 |
|---|---|
| 无人机 RGB-T 显著目标检测 | 多模态视觉学习＋无人机视觉 |
| 无人机跨相机多目标跟踪 | 多视角与多目标感知＋无人机视觉 |
| 冻结视觉语言模型的免训练航拍开放词汇分割 | 免训练开放集分割＋无人机视觉＋多模态视觉学习 |

标签由标题、已有摘要和日报概括中的明确证据生成。暂时无法确认的论文标记“待归类”，不强制归入多模态；关键词命中只是辅助，不代表单篇论文质量评价。各方向数量相加可超过论文总数。

## 收录与更新

- **刊会准入：** arXiv 通过刊会门槛；其他来源只收录[白名单](./docs/venue-policy.md)中的期刊/会议。不设期刊黑名单，仍检查研究相关性、日期与重复记录。
- **检索来源：** arXiv、OpenAlex、Crossref、Semantic Scholar、IEEE Xplore、Elsevier Scopus、Springer Nature。
- **更新安排：** GitHub Actions 远端执行，不依赖个人电脑。北京时间工作日 03:00 检查；周一补扫上周五及周末，其余工作日查前一天。索引延迟时按现有补查安排继续检查。
- **阅读方式：** 每篇论文对应一张 GitHub Issue 卡片，网页展示刊会简称、已核对的 CCF 等级及可用的开源代码链接。
- **存储原则：** 不长期保存 PDF 或论文源码；元数据来源不下载全文，arXiv 临时分析文件处理后清理。

## 使用与维护

- [研究门户](https://papers.zitalk.cn/) · [论文卡片](https://github.com/zitalk/PaperClaw/issues) · [每日报告](./daily_reports/)
- [配置与维护说明](./docs/operations.md)：远端密钥、更新安排与可选本地调试。
- [方向与子方向配置](./skills/rs-paper-pipeline/scripts/config/research_taxonomy.json)：网页标签、子方向和代表关键词。
- [召回关键词](./skills/rs-paper-pipeline/scripts/config/filter_keywords.json) · [相关性筛选标准](./skills/rs-paper-pipeline/scripts/prompts/filter_cross_prompt.md) · [刊会白名单](./skills/rs-paper-pipeline/scripts/config/venue_policy.json)

## 致谢

本项目起源于 [thinson/RS-PaperClaw](https://github.com/thinson/RS-PaperClaw) 的 Issue 驱动论文追踪思路，并围绕个人视觉研究方向独立重构与扩展。
