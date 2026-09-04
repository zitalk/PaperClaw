# Daily Reports

最近三天日报（最新在前）：

# [20260904](./202609/20260904.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "degraded", "checked_at": "2026-09-05T00:55:29+08:00", "unavailable_sources": ["Springer Nature", "IEEE Xplore"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，但存在异常 · 最近检查：2026-09-05 00:55:29（北京时间）

本轮检索候选论文 59 篇；刊会准入通过 0 篇（排除 59 篇）；本轮 LLM 新筛中 0 篇，复用已收录匹配 0 篇；本轮新增入报 0 篇；目标日累计收录 0 篇。当日未检索到符合条件并纳入日报的论文。 部分来源不可用：Springer Nature、IEEE Xplore；本次结果不代表完整覆盖。

## ✨ 今日亮点

- 本次有异常，请查看来源状态及失败明细；不能将部分结果当作完整检索结果。

## 🔎 检索说明

- 日报日期是论文检索目标日期；最近检查时间是任务实际执行时间。
- 零结果不代表所有来源当天没有新论文，只表示本次未纳入符合条件的论文。
- 同一日期后续补扫会更新这份日报，不重复创建日报 Issue。

---

Powered by OpenClaw🦞

---

# [20260903](./202609/20260903.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "degraded", "checked_at": "2026-09-04T19:06:47+08:00", "unavailable_sources": ["Semantic Scholar", "Springer Nature", "IEEE Xplore"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，但存在异常 · 最近检查：2026-09-04 19:06:47（北京时间）
本轮检索候选论文 121 篇；刊会准入通过 61 篇（排除 60 篇）；本轮 LLM 新筛中 17 篇，复用已收录匹配 13 篇；本轮新增入报 17 篇；目标日累计收录 30 篇。

部分来源不可用：Semantic Scholar、Springer Nature、IEEE Xplore；本次结果不代表完整覆盖。 今日研究呈现三大主线：一是3D场景理解与重建的深化，涵盖在线重建、世界模型、高斯泼溅及深度合成，强调空间一致性与可扩展性；二是视觉语言模型在视频理解、空间推理和具身导航中的融合应用，注重时序建模与跨模态对齐；三是面向自动驾驶、机器人及遥感等领域的专用框架与基准，关注可靠性、物理约束和实际部署。整体趋势从静态感知向动态世界建模与闭环决策演进，多模态与3D表征的结合成为核心驱动力。

## ✨ 今日亮点

- Scal3R提出多相对位姿查询，提升在线3D重建的可扩展性与回环优化效率。
- Puffin-World构建原生3D世界状态的多模态统一模型，强化空间模拟与物理动态。
- GraFT以训练无关方式利用3D场景图，增强多模态大模型的空间推理能力。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260903] Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction | Lin Chin-Yang, Sun Yang-Che, Sun Cheng, Yang Fu-En, Chen Min-Hung, Lin Yen-Yu, Chiu Wei-Chen, Liu Yu-Lun | Department of Computer Science, National Yang Ming Chiao Tung University | Scal3R通过多相对位姿查询实现可扩展在线3D重建，优化位姿图与回环检测。 | [#49](https://github.com/zitalk/PaperClaw/issues/49) |
| [20260903] Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States | Liao Kang, Luo Yihang, Wu Xiao-Ming, Jin Linyi, Wu Size, Lin Chunyu, Zhao Yao, Wang Fei, Li Wei, Chen Change Loy | S-Lab, Nanyang Technological University；University of Michigan；Beijing Jiaotong University | Puffin-World提出统一多模态模型，原生集成3D世界状态以支持空间模拟与物理动态。 | [#50](https://github.com/zitalk/PaperClaw/issues/50) |
| [20260903] Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning | Kim Ye-Chan, Choi Seunghee, Cha SeungJu, Kim Si-Woo, Kim Hwiseon, Kim Hyungee, Kim Dong-Jin | Hanyang University, South Korea | 利用VLM引导过渡事件发现，提升弱监督密集视频描述中的时序事件定位能力。 | [#51](https://github.com/zitalk/PaperClaw/issues/51) |
| [20260903] Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding | Qu Hongyu, Yao Guangming, Xing Ling, Hu Xiaobin, Ding Rongxing, Zhang Guibin, Zhang Fan, Yuan Yi, Shu Xiangbo, Yan Shuicheng | Nanjing University of Science and Technology；National University of Singapore；The Chinese University of Hong Kong * Equal contribution Corresponding authors.5em | 提出渐进式潜在记忆演化机制，增强流式视频理解中的长期推理与记忆能力。 | [#52](https://github.com/zitalk/PaperClaw/issues/52) |
| [20260903] WorldReward: Reward Modeling for Camera-Conditioned World Models | Wang Yibin, Wang Zehan, Tang Junshu, Li Zhimin, Zhou Yujie, Bu Jiazi, Ling Pengyang, Han Feng, Zhang Zhixiong, Xing Long, Ding Shengyuan, Li Ziang, Jin Cheng, Zang Yuhang, Wang Jiaqi, Pang Tianyu | Fudan University；Shanghai Innovation Institute；Shanghai Jiao Tong University；Shanghai Artificial Intelligence Laboratory；Independent Researcher | WorldReward为相机条件世界模型设计奖励建模，确保生成内容与动作一致性。 | [#53](https://github.com/zitalk/PaperClaw/issues/53) |
| [20260903] OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping | Lv Zelong, Xu Sicheng, Xiang Jianfeng, Wang Ruicheng, Dong Yue, Deng Yu, Sun Guangzhong, Yang Jiaolong | University of Science and Technology of China；Microsoft Research Asia；Tsinghua University；Work done during internship at Microsoft Research Asia | OctWorld结合八叉树3D映射与TSDF融合，实现长程世界一致的视频生成。 | [#54](https://github.com/zitalk/PaperClaw/issues/54) |
| [20260903] Revisiting Topological Graphs for Macro Action based Closed-loop Reinforcement Learning of Vision Language Navigation in Continuous Environment | Ye Shuhao, Mao Sitong, Cui Yuxiang, Wei Yufei, Yu Xuan, Zhai Shichao, Chen Wen, Zhou Shunbo, Xiong Rong, Wang Yue | Zhejiang University, Hangzhou, China；Zhejiang Humanoid Robot Innovation Center, Ningbo, China | 重新审视拓扑图在连续环境视觉语言导航中的应用，采用宏动作闭环强化学习。 | [#55](https://github.com/zitalk/PaperClaw/issues/55) |
| [20260903] GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs | Du Junqing, Ropero Fernando, Turkoz Erkin, Zhang Yanfeng, Liu Lu | Riemann Lab, Huawei Technologies | GraFT利用3D场景图以训练无关方式提升多模态大模型的空间推理与视角转换能力。 | [#56](https://github.com/zitalk/PaperClaw/issues/56) |
| [20260903] VI3: Grounding Pretrained 3D Foundation Models with Inertial Cues | Lozano Ernesto, Jaenal Alberto, Civera Javier | Universidad de Zaragoza | VI3通过惯性测量单元线索为预训练3D基础模型恢复度量尺度并估计相机位姿。 | [#57](https://github.com/zitalk/PaperClaw/issues/57) |
| [20260903] ENEAS: Embedding-guided Neural Ensemble for Adaptive Segmentation | Javier del Pino, Rodríguez Salvador, Garabito Alejandro, Álvarez Javier, Garabito Chema | speridlabs 2026 · SPERIDLABS RESEARCH；PREPRINT · 2026 · SPERIDLABS RESEARCH ENEAS · 1 | ENEAS提出嵌入引导的神经集成方法，用于自适应分割并缓解时序幻觉问题。 | [#58](https://github.com/zitalk/PaperClaw/issues/58) |
| [20260903] Unfold The World: Factorize 4D Properties in Reinforcing Spatial Reasoning | Yang Yijun, Zheng Shenghe, Li Wenbo, Liu Jianhui, Sun Haoze, Zhang Yanbing, Jiang Jiaxiu, Song Lin, Huang Haoyang, Duan Nan, Zhu Lei | The Hong Kong University of Science and Technology (Guangzhou)；Joy Future Academy；The Hong Kong University of Science and Technology；University of Hong Kong | Unfold The World分解4D属性并通过强化学习增强视觉语言模型的空间推理与时序一致性。 | [#59](https://github.com/zitalk/PaperClaw/issues/59) |
| [20260903] Residual Optimal Transport-Based Experts Collaboration Towards Modality-Aware Infrared-Visible Object Detection | Zhao Yue, Yu Hua, Zhao Yukun, Zhang Yuzhi, Gong Maoguo, Mei Xin, Hu Zhuping, Li Yanchi, A. K. Qin | School of Electronic Engineering, Key Laboratory of Collaborative Intelligence Systems, Ministry of Education, Xidian University, Xi’an, China. (；College of Computing and Data Science, Nanyang Technological University, Singapore；School of Electronics and Communication Engineering, Sun Yat‑sen University, Guangzhou, China；School of Cyber Science and Engineering, Zhengzhou University, Zhengzhou, China；School of Computer Science, China University of Geosciences, Wuhan, China；Department of Computing Technologies, Swinburne University of Technology, Hawthorn, VIC, Australia | 基于残差最优传输的专家协作框架，实现模态感知的红外-可见光目标检测。 | [#60](https://github.com/zitalk/PaperClaw/issues/60) |
| [20260903] When Depth Hurts: Reliability-Aware Geometry Distillation for Depth-Free RGB-D Salient Object Detection | Wang Xuehao, Hua Jiaxin, Li Runmei, Wu Zhenyu, Chen Chenglizhao, Gu Ke, Hao Aimin | University of International Business and Economics；State Key Laboratory of Virtual Reality Technology and；Systems,3 China University of Petroleum；Southwest Jiaotong University；Beijing University Of Technology | 提出可靠性感知几何蒸馏方法，在无深度输入下提升RGB-D显著性目标检测性能。 | [#61](https://github.com/zitalk/PaperClaw/issues/61) |
| [20260903] Principia: Relational Physics Tests for Video Models | Varun Varma Thozhiyoor, Tripathi Shivam, Venkatesh Babu Radhakrishnan, Bhattad Anand | Indian Institute of Science；Johns Hopkins University | Principia构建关系物理测试基准，评估视频模型在牛顿力学推理上的表现。 | [#62](https://github.com/zitalk/PaperClaw/issues/62) |
| [20260903] Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations | Denis M. Akola, David F. Fouhey | New York University, Tandon School of Engineering；MetroTech Center；Courant Institute of Mathematical Sciences | 利用3D基础模型场景表示实现零样本新视角深度合成，无需额外训练。 | [#63](https://github.com/zitalk/PaperClaw/issues/63) |
| [20260903] Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving | Yao Ruoyu, Xie Yusen, Liu Qingzhao, Liu Pei, Yang Zewei, Zhu Yipeng, Wang Xiaolong, Ma Jun | The Hong Kong University of Science and Technology (Guangzhou), Guangzhou 511453, China ( | 提出潜在对齐规划方法，将离散动作表示与连续控制结合用于端到端自动驾驶。 | [#64](https://github.com/zitalk/PaperClaw/issues/64) |
| [20260903] MulDP: Multimodal Diffusion Policy for Autonomous Quadruped Parkour Navigation across Complex Terrains | Hu Kangmai, Zhang Yueqi, Zhai Peng, Wei Xiaoyi, Hu Jiabin, Liu Zhixiang, Qian Quancheng, Zhang Lihua | Zhixiang Liu, Quancheng Qian and Lihua Zhang are with the College；of Intelligent Robotics and Advanced Manufacturing, Fudan University | MulDP采用多模态扩散策略，实现四足机器人在复杂地形上的跑酷导航。 | [#65](https://github.com/zitalk/PaperClaw/issues/65) |
| [20260903] Sparse auto-regressive modeling for scene generation from multi-view images | Lucas Thomas, Pietrantoni Maxime, Weinzaepfel Philippe, Cho Wonjune, Bardienus Pieter Duisterhof, Leroy Vincent, Revaud Jerome | Carnegie Mellon University, USA | 稀疏自回归建模从多视角图像生成3D场景，结合3D高斯泼溅表示。 | [#66](https://github.com/zitalk/PaperClaw/issues/66) |
| [20260903] Urban Boundaries, Social Barriers: A Benchmark and Vision-Centric Framework for Mapping Gated Communities and Equity Implications | Zhao Minwei, Zhang Weiming, Du Jiawang, Liu Qiming, Zhuang Weiming, Nie Pei, Wu Cai | The Hong Kong University of Science and Technology (Guangzhou)；School of Public Administration and Policy, Renmin University of China；University of South China | 构建门禁社区映射基准与视觉中心框架，分析城市边界与社会公平的关联。 | [#67](https://github.com/zitalk/PaperClaw/issues/67) |
| [20260903] A Reverse Sign Language Dictionary: Open-Vocabulary Sign Recognition from Continuous Signing via Video Captioning and Description Retrieval | Poveda-Gutiérrez Santiago, Nakayama Hideki, Bono Mayumi | University of Tokyo；Information and Society Research Division；National Institute of Informatics | 通过视频描述与描述检索实现开放词汇手语识别，构建反向手语词典。 | [#68](https://github.com/zitalk/PaperClaw/issues/68) |
| [20260903] Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations | Şahin Onat, Altillawi Mohammad, Eskandar George, Carbone Carlos, Liu Ziyuan | Institution1；Institution1 address；Institution2；First line of institution2 address；Technical University of Munich；Huawei Heisenberg Research Center | 提出优化无关的形态学扰动方法，学习3D感知视频先验以修复生成伪影。 | [#69](https://github.com/zitalk/PaperClaw/issues/69) |
| [20260903] Stabilizing Camera-Controlled Novel View Synthesis at Inference Time | Singh Prajwal, Badola Arjun, Kumari Seema, Nagahara Hajime, Raman Shanmuganathan | CVIG Lab and ISLab, D3 Center；IIT Gandhinagar and Osaka University | 在推理时稳定相机控制的新视角合成，缓解自回归生成中的漂移问题。 | [#70](https://github.com/zitalk/PaperClaw/issues/70) |
| [20260903] FailBench: How Reliable are VLMs at Judging Robot Task Success? | Navasardyan Zaruhi, Danielyan Tatul, Davtyan Hrant | Metric AI Lab | FailBench基准评估视觉语言模型在机器人任务成功判定上的可靠性。 | [#71](https://github.com/zitalk/PaperClaw/issues/71) |
| [20260903] Text2Thermal: Physics-Aware Thermal Image Synthesis from Textual Priors | Qazi Tayeba, Lall Brejesh, Mukherjee Prerana | \( 1\) Bharti School of Telecommunications Technology and Management；Indian Institute of Technology, Delhi, India；\( 2\) School of Engineering, Jawaharlal Nehru University, Delhi, India | Text2Thermal从文本先验合成物理感知的热红外图像，结合多模态学习。 | [#72](https://github.com/zitalk/PaperClaw/issues/72) |
| [20260903] Drive-HWM: Hierarchical World Models for Dynamic-Latent Guided Autonomous Driving | Fan Zhaoxin, Zhang Tianbao, Wu Wenjun, Wang Xiaofeng, Jin Yeying, Zhao Jian, Zhu Zheng, Yan Shuicheng | School of Artificial Intelligence, Beihang University, Beijing, China；Shanghai Jiao Tong University, Shanghai, China and Dim12 AI；National University of Singapore；the National University of Singapore, Singapore | Drive-HWM构建分层世界模型，利用动态潜在变量与光流引导自动驾驶决策。 | [#73](https://github.com/zitalk/PaperClaw/issues/73) |
| [20260903] WIDE: Wildcard Inference with Dynamic Expansion for Cross-Modal Generative Retrieval | Guo Teng, Wang Xin, Xu Jiayou, Zhou Keying, Shen Jifeng, Ruan Haoxin | College of Computer Science and College of Computer Science and College of Computer Science and；Jilin University Jilin University Jilin University；College of Computer Science and School of Electrical and Information College of Computer Science and；Jilin University Jiangsu University Jilin University；∗ Also with Key Laboratory of Symbolic Computation and Knowledge Engineering of；Ministry of Education, Jilin University | WIDE提出通配符推理与动态扩展机制，提升跨模态生成式检索的灵活性。 | [#74](https://github.com/zitalk/PaperClaw/issues/74) |
| [20260903] Air-Ground Collaborative Vision-and-Language Navigation via Shared Bird's-Eye Maps | Zhang Shuning, Li Liang, Wang Yunheng, Wang Tao, Kang Yihang, Xu Renjing | the Robotics and Autonomous Systems Thrust, Systems Hub, The Hong Kong University of Science and Technology (Guangzhou), China；School of Communications and Information Engineering, Nanjing University of Posts and Telecommunications, China | 通过共享鸟瞰图实现空地协同视觉语言导航，增强无人机与地面机器人协作。 | [#75](https://github.com/zitalk/PaperClaw/issues/75) |
| [20260903] STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction | Li Bocheng, Zhang Wenjuan, Jie Pan. Dongxu Han, Ma Xuesong, Yao Yiling, Wang Yaning | State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute, Chinese Academy of Sciences；Aerospace Information Research Institute, Chinese Academy of Sciences；University of Chinese Academy of Sciences | STARS-GS采用结构感知正则化高斯泼溅，用于大规模航空影像表面重建。 | [#76](https://github.com/zitalk/PaperClaw/issues/76) |
| [20260903] Exploring the Potential of Contrastive Language-Image Pre-training for Multi-Source Remote Sensing Data | Miao Xiangyang, Yao Kelu, Huang Yekai, Xu Xiaogang, Xue Junxiao, Shen Minjun, Lv Chenghui, Liu Shanji, Chen Yaying, Li Chao | School of Computer Science and Technology, Zhejiang University；Space-based Computing System Research Center, Zhejiang Lab | 探索对比语言-图像预训练在多源遥感数据中的应用，提出光谱-空间基分解。 | [#77](https://github.com/zitalk/PaperClaw/issues/77) |
| [20260903] R2S-Eval: Robot Evaluation with Real-to-Sim Calibration via Vision-Language Models | Wang Yidi, Ruan Feixiang, Chen Ruoqu, Yin Jie, Yu Yang, Xu Mengdi, Zhang Kaifeng | Tongji University；Tsinghua University | R2S-Eval利用视觉语言模型进行真实到仿真校准，评估机器人操作策略。 | [#78](https://github.com/zitalk/PaperClaw/issues/78) |

## 🔎 观察

- 3D表征与多模态大模型的融合正在加速，从场景重建扩展到世界建模与空间推理，显示空间智能成为研究焦点。
- 面向自动驾驶、机器人和遥感的专用框架强调物理约束与可靠性，反映从通用模型向任务导向部署的转变趋势。

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

<!-- paperclaw-report: zitalk/PaperClaw -->

---
