# Daily Reports

最近三天日报（最新在前）：

# [20261006](./202610/20261006.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "ok", "checked_at": "2026-10-07T03:36:59+08:00", "unavailable_sources": [], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成 · 最近检查：2026-10-07 03:36:59（北京时间）

本轮检索候选论文 55 篇；刊会准入通过 0 篇（排除 55 篇）；本轮 LLM 新筛中 0 篇，复用已收录匹配 0 篇；本轮新增入报 0 篇；目标日累计收录 0 篇。当日未检索到符合条件并纳入日报的论文。 

## ✨ 今日亮点

- 留一点时间给思考，好的问题值得耐心打磨。

## 🔎 检索说明

- 日报日期是论文检索目标日期；最近检查时间是任务实际执行时间。
- 零结果不代表所有来源当天没有新论文，只表示本次未纳入符合条件的论文。
- 同一日期后续补扫会更新这份日报，不重复创建日报 Issue。

---

Powered by OpenClaw🦞

---

# [20261005](./202610/20261005.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "partial", "checked_at": "2026-10-06T20:22:39+08:00", "unavailable_sources": ["Semantic Scholar"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，部分来源覆盖受限 · 最近检查：2026-10-06 20:22:39（北京时间）
本轮检索候选论文 136 篇；刊会准入通过 72 篇（排除 64 篇）；本轮 LLM 新筛中 24 篇，复用已收录匹配 0 篇；本轮新增入报 24 篇；目标日累计收录 24 篇。

部分来源不可用：Semantic Scholar；本次结果不代表完整覆盖。 今日论文覆盖3D基础模型、4D世界生成、视频编码、多模态理解与鲁棒感知等方向。研究趋势显示：掩码几何编码与跨视图注意力被用于提升3D鲁棒性；相机控制与时空线索结合推动4D生成一致性；视觉语言模型的空间推理与读出盲区受到关注；噪声标签、部分误标与测试时适应成为鲁棒学习焦点；零样本分割、导航与交互检测继续借助大模型先验。整体上，几何先验、多模态融合与鲁棒性增强是核心主线。

## ✨ 今日亮点

- 掩码几何编码与跨视图注意力提升3D基础模型遮挡鲁棒性
- 相机控制4D生成结合时空线索与几何反射增强一致性
- 视觉语言模型空间推理与读出盲区诊断成为新关注点

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261005] Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models | Shao Zhimin, Liu Xijun, Zhang Zhaoliang, Tang Yutao, Yadav Abhay, Chellappa Rama, Peng Cheng | Department of Electrical and Computer Engineering；Johns Hopkins University；Department of Data Science；University of Virginia；Extracting 3 D concepts from images is a fundamental research problem in computer vision, with | 提出掩码几何编码器，通过减少上下文提升3D基础模型的几何鲁棒性。 | [#821](https://github.com/zitalk/PaperClaw/issues/821) |
| [20261005] ChronoWorld: Camera-Controlled Consistent 4D World Generation via Spatiotemporal Cues and Geometric Reflections | Zhou Xiaoyu, Xian Dingwei, Wang Zhenyu, Xiong Yajiao, Wang Yongtao, Yang Ming-Hsuan | Wangxuan Institute of Computer Technology, Peking University；University of California, Merced | 利用时空线索与几何反射实现相机控制的4D世界一致生成。 | [#822](https://github.com/zitalk/PaperClaw/issues/822) |
| [20261005] Video Encoders Built on Image Representations | Zhang Jusheng, Wang Wenhao, Cai Longqi, Yuan Liangzhe, Wang Yuxiao, Yang Ming-Hsuan | Stanford University；Vast Intelligence Lab | 在图像表示上构建视频编码器，引入跨帧令牌分配与问题感知选择。 | [#823](https://github.com/zitalk/PaperClaw/issues/823) |
| [20261005] A Robust Learning Framework for Deep-Learning-Based Radar Target Detection With Partially Mislabeled Training Data | Zang Chuanfei, Lin Yiru, Wang Yumiao, Chen Xingyu, Yang Xiaobo, Cui Guolong | School of Information and Communication Engineering, University of Electronic Science and Technology of China, Chengdu, China ( | 针对部分误标雷达数据，提出鲁棒学习框架提升目标检测性能。 | [#824](https://github.com/zitalk/PaperClaw/issues/824) |
| [20261005] Lens3D: Target-Conditioned Visual Foveation for Fine-Grained 3D Understanding | Huang Junming, Hou Shuaiying, Chen Zini, Wang Chi, Dai Qiang, Xu Weiwei | Zhejiang University LIGHTSPEED；grounding and question-answering abilities (center) | Lens3D通过目标条件视觉中央凹实现细粒度3D理解与定位。 | [#825](https://github.com/zitalk/PaperClaw/issues/825) |
| [20261005] Analysis of SWIR Imaging Detection Performance Under Adverse Environmental Conditions for Autonomous Driving Systems | Mehra Rohan, Riffard Alexandre, Loumouamou Yannis, Labussière Mathieu | Universit\'e Clermont Auvergne, Clermont Auvergne INP, CNRS, Institut Pascal, F-63000 Clermont-Ferrand, France | 分析短波红外成像在恶劣环境下对自动驾驶目标检测的性能。 | [#826](https://github.com/zitalk/PaperClaw/issues/826) |
| [20261005] VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges | Choi Sungjae, Bae Hanna, Baek Sunghyun, Kim Junmo | Korea Advanced Institute of Science and Technology, South Korea | VGGT-Bridge利用粗步长跳跃边改进长序列位姿图优化。 | [#827](https://github.com/zitalk/PaperClaw/issues/827) |
| [20261005] FrontVeg V2: A Training-Free Software Framework for Foreground-Aware Zero-Shot Plant Trait Segmentation in High-Resolution Images of Trellised Crops | Abdoul Djalil Ousseini Hamza, Metuarea Herearii, Lothodé Corentin, Roth Morgane, Jacem Ben Hamden, Duchêne Eric, Leye Lionel, Alletru David, Rousseau David | 暂无 | FrontVeg V2以无训练框架实现高分辨率棚架作物前景感知零样本分割。 | [#828](https://github.com/zitalk/PaperClaw/issues/828) |
| [20261005] MarvisNav: Making Memory Visible on Route Choices for Zero-Shot Object Navigation | Wang Jincheng, Chi Pui Chan, Zeng Wei, Zhang Shuyang, Jiao Jianhao, Kanoulas Dimitrios | University College London, University of London；China Merchants Group, LionRock AI Lab；Shenzhen University | MarvisNav将探索记忆可视化，用于零样本物体导航的路线选择。 | [#829](https://github.com/zitalk/PaperClaw/issues/829) |
| [20261005] MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks | Kim Eunji, Kim Gahyeon, Cravioto Gianella, Lee Dong-hun, Moon Chaewon, Song Chae-yeong, Park Sang-hyo | School of Computer Science and Engineering；Kyungpook National University, Daegu, Republic of Korea；object reconstruction, recent 3 D Gaussian Splatting (3 DGS) [20] research has | MaRO-GS从不一致多视图掩码中实现鲁棒对象中心高斯泼溅重建。 | [#830](https://github.com/zitalk/PaperClaw/issues/830) |
| [20261005] Harnessing Multimodal Large Language Models for Training-Free Human-Object Interaction Detection | Cai Zhaolin, Duan Huiyu, Yang Liu, Qin Yanjun, Ai Bo, Chen Wei, Min Xiongkuo, Zhai Guangtao | Shanghai Jiao Tong University；Xinjiang University；Beijing Jiaotong University；Shanghai AI Laboratory | 利用多模态大语言模型实现免训练的人-物交互检测。 | [#831](https://github.com/zitalk/PaperClaw/issues/831) |
| [20261005] MTOR: Generalizable AI-Generated Video Detection with Multimodal Semantics and Temporal Over-Regularity | Wang Hang, Shen Chao, Zhang Lei, Cheng Zhi-Qi | Xi’an Jiaotong University, Xi’an, China, and The Hong Kong Polytechnic University, Hong Kong, China (；Xi’an Jiaotong University, Xi'an, China (；The Hong Kong Polytechnic University, Hong Kong, China (；the Language Technologies Institute, Carnegie Mellon University, Pittsburgh, PA, USA ( | MTOR结合多模态语义与时间过规则性检测AI生成视频。 | [#832](https://github.com/zitalk/PaperClaw/issues/832) |
| [20261005] Readout Blindness: VLM Scores Miss the Spatial Direction Their Frozen Encoders Retain | Li Guangyuan, Du Tianming, Jiang Yan, Wen Bihan, Yang Jiancheng | ELLIS Institute Finland；Aalto University；University of Oulu；Nanyang Technological University | 揭示视觉语言模型评分忽略冻结编码器保留的空间方向信息。 | [#833](https://github.com/zitalk/PaperClaw/issues/833) |
| [20261005] LeAVJEPA: A Minimalist Architecture for Audio-Visual Self-Supervised Learning | Robson Benjamin, Mentu Santeri, Zhao Wenshuai, Solin Arno | ELLIS Institute Finland Aalto University；ELLIS Institute Finland and Department of Computer Science；Aalto University | LeAVJEPA以极简架构实现音频-视觉自监督跨模态对齐。 | [#834](https://github.com/zitalk/PaperClaw/issues/834) |
| [20261005] Towards Quadruped-Provided Localization and Active Tracking for Micro-UAVs | Alejandro Lorite Mora, Faíña Andrés | IT University of Copenhagen, Rued Langgaards Vej 7, Copenhagen 2300, Denmark；Helix Lab, Campus Kalundborg 3 | 探索四足机器人提供定位与主动跟踪微型无人机的方法。 | [#835](https://github.com/zitalk/PaperClaw/issues/835) |
| [20261005] Efficient Test-time Adaptation through Candidate Verification and Divergence Shifts | Oh Seungmin, Kang Seunghun, Ryu Jongbin | Ajou University | 通过候选验证与散度偏移实现高效测试时适应。 | [#836](https://github.com/zitalk/PaperClaw/issues/836) |
| [20261005] Prompt and Refinement: Asymmetric Mutual Learning for Infrared Small Target Detection with Noisy Labels | Fu Yimin, Wang Songbo, Liu Lizhuo, Pan Baicheng, Liu Zhunga, Michael K. Ng | Department of Mathematics, Hong Kong Baptist University, Hong Kong, China (；School of Automation, Northwestern Polytechnical University, Xi'an,, China (；School of Electrical and Control Engineering, Xi'an University of Science and Technology, Xi'an,, China ( | 提出提示与精炼的非对称互学习，应对红外小目标噪声标签。 | [#837](https://github.com/zitalk/PaperClaw/issues/837) |
| [20261005] Every View Counts: View-Consistent Panoptic Quality for Multi-view Panoptic Segmentation | Lee Youngmin, Ko Byungha, Yun Guhnoo, Dong Hwan Kim | Korea University；Korea Institute of Science and Technology | 提出视图一致全景质量指标，用于多视图全景分割评估。 | [#838](https://github.com/zitalk/PaperClaw/issues/838) |
| [20261005] AstraSR: Real-World Thermal Super-Resolution with GPT-6 Astra | Li Mengyuan, Fu Changhong, Zhang Jun, Lu Ziyu, Zhang Yuhang, Zuo Haobo | School of Mechanical Engineering, Tongji University, Shanghai, China；School of Electrical and Electronic Engineering, Nanyang Technological University, Singapore；School of Computing and Data Science, the University of Hong Kong, Hong Kong, China | AstraSR利用GPT-6 Astra实现真实世界热成像超分辨率。 | [#839](https://github.com/zitalk/PaperClaw/issues/839) |
| [20261005] Fitting Vision Adapters at Frontier Scales | Lee Jaehoon, Partridge Harry, Jayasekara Mudith, O’Neill Charles, Kirkby Max, Psenka Michael | Base Labs | 研究前沿规模下视觉适配器的拟合与缩放规律。 | [#840](https://github.com/zitalk/PaperClaw/issues/840) |
| [20261005] OGAM: Connecting Systematic Testing to Runtime Assurance through Object-Grounded Attention Monitoring for VLA Policies | Darwish Haki, Yin Xiangyu, Li Changwen, Yan Rongjie, Francisco Gomes de Oliveira Neto, Cheng Chih-Hong | Carl von Ossietzky University of Oldenburg, Germany；was conducted during his service at Chalmers University of Tech- by instruction role: the named objects, the strongest；Institute of Software, Chinese Academy of Science, China；Chalmers University of Technology, Sweden | OGAM通过对象接地注意力监控连接系统测试与运行时保障。 | [#841](https://github.com/zitalk/PaperClaw/issues/841) |
| [20261005] Rotated, but How Far? Diagnosing and Improving Object-Rotation Reasoning in VLMs | Wang Zhaochen, Cai Yujun, Zou Huangbo, Yang Hower, Dong Naipeng, Xu Miao, Ling Haibin | University of Queensland；Westlake University | 诊断并改进视觉语言模型中的物体旋转推理能力。 | [#842](https://github.com/zitalk/PaperClaw/issues/842) |
| [20261005] Bayesian Data Augmentation for DNN Retraining with Binomial Outcomes in Vision-Based UAV Landing | Ashik E Rasul, Yoon Hyung-Jin | Department of Mechanical and Nuclear Engineering；Tennessee Technological University | 贝叶斯数据增强用于二项结果下无人机视觉着陆的DNN重训练。 | [#843](https://github.com/zitalk/PaperClaw/issues/843) |
| [20261005] StageVLN: Spatial and Trajectory Auxiliary Guidance for Efficient Vision-Language Navigation | Dao Anh, Pham Quan-Dung, Le Danh Vinh, The Anh Nguyen, Nguyen Viet Tri Pham, Chen Yiyu, Pham Tuyen Le, Nguyen Van-Truong, Nguyen Quan | University of Southern California, USA | StageVLN引入空间与轨迹辅助引导提升视觉语言导航效率。 | [#844](https://github.com/zitalk/PaperClaw/issues/844) |

## 🔎 观察

- 3D与4D生成研究正从单纯增加上下文转向几何先验与掩码策略，以提升鲁棒性与一致性。
- 视觉语言模型的空间推理短板被多篇论文从读出机制与旋转推理角度诊断并改进。

---

Powered by OpenClaw🦞

---

# [20261004](./202610/20261004.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "partial", "checked_at": "2026-10-05T20:17:42+08:00", "unavailable_sources": ["IEEE Xplore"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，部分来源覆盖受限 · 最近检查：2026-10-05 20:17:42（北京时间）

本轮检索候选论文 56 篇；刊会准入通过 0 篇（排除 56 篇）；本轮 LLM 新筛中 0 篇，复用已收录匹配 0 篇；本轮新增入报 0 篇；目标日累计收录 0 篇。当日未检索到符合条件并纳入日报的论文。 部分来源不可用：IEEE Xplore；本次结果不代表完整覆盖。

## ✨ 今日亮点

- 研究的进展，常常藏在持续积累的每一个小步里。

## 🔎 检索说明

- 日报日期是论文检索目标日期；最近检查时间是任务实际执行时间。
- 零结果不代表所有来源当天没有新论文，只表示本次未纳入符合条件的论文。
- 同一日期后续补扫会更新这份日报，不重复创建日报 Issue。

---

Powered by OpenClaw🦞

---
