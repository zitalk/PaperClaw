# 刊会准入名单

生效：2026-09-04。按研究兴趣维护的视觉 / AI / 遥感 / 机器人白名单，**不是全部 CCF 目录，也不是对单篇论文质量的保证**。

## 规则

1. Scientific Reports、Engineering Research Express、IEEE Access、Sensors（MDPI）、Applied Sciences（MDPI）明确排除。匹配正式刊名、别名及期刊专属 DOI，不扫描摘要中的普通单词；不误删 IEEE Sensors Journal 或 Sensors and Actuators。
2. 真实 arXiv ID/链接免于刊会白名单，但已确认发表在上述排除期刊的同一论文仍排除。日期、方向相关性与去重不豁免。
3. 其他正式发表论文需命中下表。未知刊会、未列入刊会暂不纳入；不会凭数据库名称、关键词或 LLM 猜测放行。
4. 会议 Workshop、Demo、Companion、摘要集不继承主会准入。普通主会正式论文（含 poster）不因展示形式被排除。
5. 刊会门槛在 LLM 前执行；运行日志及统计 JSON 记录每篇排除原因，日报显示准入 / 排除计数。无准入候选不调用筛选 LLM。
6. 不自动放行所有“一区”或所有 IEEE Transactions。KBS、ESWA、PR 明确纳入；ESWA 是 Expert Systems with Applications，不是另一本 Expert Systems。

## 名单

CCF 等级参考 [CCF 第七版目录（2026 年）](https://www.ccf.org.cn/Academic_Evaluation/By_category/)。空白表示本项目未标注 CCF 等级，不代表对该刊会的负面判断。名单由 `skills/rs-paper-pipeline/scripts/config/venue_policy.json` 管理；增删时同时维护别名和测试。

| 简称 | 期刊 / 会议 | CCF |
|---|---|---|
| TPAMI | IEEE Transactions on Pattern Analysis and Machine Intelligence | A |
| IJCV | International Journal of Computer Vision | A |
| TIP | IEEE Transactions on Image Processing | A |
| TMM | IEEE Transactions on Multimedia | A |
| TVCG | IEEE Transactions on Visualization and Computer Graphics | A |
| JMLR | Journal of Machine Learning Research | A |
| TCSVT | IEEE Transactions on Circuits and Systems for Video Technology | B |
| TNNLS | IEEE Transactions on Neural Networks and Learning Systems | B |
| TCYB | IEEE Transactions on Cybernetics | B |
| PR | Pattern Recognition | B |
| CVIU | Computer Vision and Image Understanding | B |
| TOMM | ACM Transactions on Multimedia Computing, Communications, and Applications | B |
| TGRS | IEEE Transactions on Geoscience and Remote Sensing | B |
| T-RO | IEEE Transactions on Robotics | B |
| TASE | IEEE Transactions on Automation Science and Engineering | B |
| TITS | IEEE Transactions on Intelligent Transportation Systems | B |
| GRSL | IEEE Geoscience and Remote Sensing Letters | C |
| TII | IEEE Transactions on Industrial Informatics | C |
| KBS | Knowledge-Based Systems | C |
| ESWA | Expert Systems with Applications | C |
| Inf Fusion | Information Fusion | — |
| ISPRS JPRS | ISPRS Journal of Photogrammetry and Remote Sensing | — |
| RA-L | IEEE Robotics and Automation Letters | — |
| IJRR | The International Journal of Robotics Research | — |
| TIM | IEEE Transactions on Instrumentation and Measurement | — |
| TIE | IEEE Transactions on Industrial Electronics | — |
| T-IV | IEEE Transactions on Intelligent Vehicles | — |
| CVPR | IEEE/CVF Conference on Computer Vision and Pattern Recognition | A |
| ICCV | IEEE/CVF International Conference on Computer Vision | A |
| ACM MM | ACM International Conference on Multimedia | A |
| NeurIPS | Advances in Neural Information Processing Systems | A |
| ICML | International Conference on Machine Learning | A |
| ICLR | International Conference on Learning Representations | A |
| AAAI | AAAI Conference on Artificial Intelligence | A |
| ECCV | European Conference on Computer Vision | B |
| ICRA | IEEE International Conference on Robotics and Automation | B |
| IJCAI | International Joint Conference on Artificial Intelligence | B |
| ICME | IEEE International Conference on Multimedia and Expo | B |
| ICASSP | IEEE International Conference on Acoustics, Speech and Signal Processing | B |
| IROS | IEEE/RSJ International Conference on Intelligent Robots and Systems | C |
| BMVC | British Machine Vision Conference | C |
| ACCV | Asian Conference on Computer Vision | C |
| ICIP | IEEE International Conference on Image Processing | C |
| PRCV | Chinese Conference on Pattern Recognition and Computer Vision | C |
| WACV | IEEE/CVF Winter Conference on Applications of Computer Vision | — |
| RSS | Robotics: Science and Systems | — |
| CoRL | Conference on Robot Learning | — |

## 历史清理范围

2026-09-04 仅追溯移除上述五个指定期刊：删除 5 张卡片（Engineering Research Express 4 篇、Scientific Reports 1 篇），同步清理索引、日报条目、相关亮点与失败候选引用。其他三刊未发现已收录卡片；其余历史论文保留，新白名单用于后续检索。

原始候选 / LLM 匹配数保留，最终纳入数反映清理后的列表。Git 历史提交不改写；删除前的 Issue JSON 与日报快照只备份在本机，不发布到网站。GitHub Issue 删除后不能恢复原编号。
