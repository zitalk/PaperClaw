# Daily Reports

最近三天日报（最新在前）：

# [20260903](./202609/20260903.md)
## 📌 今日概况

今日共检索候选论文 57 篇；关键词+LLM 智能匹配研究方向论文 7 篇；最终纳入日报 3 篇（原收录 5 篇，按期刊排除规则移除 2 篇；候选与匹配数保留原运行统计）。

清理后保留的论文涉及空中目标跟踪、无人机检测与海上搜索任务：包括 GRU 与卡尔曼滤波的混合跟踪策略、星增强跨尺度对齐方法，以及结合模型预测控制与 CNN 目标检测的海上搜索框架。

## ✨ 今日亮点

- 星增强跨尺度对齐方法缓解无人机检测中的表征脆弱性问题。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260903] Разработка гибридного модуля сопровождения воздушных объектов на основе GRU и фильтра Калмана | Е. Ю. Фелагерева, Н. Р. Рудоман, А. Д. Новиков | 暂无 | 提出GRU与卡尔曼滤波混合模块，用于空中目标跟踪与轨迹预测。 | [#43](https://github.com/zitalk/PaperClaw/issues/43) |
| [20260903] Seeing the unseen: overcoming representational fragility in UAV detection with star-enhanced cross-scale alignment | Cai Hao, Xu Jingxuan, Zhang Jinhong, Ouyang Zhong, Liu Jiafu, Zhang Yi, Yang Qin | 暂无 | 提出星增强跨尺度对齐方法，缓解无人机小目标检测中的表征脆弱性问题。 | [#46](https://github.com/zitalk/PaperClaw/issues/46) |
| [20260903] A Framework for Fast and Reliable UAV Maritime Search Missions | Anastasiou Andreas, Papaioannou Savvas, Kolios Panayiotis, Christos G. Panayiotou | 暂无 | 构建结合模型预测控制与CNN目标检测的无人机海上搜索快速可靠框架。 | [#47](https://github.com/zitalk/PaperClaw/issues/47) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。可通过来源链接查看原文。

| 标题 | 来源 | 失败原因 |
|------|-------|----------|
| LSO-YOLO: a lightweight real-time object detection network for UAV small-object detection | [doi:10.1007/s11554-026-01977-y](https://doi.org/10.1007/s11554-026-01977-y) | 质检未通过: 摘要为空或无效 |
| Precise small unmanned aerial vehicle target detection model ATU-Net | [doi:10.1007/s11554-026-01976-z](https://doi.org/10.1007/s11554-026-01976-z) | 质检未通过: 摘要为空或无效 |


## 🔎 观察

- 保留论文分别关注无人机检测、目标跟踪与海上搜索；本次整理仅执行指定期刊排除，不对其余历史论文追溯应用新白名单。
- 跟踪与检测方法出现融合趋势，如GRU与卡尔曼滤波结合，反映对时序一致性和预测稳定性的重视。

---

Powered by OpenClaw🦞

---

# [20260902](./202609/20260902.md)
## 📌 今日概况

今日共检索候选论文 143 篇；关键词+LLM 智能匹配研究方向论文 17 篇；最终纳入日报 14 篇（原收录 17 篇，按期刊排除规则移除 3 篇；候选与匹配数保留原运行统计）。

今日论文覆盖无人机视觉、多模态理解与鲁棒性评估等方向。研究重点包括：面向真实部署的LiDAR语义分割鲁棒性评估、流式视频理解中的视觉token剪枝、RGB到红外图像转换以提升无人机车辆检测、多鱼眼全景感知平台、以及基于MLLM的指称多目标跟踪。此外，生成式图像编辑用于域偏移鲁棒目标检测、雷达Transformer运动检测、旋转诱导显著性漂移审计、多光谱与SAR图像理解、海事3D船舶检测、缺失模态适应、无人机小目标检测及医学图像分割等方向均有涉及，整体呈现从感知精度向部署鲁棒性与计算效率延伸的趋势。

## ✨ 今日亮点

- LiDAR语义分割鲁棒性评估覆盖粗标签、恶劣条件与域偏移，推动真实部署。
- ShallowStream通过浅层索引与深层回答策略，显著提升流式视频理解效率。
- 多鱼眼全景感知平台实现超低空无人机无死角环境建模与视差感知。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260902] Toward Robust LiDAR Semantic Segmentation for Real-World Deployment: Evaluation under Coarse Labels, Adverse Conditions, and Domain Shifts | Samir Abou Haidar, Chariot Alexandre, Darouich Mehdi, Joly Cyril, Deschaud Jean-Emmanuel | remains largely centered on standard train/val/test splits of；sity, Centre for Robotics (CAOR)；The authors are with Paris-Saclay University, CEA, List, F-91120, Robustness evaluation measures model performance un- | 评估LiDAR语义分割在粗标签、恶劣条件与域偏移下的鲁棒性，面向真实自动驾驶部署。 | [#25](https://github.com/zitalk/PaperClaw/issues/25) |
| [20260902] ShallowStream: Index Shallow then Answer Deep for Streaming Video Understanding | Hao Jitai, Yang Ke, Huang Qiang, Yu Jun | Harbin Institute of Technology (Shenzhen) | 提出先浅层索引后深层回答的流式视频理解方法，降低视觉token与KV缓存开销。 | [#26](https://github.com/zitalk/PaperClaw/issues/26) |
| [20260902] RGB-to-IR image translation for infrared vehicle detection in unseen UAV domains | Thijs A. Eker, Ella P. Fokkinga, Jan Erik van Woerden, Elfi I. S. Hofmeijer, Sebastiaan P. Snel, Schutte Klamer, Friso G. Heslinga | TNO - Intelligent Imaging | 利用RGB到红外图像转换生成合成数据，提升无人机平台红外车辆检测泛化能力。 | [#27](https://github.com/zitalk/PaperClaw/issues/27) |
| [20260902] From Multi-Fisheye Sensing to Panoramic Perception: A Parallax-Aware Onboard Platform for Ultra-Low-Altitude UAVs | Dai Dun, Lu Ze, He Cheng, Wang Yaowen, Quan Quan | School of Automation Science and Electrical Engineering, Beihang University, Beijing, China (；the Tianmushan Laboratory, Hangzhou, China (；School of Automation Science and Electrical Engineering, Beihang University, Beijing, China | 构建视差感知的多鱼眼机载平台，实现超低空无人机全景感知与等距柱状全景生成。 | [#28](https://github.com/zitalk/PaperClaw/issues/28) |
| [20260902] YesTrack: Referring Multi-Object Tracking via MLLM-based Yes/No Verification | Hu Quansheng, Sun Qin, Dai Qiansen, Ding Jin, Zhang Wan, Zhou Xue, Zou Jianxiao | University of Electronic Science and Technology of China, Chengdu, China；Shenzhen Institute for Advanced Study, UESTC, Shenzhen, China | 基于MLLM的是非验证机制实现指称多目标跟踪，增强时序一致性与参考传播。 | [#29](https://github.com/zitalk/PaperClaw/issues/29) |
| [20260902] Domain shift-robust object detection with GenAI image editing | Isabel D. Stein, Thijs A. Eker, Sebastiaan P. Snel, Ella P. Fokkinga, Schutte Klamer, Ambrogioni Luca, Friso G. Heslinga | Radboud University, Nijmegen, the Netherlands | 采用生成式图像编辑进行数据增强，提升目标检测模型对域偏移的鲁棒性。 | [#30](https://github.com/zitalk/PaperClaw/issues/30) |
| [20260902] If It Moves, Radar Knows: A Physics-Aware Radar Transformer for Class-Agnostic Moving-Object Detection | Sun Yinghao, Li Shuguang, Shao Jinliang, Li Tieshan | School of Automation Engineering of the University of Electronic Science and Technology of China (UESTC), Chengdu, Sichuan, P | 提出物理感知雷达Transformer，利用多普勒运动线索实现类别无关的运动目标检测。 | [#31](https://github.com/zitalk/PaperClaw/issues/31) |
| [20260902] Signal or Noise? Auditing Rotation-Induced Saliency Drift in Medical and Aerial Imaging | Khawaja Murad ul Hassan, Ebrahimi Mehran | Independent Researcher；Ontario Tech University | 审计医学与航拍图像中旋转引起的显著性漂移，揭示Grad-CAM等方法的旋转等变性缺陷。 | [#32](https://github.com/zitalk/PaperClaw/issues/32) |
| [20260902] Lightweight Adaptation of General-Purpose VLMs for Multispectral and SAR Image Understanding | Liu Shanji, Yao Kelu, Xue Junxiao, Lv Chenghui, Miao Xiangyang, Huang Yekai, Chen Yaying, Li Chao | Zhejiang University；Zhejiang Lab | 通过轻量级适配将通用视觉语言模型扩展至多光谱与SAR图像理解任务。 | [#33](https://github.com/zitalk/PaperClaw/issues/33) |
| [20260902] KSG-Net: Key-Sparse and Global-Context Learning for Maritime 3D Ship Detection | Huai Zhouyuan, Wan Meiqi, Yang Yan, Chen Minshi, Yuan Xin, Wang Wei, Wang Xiao | School of Computer Science and Technology, Wuhan University of Science and；Hubei Province Key Laboratory of Intelligent Information Processing and；Real-Time Industrial System, Wuhan University of Science and Technology, Wuhan；State Key Laboratory of Robotics and Intelligent Systems, Shenyang Institute of；Automation, Chinese Academy of Sciences, Shenyang 110016, China；China University of Chinese Academy of Sciences, Beijing 100049, China | 提出关键稀疏与全局上下文学习网络，提升海事场景LiDAR点云3D船舶检测性能。 | [#34](https://github.com/zitalk/PaperClaw/issues/34) |
| [20260902] Test-Time Logit Prompting for Source-Free Missing Modality Adaptation | Chen Taixi, Guo Nancy | School of Computing；State University of New York at Binghamton | 在测试时利用logit提示实现无源缺失模态适应，增强视觉语言模型鲁棒性。 | [#35](https://github.com/zitalk/PaperClaw/issues/35) |
| [20260902] Stereo 4D Radar for 3D Object Detection: Integrating Geometric Alignment and Absolute Velocity Estimation | Song Seung-Hyun, Paek Dong-Hee, Byun Woong-Chan, Kong Seung-Hyun | Graduate School of Mathematics, Nagoya University, Nagoya, Japan；the Faculty of Informatics, Shizuoka University, Hamamatsu, Shizuoka, Japan | 融合几何对齐与绝对速度估计，利用立体4D雷达实现3D目标检测。 | [#40](https://github.com/zitalk/PaperClaw/issues/40) |
| [20260902] TempoGround: State-Aware Streaming Visual Grounding with Vision-Language Models | Ding Leqian, Qiu Junning, Yang Manwen, Guo Yu, Wang Fei | Xi’an Jiaotong University, Xi’an, China | 提出状态感知的流式视觉定位方法，利用视觉语言模型处理连续视频流中的目标对应。 | [#41](https://github.com/zitalk/PaperClaw/issues/41) |
| [20260902] InstEditSeg: Instruction-Driven Image Editing for Polyp and Skin Lesion Segmentation | Liu Ziquan, Zhu Zhewei, Shi Xuyang | School of Information and Control Engineering, Southwest University of Science and Technology, Mianyang 621010, China | 通过指令驱动的图像编辑提升息肉与皮肤病变分割性能，结合扩散模型进行数据增强。 | [#42](https://github.com/zitalk/PaperClaw/issues/42) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。可通过来源链接查看原文。

| 标题 | 来源 | 失败原因 |
|------|-------|----------|
| Paddy parcel detection method using drone images based on YOLO-Seg model and tiling movement | [doi:10.1007/s10333-026-01092-5](https://doi.org/10.1007/s10333-026-01092-5) | 质检未通过: 摘要为空或无效 |


## 🔎 观察

- 无人机视觉研究呈现从单一传感器向多传感器融合与全景感知演进的趋势，同时强调小目标检测与域偏移鲁棒性。
- 多模态大模型在流式视频理解、指称跟踪与缺失模态适应等任务中持续渗透，效率优化与轻量化适配成为关键方向。

---

Powered by OpenClaw🦞

---

# [20260901](./202609/20260901.md)
## 📌 今日概况

今日共检索候选论文 75 篇；关键词+LLM 智能匹配研究方向论文 17 篇；最终纳入日报 17 篇。

今日论文聚焦无人机视觉与多模态学习两大主线。无人机方向涵盖GPS退化环境下的编队控制、多模态大模型操控、在线三维重建及事件相机预测，显示从感知向决策与重建延伸。多模态方向则集中于视觉token剪枝、CLIP模态鸿沟分析及文本引导融合，强调效率与可解释性。此外，野火分割、红外小目标检测等任务呈现多模态融合与文本引导趋势，整体研究注重鲁棒性、轻量化与跨模态对齐。

## ✨ 今日亮点

- 多模态大模型被评估为无人机通用视觉-语言-动作智能体，覆盖指挥、接近、跟踪与搜索任务。
- S$^2$Prune与SinkPruner分别从空间覆盖和注意力汇角度提出视觉token剪枝方法，提升MLLM推理效率。
- On-the-Fly3R面向大规模无人机场景，利用前馈3R模型实现无序图像流的鲁棒在线三维重建。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260901] Vision-Based Leader-Follower Formation Control for Cooperative UAVs in GPS-Degraded Environments | Angadi Deekshitha, Budda Naveena, Agarwal Vikas, Rojesh Arunkumar Mulasa, Killamsetty Ravi, Samshad Mohamed, Kemsaram Narsimlu | AI, IoT and Robotics Lab (AIR Lab), UAVs Group, Autonomous Robotics Systems Limited, Hyderabad, India；Department of Microelectronics and VLSI Design, University of Hyderabad, Hyderabad, India；Department of Internet of Things, Ideabytes Software India Private Limited, Hyderabad, India；School of Computer Science, Georgia Institute of Technology, Atlanta, USA；Department of Electrical Engineering, Indian Institute of Technology, Kanpur, India；Department of Artificial Intelligence, University of Malaya, Kuala Lumpur, Malaysia | 提出基于视觉的领航-跟随编队控制方法，利用RGB-D感知在GPS退化环境中实现多无人机协同。 | [#1](https://github.com/zitalk/PaperClaw/issues/1) |
| [20260901] Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching | Park Jaewoo, Lee Minyoung, Seo Sukmin, Yim Moonbin, Yoon Hyunwook, Ryu Dohoon, Kim Daehee, Song Myungseo, Byun Jihyuk, Chang Seunggyu, Kil Taeho, Kim Jiseob, Lee Bado, Kim Geewook | NAVER Cloud | 系统评估多模态大模型作为无人机控制智能体的能力，覆盖指挥、接近、跟踪与搜索四类任务。 | [#2](https://github.com/zitalk/PaperClaw/issues/2) |
| [20260901] Scale-based Approach for Active Wildfire Segmentation on Satellite Imagery | Matheus F. Kovaleski, Premebida Cristiano, João Ruivo Paulo | ∗ Institute of Systems and Robotics, Department of Electrical and Computer Engineering, University of Coimbra, Portugal；detection and monitoring, recent research has also explored | 提出基于尺度的主动野火分割方法，在Landsat-8卫星影像上利用U-Net进行深度学习分割。 | [#3](https://github.com/zitalk/PaperClaw/issues/3) |
| [20260901] Multimodal RGB-Infrared Combination for UAV-Based Wildfire Segmentation: A Comparative Study on FLAME3 | Matheus F. Kovaleski, Garrote Luís, Premebida Cristiano, Mendes Jérôme, João Ruivo Paulo | Institute of Systems and Robotics, Department of Electrical and Computer Engineering, University of Coimbra, Portugal；University of Coimbra, CEMMPRE, ARISE, Department of Mechanical Engineering, Polo II, PT-3030-788 Coimbra, Portugal | 在FLAME3数据集上比较RGB与红外多模态融合策略，用于无人机视角的野火分割任务。 | [#4](https://github.com/zitalk/PaperClaw/issues/4) |
| [20260901] S$^2$Prune: Spatially Structured Visual Token Pruning for Multimodal Large Language Models | Jia Yuanyuan, Tang Shunpu, Yang Qianqian | College of Information Science and Electronic Engineering, Zhejiang University | 提出空间结构化的视觉token剪枝方法，通过拉普拉斯变化保持空间覆盖并提升多模态大模型效率。 | [#5](https://github.com/zitalk/PaperClaw/issues/5) |
| [20260901] When Modality Gap Reduction Fails: Prediction-Level Hubness in CLIP | Sato Shota, Kiyama Hajime, Hirasawa Tosho, Komachi Mamoru | Hitotsubashi University | 分析CLIP中模态鸿沟缩减失败时的预测级hubness现象，揭示零样本分类中的跨模态对齐问题。 | [#6](https://github.com/zitalk/PaperClaw/issues/6) |
| [20260901] IT-TextFusion: Iterative Text-Image Interaction with Text-Guided Residual Refinement for Degradation-Aware Image Fusion | Liu Siyang, Zhou Peiyi, Jin Tianle, Bian Rongrong, Jin Zheke, Gao Mengze | School of Automation, Southeast University, Nanjing, China；Chair of Robotics, Artificial Intelligence and Real-time Systems, Technical University of Munich | 提出迭代式文本-图像交互融合网络，利用文本引导残差细化实现退化感知的图像融合。 | [#7](https://github.com/zitalk/PaperClaw/issues/7) |
| [20260901] Adaptive Depth-Map-Guided Bundle Adjustment for Correspondence-Free Multi-View Point Cloud Registration | Zhou Yiran, Wang Yingyu, Huang Shoudong, Zhao Liang | the Robotics Institute, Faculty of Engineering and Information Technology, University of Technology Sydney,Sydney, NSW, Australia (；School of Informatics, The University of Edinburgh, Edinburgh EH8 9 AB, U.K. ( | 提出自适应深度图引导的束调整方法，实现无对应关系的多视角点云配准。 | [#8](https://github.com/zitalk/PaperClaw/issues/8) |
| [20260901] Lightweight Interpretable RGB-Guided Hyperspectral Super-Resolution under Real Cross-resolution Misalignment | Jouni Mohamad, Godet Aurélien, Mauro Dalla Mura | Grenoble INP, GIPSA-Lab | 提出轻量可解释的RGB引导高光谱超分辨率方法，处理真实跨分辨率未对齐问题。 | [#9](https://github.com/zitalk/PaperClaw/issues/9) |
| [20260901] SinkPruner: Sink-Free Visual Token Pruning for Multimodal Large Language Models | Li Shiyu, Hu Zi-Yuan, Huang Shijia, Li Yanyang, Zhong Yiwu, Wang Liwei | The Chinese University of Hong Kong；Peking University | 提出无汇视觉token剪枝方法，通过去除高范数离群点实现免训练的多模态大模型推理加速。 | [#10](https://github.com/zitalk/PaperClaw/issues/10) |
| [20260901] Beyond the Image Plane: World-Grounded Queries for Multi-Object Tracking | Cetintas Orcun, Brasó Guillem, Meinhardt Tim, Leal-Taixé Laura | Technical University of Munich | 提出世界坐标系锚定的查询机制，利用单目视频实现超越图像平面的多目标跟踪。 | [#11](https://github.com/zitalk/PaperClaw/issues/11) |
| [20260901] On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios | Shen Zhe, Lou Liyuan, Yu Yifei, Wang Guanbo, Ji Quanjian, Wang Xin, Zhan Zongqian | School of Geodesy and Geomatics, Wuhan University, Wuhan 430079, China | 提出基于前馈3R模型的在线三维重建方法，面向大规模无人机场景处理无序图像流。 | [#12](https://github.com/zitalk/PaperClaw/issues/12) |
| [20260901] ADGNet: Asymmetric Dual-text Guided Network for Infrared Small Target Detection | Wang Tongtong, Xu Mingzhu, Yu Chenglong, Wang Jing, Lin Xiaohui, Guan Weili | Shandong University Jinan China；Harbin Institute of Technology, Shenzhen Shenzhen China | 提出非对称双文本引导网络，通过双分支交互实现红外小目标检测的语义建模。 | [#13](https://github.com/zitalk/PaperClaw/issues/13) |
| [20260901] Residual Kalman Dynamics for Event-Based UAV Forecasting | Nyblom Per, Ovrén Hannes, Gustafsson David | Swedish Defence Research Agency (FOI), Linköping, Sweden；Kalman filter over a full center-size box state as a strong physical baseline, and train a residual model to predict acceleration-like corrections | 结合卡尔曼滤波与残差学习，利用事件相机实现无人机边界框预测的动力学建模。 | [#14](https://github.com/zitalk/PaperClaw/issues/14) |
| [20260901] Feed-Forward Multi-view Multi-person Reconstruction with Contrastive Human-Aware 3D Representation | Yang Yuanwang, Huang Buzhen, Ren Zongxuan, Huang Jing, Li Kun | College of Intelligence and Computing, Tianjin University | 提出前馈多视角多人重建方法，利用对比学习的人体感知三维表示实现免优化重建。 | [#15](https://github.com/zitalk/PaperClaw/issues/15) |
| [20260901] DGNet: Dual-knowledge Guided Network for Infrared Small Target Detection | Yu Chenglong, Xu Mingzhu, Wang Jing, Wang Tongtong, Miao Pingping, Nie Liqiang | Shandong University Jinan China；Harbin Institute of Technology, Shenzhen Shenzhen China | 提出双知识引导网络，通过语义解耦与小波调制实现文本引导的红外小目标检测。 | [#16](https://github.com/zitalk/PaperClaw/issues/16) |
| [20260901] Restrict, Don't Retrain: Inference-Time VLM Guidance for Zero-Shot Aerial Segmentation | DiMeola Teresa, Walter Charles, Xiao Hong | University of Mississippi | 提出推理时视觉语言模型引导方法，无需重训练即可实现零样本航空影像分割。 | [#17](https://github.com/zitalk/PaperClaw/issues/17) |

## 🔎 观察

- 多模态大模型在无人机控制中的评估表明，视觉-语言-动作智能体正从仿真走向真实任务验证，但通用性与鲁棒性仍需系统基准测试。
- 视觉token剪枝成为多模态大模型效率优化的热点，空间覆盖与注意力汇等不同视角的方法并行发展，反映推理成本与性能平衡的持续探索。

---

Powered by OpenClaw🦞

---
