<div align="center">
  <img src="./docs/paperclaw-mark.svg" alt="PaperClaw research radar mark" width="132" />

  <h1>PaperClaw</h1>

  <p><strong>A personal paper radar for multimodal vision and UAV research</strong></p>
  <p>Four research directions · Overlapping tags · Daily paper cards</p>

  <p>
    <a href="https://papers.zitalk.cn/"><img src="https://img.shields.io/badge/Research_Portal-Live-0D6B66?style=flat-square" alt="Research portal" /></a>
    <a href="https://github.com/zitalk/PaperClaw/issues"><img src="https://img.shields.io/badge/Paper_Cards-GitHub_Issues-24292F?style=flat-square&logo=github" alt="GitHub Issues" /></a>
    <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+" />
  </p>

  <p><a href="./README.md">中文</a> · <a href="https://papers.zitalk.cn/">Portal</a> · <a href="./daily_reports/">Daily reports</a> · <a href="https://github.com/zitalk/PaperClaw/issues">Paper library</a></p>
</div>

---

PaperClaw tracks new papers across four overlapping research directions. Each paper appears once in the library, with multiple direction and subtopic tags where appropriate.

## Research radar

| Main direction | Subtopics |
|---|---|
| Multimodal visual learning | Salient object detection (SOD); camouflaged object detection (COD); fusion and cross-modal representation; alignment and misalignment; missing-modality robustness; multimodal detection/segmentation/tracking; vision-language models and efficient adaptation |
| Multi-view and multi-object perception | Multi-object tracking; multi-camera tracking; cross-view matching and ReID; multi-view geometry and 3D perception; spatiotemporal association and robustness |
| UAV vision | Aerial object detection; segmentation and scene understanding; tracking and cross-view retrieval; visual localization/navigation/mapping; cooperative perception; multimodal and adverse-condition perception |
| Training-free open-set segmentation | Training-free open-vocabulary segmentation; open-set/open-world segmentation; frozen foundation-model inference; spatial and boundary refinement; context/prototypes/calibration; cross-domain and remote-sensing extensions |

See the [complete subtopic and keyword tables](./README.md#研究雷达) and the [shared taxonomy](./skills/rs-paper-pipeline/scripts/config/research_taxonomy.json).

SOD and COD are task groups within the multimodal research direction; related single-modality work is not thereby claimed to be multimodal. Zero-shot or annotation-free does not automatically mean training-free. Satellite imagery is not automatically UAV vision. Papers without clear classification evidence remain unclassified rather than defaulting to multimodal learning.

## Collection policy

- arXiv papers bypass the venue gate; other sources must match the [explicit venue allowlist](./docs/venue-policy.md). No journal blacklist is used. Date, relevance and deduplication checks still apply.
- Sources: arXiv, OpenAlex, Crossref, Semantic Scholar, IEEE Xplore, Elsevier Scopus and Springer Nature.
- GitHub Actions runs remotely on weekdays. Monday covers the previous Friday through Sunday; other weekdays cover the preceding day. A personal computer does not need to stay online.
- Papers are saved as GitHub Issues and daily reports. Transient arXiv downloads are cleaned after analysis; metadata sources do not download full text.

## Use and configuration

[Portal](https://papers.zitalk.cn/) · [Paper cards](https://github.com/zitalk/PaperClaw/issues) · [Daily reports](./daily_reports/) · [Configuration and maintenance](./docs/operations.md)

## Acknowledgements

PaperClaw originated from the Issue-driven tracking idea in [thinson/RS-PaperClaw](https://github.com/thinson/RS-PaperClaw) and has been independently rebuilt around a personal vision research profile.
