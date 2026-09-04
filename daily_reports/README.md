# Daily Reports

最近三天日报（最新在前）：

# [20260903](./202609/20260903.md)
## 📌 今日概况

今日共检索候选论文 119 篇；刊会准入通过 61 篇（排除 58 篇）；关键词+LLM 智能匹配研究方向论文 13 篇；最终纳入日报 13 篇。

今日研究集中于三维场景理解与多模态空间推理，涵盖在线三维重建、世界模型、视频生成与视觉语言导航等方向。多篇工作强调将3D几何先验、拓扑图或八叉树结构融入学习框架，以提升空间一致性与长程推理能力。同时，弱监督视频理解、流式记忆演化及跨模态融合方法持续演进，显示从静态感知向动态、可扩展、物理一致的场景建模转变。

## ✨ 今日亮点

- Scal3R提出多相对位姿查询，提升在线三维重建的可扩展性与回环能力。
- Puffin-World构建原生三维世界状态的统一多模态模型，强化空间与物理仿真。
- OctWorld利用八叉树三维映射实现长程世界一致的视频生成。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260903] Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction | Lin Chin-Yang, Sun Yang-Che, Sun Cheng, Yang Fu-En, Chen Min-Hung, Lin Yen-Yu, Chiu Wei-Chen, Liu Yu-Lun | Department of Computer Science, National Yang Ming Chiao Tung University | Scal3R通过多相对位姿查询与位姿图优化，实现可扩展的在线三维重建。 | [#49](https://github.com/zitalk/PaperClaw/issues/49) |
| [20260903] Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States | Liao Kang, Luo Yihang, Wu Xiao-Ming, Jin Linyi, Wu Size, Lin Chunyu, Zhao Yao, Wang Fei, Li Wei, Chen Change Loy | S-Lab, Nanyang Technological University；University of Michigan；Beijing Jiaotong University | Puffin-World提出统一多模态模型，原生建模三维世界状态与物理动态。 | [#50](https://github.com/zitalk/PaperClaw/issues/50) |
| [20260903] Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning | Kim Ye-Chan, Choi Seunghee, Cha SeungJu, Kim Si-Woo, Kim Hwiseon, Kim Hyungee, Kim Dong-Jin | Hanyang University, South Korea | 利用视觉语言模型发现过渡事件，提升弱监督密集视频描述性能。 | [#51](https://github.com/zitalk/PaperClaw/issues/51) |
| [20260903] Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding | Qu Hongyu, Yao Guangming, Xing Ling, Hu Xiaobin, Ding Rongxing, Zhang Guibin, Zhang Fan, Yuan Yi, Shu Xiangbo, Yan Shuicheng | Nanjing University of Science and Technology；National University of Singapore；The Chinese University of Hong Kong * Equal contribution Corresponding authors.5em | 提出渐进式潜在记忆演化机制，增强流式视频理解与推理能力。 | [#52](https://github.com/zitalk/PaperClaw/issues/52) |
| [20260903] WorldReward: Reward Modeling for Camera-Conditioned World Models | Wang Yibin, Wang Zehan, Tang Junshu, Li Zhimin, Zhou Yujie, Bu Jiazi, Ling Pengyang, Han Feng, Zhang Zhixiong, Xing Long, Ding Shengyuan, Li Ziang, Jin Cheng, Zang Yuhang, Wang Jiaqi, Pang Tianyu | Fudan University；Shanghai Innovation Institute；Shanghai Jiao Tong University；Shanghai Artificial Intelligence Laboratory；Independent Researcher | WorldReward构建面向相机条件世界模型的奖励建模，提升动作一致性。 | [#53](https://github.com/zitalk/PaperClaw/issues/53) |
| [20260903] OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping | Lv Zelong, Xu Sicheng, Xiang Jianfeng, Wang Ruicheng, Dong Yue, Deng Yu, Sun Guangzhong, Yang Jiaolong | University of Science and Technology of China；Microsoft Research Asia；Tsinghua University；Work done during internship at Microsoft Research Asia | OctWorld结合八叉树与TSDF融合，生成长程世界一致的视频内容。 | [#54](https://github.com/zitalk/PaperClaw/issues/54) |
| [20260903] Revisiting Topological Graphs for Macro Action based Closed-loop Reinforcement Learning of Vision Language Navigation in Continuous Environment | Ye Shuhao, Mao Sitong, Cui Yuxiang, Wei Yufei, Yu Xuan, Zhai Shichao, Chen Wen, Zhou Shunbo, Xiong Rong, Wang Yue | Zhejiang University, Hangzhou, China；Zhejiang Humanoid Robot Innovation Center, Ningbo, China | 重新审视拓扑图在连续环境视觉语言导航闭环强化学习中的作用。 | [#55](https://github.com/zitalk/PaperClaw/issues/55) |
| [20260903] GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs | Du Junqing, Ropero Fernando, Turkoz Erkin, Zhang Yanfeng, Liu Lu | Riemann Lab, Huawei Technologies | GraFT利用三维场景图实现多模态大模型空间推理，无需额外训练。 | [#56](https://github.com/zitalk/PaperClaw/issues/56) |
| [20260903] VI3: Grounding Pretrained 3D Foundation Models with Inertial Cues | Lozano Ernesto, Jaenal Alberto, Civera Javier | Universidad de Zaragoza | VI3借助惯性测量单元为预训练三维基础模型恢复度量尺度与位姿。 | [#57](https://github.com/zitalk/PaperClaw/issues/57) |
| [20260903] ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation | Javier del Pino, Rodríguez Salvador, Garabito Alejandro, Álvarez Javier, Garabito Chema | speridlabs 2026 · SPERIDLABS RESEARCH；PREPRINT · 2026 · SPERIDLABS RESEARCH ENEAS · 1 | ENEAS提出嵌入引导的神经集成方法，用于自适应分割与实例跟踪。 | [#58](https://github.com/zitalk/PaperClaw/issues/58) |
| [20260903] Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning | Yang Yijun, Zheng Shenghe, Li Wenbo, Liu Jianhui, Sun Haoze, Zhang Yanbing, Jiang Jiaxiu, Song Lin, Huang Haoyang, Duan Nan, Zhu Lei | The Hong Kong University of Science and Technology (Guangzhou)；Joy Future Academy；The Hong Kong University of Science and Technology；University of Hong Kong | Unfold The World通过分解四维属性并强化学习，增强空间推理与时间一致性。 | [#59](https://github.com/zitalk/PaperClaw/issues/59) |
| [20260903] Residual Optimal Transport-Based Experts Collaboration Towards Modality-Aware Infrared-Visible Object Detection | Zhao Yue, Yu Hua, Zhao Yukun, Zhang Yuzhi, Gong Maoguo, Mei Xin, Hu Zhuping, Li Yanchi, A. K. Qin | School of Electronic Engineering, Key Laboratory of Collaborative Intelligence Systems, Ministry of Education, Xidian University, Xi’an, China. (；College of Computing and Data Science, Nanyang Technological University, Singapore；School of Electronics and Communication Engineering, Sun Yat‑sen University, Guangzhou, China；School of Cyber Science and Engineering, Zhengzhou University, Zhengzhou, China；School of Computer Science, China University of Geosciences, Wuhan, China；Department of Computing Technologies, Swinburne University of Technology, Hawthorn, VIC, Australia | 基于残差最优传输的专家协作方法，提升红外-可见光目标检测的模态感知融合。 | [#60](https://github.com/zitalk/PaperClaw/issues/60) |
| [20260903] When Depth Hurts: Reliability-Aware Geometry Distillation for Depth-Free RGB-D Salient Object Detection | Wang Xuehao, Hua Jiaxin, Li Runmei, Wu Zhenyu, Chen Chenglizhao, Gu Ke, Hao Aimin | University of International Business and Economics；State Key Laboratory of Virtual Reality Technology and；Systems,3 China University of Petroleum；Southwest Jiaotong University；Beijing University Of Technology | 提出可靠性感知几何蒸馏，实现无深度输入的RGB-D显著性目标检测。 | [#61](https://github.com/zitalk/PaperClaw/issues/61) |

## 🔎 观察

- 三维几何先验与多模态模型融合成为主流，多篇工作将八叉树、场景图或拓扑图引入生成与推理框架。
- 从静态感知转向动态、物理一致的世界建模，强化学习与奖励建模被用于提升空间推理和动作一致性。

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
