# Daily Reports

最近三天日报（最新在前）：

# [20260930](./202609/20260930.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "ok", "checked_at": "2026-10-01T03:27:02+08:00", "unavailable_sources": [], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成 · 最近检查：2026-10-01 03:27:02（北京时间）

本轮检索候选论文 120 篇；刊会准入通过 1 篇（排除 119 篇）；本轮 LLM 新筛中 0 篇，复用已收录匹配 0 篇；本轮新增入报 0 篇；目标日累计收录 0 篇。当日未检索到符合条件并纳入日报的论文。 

## ✨ 今日亮点

- 研究的进展，常常藏在持续积累的每一个小步里。

## 🔎 检索说明

- 日报日期是论文检索目标日期；最近检查时间是任务实际执行时间。
- 零结果不代表所有来源当天没有新论文，只表示本次未纳入符合条件的论文。
- 同一日期后续补扫会更新这份日报，不重复创建日报 Issue。

---

Powered by OpenClaw🦞

---

# [20260929](./202609/20260929.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "partial", "checked_at": "2026-09-30T19:45:39+08:00", "unavailable_sources": ["Semantic Scholar", "IEEE Xplore"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，部分来源覆盖受限 · 最近检查：2026-09-30 19:45:39（北京时间）
本轮检索候选论文 240 篇；刊会准入通过 141 篇（排除 99 篇）；本轮 LLM 新筛中 41 篇，复用已收录匹配 0 篇；本轮新增入报 41 篇；目标日累计收录 41 篇。

部分来源不可用：Semantic Scholar、IEEE Xplore；本次结果不代表完整覆盖。 今日论文聚焦多模态大模型的空间推理、视觉token效率与跨模态对齐。Imagine3D-LLM、EviViT等工作探索让模型在回答前先想象或筛选视觉证据；多篇token剪枝与路由研究（TReVS、OmniRoute、UniAfford）试图在效率与细粒度感知间取得平衡。自动驾驶与机器人领域强调物理一致的世界-动作模型（PhysWAM、MVG-WAM）及规划导向的基准测试。此外，遥感、工业异常检测与增量学习也出现针对性方案，整体呈现从通用能力向可靠、高效、可解释方向演进的趋势。

## ✨ 今日亮点

- 多模态模型从被动感知转向主动想象与证据筛选，提升空间推理可靠性。
- 视觉token剪枝与路由成为效率热点，兼顾文本相关性与空间结构保留。
- 世界-动作模型强调几何与物理一致性，推动自动驾驶与机器人规划落地。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260929] Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering | Jung Jaewoo, Yu Hyeonseo, An Honggyu, Han Jisang, Kim Mungyeom, Jeon Minkyeong, Shin Heeseong, Moon WonJun, Tombari Federico, Barath Daniel, Pollefeys Marc, Kim Seungryong, Hong Sunghwan | KAIST AI ETH Zürich Google TUM ETH AI Center；One line of research implicitly or explicitly boosts pixel-level correspondences across views by either；∗ Work done during a visiting researcher period at ETH Zürich | 提出Imagine3D-LLM，让多模态大模型在回答前先想象3D场景，增强空间推理能力。 | [#599](https://github.com/zitalk/PaperClaw/issues/599) |
| [20260929] From Routing Signals to Selective Review: Visual regrounding in MoE VLMs | Guo Hongzhu, Fayyaz Mohsen, Peng Nanyun | University of California, Los Angeles；Peking University | 利用MoE路由信号进行选择性视觉重定位，提升VLM对目标缺失的检测能力。 | [#600](https://github.com/zitalk/PaperClaw/issues/600) |
| [20260929] OmniTaskonomy: When Does Visual Generation Improve Visual Understanding? | Ge Jiaxin, Qin Yiming, Xie Ji, Jiang Haozhe, Han Xiaochuang, Zhang Junyi, Dai Andrew, Yang Yinfei, Malik Jitendra, Krishna Ranjay, Min Sewon, Feng Haiwen, Xue Le, Shi Baifeng, Darrell Trevor, Wang XuDong | University of California, Berkeley；Duke University；Carnegie Mellon University；University of Washington；Impossible Research；Work done during a summer internship at Impossible Research | 系统研究视觉生成何时能提升视觉理解，提出OmniTaskonomy评估框架。 | [#601](https://github.com/zitalk/PaperClaw/issues/601) |
| [20260929] RS-OPSD: Reliable Privileged On-Policy-Self-Distillation for Ultra-High-Resolution Remote Sensing VQA | Jiang Chengjie, Zhou Yunqi, Yan Jiafeng, Zhao Sihang, Yuan Chun, Li Jing | Tsinghua University；Zhejiang University；Central University of Finance and Economics；East China Normal University；Key Laboratory of Geographic Information Science | 面向超高分辨率遥感VQA，提出可靠特权在线自蒸馏方法RS-OPSD。 | [#602](https://github.com/zitalk/PaperClaw/issues/602) |
| [20260929] PhysWAM: Physically Consistent World Action Model for Autonomous Driving | Parikh Dhruv, Yu Fengcheng, Gao Quankai, Yang Jiawei, Ye Junjie, Bhatt Maulik, Vu Thang, Ochoa Charles, McAllister Rowan, Vasiljevic Igor, Kannan Rajgopal, Prasanna Viktor, Guizilini Vitor, Wang Yue | University of Southern California；Toyota Research Institute；DEVCOM Army Research Office * | 构建物理一致的世界-动作模型PhysWAM，用于自动驾驶多视角视频预测。 | [#603](https://github.com/zitalk/PaperClaw/issues/603) |
| [20260929] SYNCR: Diagnosing and Learning Cross-Video Reasoning from Simulation | Ghazanfari Sara, Garg Siddharth, Krishnamurthy Prashanth, Khorrami Farshad | New York University | 提出SYNCR框架，从仿真中诊断并学习跨视频推理能力。 | [#604](https://github.com/zitalk/PaperClaw/issues/604) |
| [20260929] Visual Branch is What You Need for CLIP-based Class-Incremental Learning | Hu Tao, Xie Zhen-Hao, Guo Jingcai, Zhan De-Chuan, Zhou Da-Wei | School of Artificial Intelligence, Nanjing University；State Key Laboratory for Novel Software Technology, Nanjing University；Hong Kong Polytechnic University | 发现视觉分支对CLIP类增量学习至关重要，提出相应改进方法。 | [#605](https://github.com/zitalk/PaperClaw/issues/605) |
| [20260929] ExceptionDrive: A Planning-Oriented Counterfactual Corner-Case Benchmark for Autonomous Driving | Luo Ziyi, Sun Zhe, Lu Yehao, Zhou Lei, Wu Lisheng, Li Xuewei, Qin Zequn, Li Xi | College of Computer Science and Technology, Zhejiang University, Hangzhou, China | 发布ExceptionDrive，面向规划的反事实 corner-case 自动驾驶基准。 | [#606](https://github.com/zitalk/PaperClaw/issues/606) |
| [20260929] MVG-WAM: Multiple View Geometry-Aware World-Action Modeling for Robotic Manipulation | Chen Wenbo, Li Tianfu, Xu Haoxuan, Cao Zhihao, Chen Zhenghan, Zhu Zhengming, Luo Zizhou, Yang Guosheng, Liu Yuan, Wang Lujia, Chen Wen, Li Haoang | The Hong Kong University of Science and Technology (Guangzhou)；The Hong Kong University of Science and Technology；Zhejiang University；University of Zurich；The Chinese University of Hong Kong | 提出MVG-WAM，融合多视角几何约束的世界-动作模型用于机器人操作。 | [#607](https://github.com/zitalk/PaperClaw/issues/607) |
| [20260929] Selective Channel Restoration for Backdoored Vision-Language Models | Liu Shuming, Zhang Zhifang, Yuan Suqin, Khin Mi Mi Aung, Lin Zhuoyi, Feng Lei | Southeast University；University of Queensland；University of Sydney | 针对后门攻击的视觉语言模型，提出选择性通道恢复防御方法。 | [#608](https://github.com/zitalk/PaperClaw/issues/608) |
| [20260929] Are In-Context Images Worth 10 Dimensions? | Adhemar de Senneville, Bou Xavier, Anger Jérémy, Grompone Rafael, Facciolo Gabriele | Université Paris-Saclay, CNRS, ENS Paris-Saclay, Centre Borelli, Paris, France；Institut Universitaire de France, Paris, France | 探究上下文图像在LVLM中的价值，发现共享判别几何可降维至10维。 | [#609](https://github.com/zitalk/PaperClaw/issues/609) |
| [20260929] When to Adapt: Multi-Signal Domain Shift Detection for Efficient Training-Free Adaptation in Open-Vocabulary Segmentation | Antonazzi Michele, Alejandra C. Hernandez, Araujo José, Andersson Olov, Jensfelt Patric | EECS and Digital Futures, KTH Royal Institute of Technology, Stockholm, Sweden；Ericsson Research, Ericsson AB, Stockholm, Sweden | 提出多信号域偏移检测，实现开放词汇分割的高效无训练自适应。 | [#610](https://github.com/zitalk/PaperClaw/issues/610) |
| [20260929] TReVS: Integrating Textual Relevance and Visual Saliency for Efficient Vision-Language Model Token Pruning | Wang Jing, Wu Zhiping, Ren Dongdong, Han Youfang, Zhao Wei, Li Wenbin | School of Intelligence Science and Technology, Nanjing University；School of Electronic Science and Engineering, Nanjing University；Geely Automobile Research Institute (Ningbo) Co., Ltd., 315000 | TReVS结合文本相关性与视觉显著性，高效剪枝VLM视觉token。 | [#611](https://github.com/zitalk/PaperClaw/issues/611) |
| [20260929] HyperSAM: A Promptable Foundation Model for Hyperspectral Remote Sensing | Pang Li, Wu Xinqiao, Yao Jing, Ghamisi Pedram, Zhou Jun, Chen Zhengchao, Meng Deyu, Cao Xiangyong | School of Mathematics and Statistics, Xi'an Jiaotong University, Xi'an, China (；the Faculty of Electronic and Information Engineering, Xi'an Jiaotong University, Xi'an, China (；State Key Laboratory of Remote Sensing and Digital Earth, Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing, China (；Faculty of Electrical and Computer Engineering, University of Iceland, 101 Reykjavik, Iceland (；School of Information and Communication Technology, Griffith University, Nathan, QLD, Australia (；School of Computer Science and Technology, Xi'an Jiaotong University, Xi'an, China ( | HyperSAM：面向高光谱遥感的可提示分割基础模型。 | [#612](https://github.com/zitalk/PaperClaw/issues/612) |
| [20260929] FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection | Abhay Kumar Das, Gangireddy Rajesh, Vaidya Ashwin, Akcay Samet | Silicon University, Bhubaneswar, India | FLASH框架实现工业异常检测中合成异常的一次生成多次合成。 | [#613](https://github.com/zitalk/PaperClaw/issues/613) |
| [20260929] UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception | Liu Yuhao, Zhong Yiming, Wang Hanqing, Yan Shaocheng, Zhang Yuhang, Lyu Wenzhou, Ding Ziyang, Zhang Wei, Zhao Xue, Pan Jin, Ma Yuexin, Zhu Xinge | ShanghaiTech University；Shandong University；Wuhan University | UniAfford通过token路由多任务学习，实现可泛化的2D-3D可供性感知。 | [#614](https://github.com/zitalk/PaperClaw/issues/614) |
| [20260929] Codebook-Guided Cross-Modal Knowledge Distillation for Structurally Heterogeneous Features | Dae Ung Jo, Lim Jongin, Yoo YoungJoon, Um Daeho | Kyungpook National University；AX/PI Center, Samsung Electronics；Chung-Ang University, SNUAILAB；University of Seoul | 基于码本的跨模态知识蒸馏，对齐结构异构特征。 | [#615](https://github.com/zitalk/PaperClaw/issues/615) |
| [20260929] End-to-End Self-Supervised RGB-T Tracking without Modality Misleading | Li Shenglan, Yao Rui, Sun Kunyang, Jia Hong, Zhou Yong, Javen Qinfeng Shi, Zhang Xinyu | School of Computer Science and Technology / School of Artificial；Intelligence, China University of Mining and Technology, China；Mine Digitization Engineering Research Center of the Ministry of；University of Auckland, Auckland, New Zealand | 端到端自监督RGB-T跟踪，避免模态误导。 | [#616](https://github.com/zitalk/PaperClaw/issues/616) |
| [20260929] EviViT: Evidence-Adaptive Vision Transformers for Fine-Grained Perception | Niu Yaoxin, Chen Zhangquan, Zhang Yang, An Xiang, Wang Zhumei, Liao Chih-Ting, Cao Hongkun, Huang Ruqi | Tsinghua University；Peng Cheng Laboratory；The Hong Kong University of Science and Technology；LMMs-Lab；Beijing Institute of Technology；University of New South Wales | EviViT：证据自适应视觉Transformer，按问题分配视觉token实现细粒度感知。 | [#617](https://github.com/zitalk/PaperClaw/issues/617) |
| [20260929] Why MLLMs Struggle to Count: Overcoming Individuation and Aggregation Bottlenecks with ConvStack | Che Liwei, Quan Yihao, Fang Sen, Wang Hongyi, Krishna Ranjay, Tang Ruixiang, Pavlovic Vladimir | Department of Computer Science, Rutgers University；Department of Computer Science, University of Washington | 分析MLLM计数瓶颈，提出ConvStack克服个体化与聚合难题。 | [#618](https://github.com/zitalk/PaperClaw/issues/618) |
| [20260929] OmniRoute: Mapping Temporal Semantic Evidence to Audio-Visual Token Budgets for Efficient Omnimodal Large Language Models | Deng Yuchen, Cai Zidang, Yang Feidiao, Wang Yufei, Wang Jie, Zheng Hai-Tao, Han Yuxing | Shenzhen International Graduate School, Tsinghua University, China；Pengcheng Laboratory, China；will be released to facilitate further research | OmniRoute将时序语义证据映射到音视频token预算，实现高效全模态LLM。 | [#619](https://github.com/zitalk/PaperClaw/issues/619) |
| [20260929] Speed in the Blind Spot: An Interpretability Analysis of Dynamic Perception in VLMs for Autonomous Driving | Winter Katharina, Englmeier Stefan, Fabian B. Flohr | Munich University of Applied Sciences, Intelligent Vehicles Lab (IVL) | 可解释性分析揭示VLM在自动驾驶动态感知中的速度估计盲区。 | [#620](https://github.com/zitalk/PaperClaw/issues/620) |
| [20260929] UniBuild: Unified Building Mapping From Multi-Source Optical Remote Sensing Imagery With Detail Decoding and Geometry Regularization | Huang Wei, Liu Chenying, Shi Yilei, Xiao Xiang Zhu | the Chair of Data Science in Earth Observation, Technical University of Munich, Munich, Germany; Chenying Liu and Xiao Xiang Zhu are also with Fig. 1 | UniBuild统一多源光学遥感建筑制图，结合细节解码与几何正则。 | [#621](https://github.com/zitalk/PaperClaw/issues/621) |
| [20260929] VesselBench-800K: A Large-scale Perception Benchmark for Multimodal Vessel Detection, Counting, and Density Estimation | Hong Danfeng, Li Chenyu, Chanussot Jocelyn | School of Automation, Southeast University, Nanjing, China. (；Univ | VesselBench-800K：大规模多模态船舶检测、计数与密度估计基准。 | [#622](https://github.com/zitalk/PaperClaw/issues/622) |
| [20260929] Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference | Chen Jiayu, Gao Shuyong, Jia Jingkai, Bu Xiaosheng, Fu Jiyuan, Hong Lingyi, Jiang Kaixun, Xu Yipan, Zhang Wenqiang | Fudan University；The Hong Kong Polytechnic University | 超越token重要性，保留空间支架实现高效视觉-语言-动作推理。 | [#623](https://github.com/zitalk/PaperClaw/issues/623) |
| [20260929] SFE-VGGT: Source-Free VGGT Distillation for Event-Based Monocular Depth Estimation | Thai Duy Nguyen, Addison Lin Wang | Nanyang Technological University, Singapore | SFE-VGGT：无源VGGT蒸馏用于事件相机单目深度估计。 | [#624](https://github.com/zitalk/PaperClaw/issues/624) |
| [20260929] Representation Dynamics Reveal Semantic Saliency and Similarity for Visual Token Pruning in MLLMs | Li Weixuan, Zhou Zikun, Zhuang Xinyi, Guo Xinyan, Tian Rui, Zhang Chuyao, Gao Lin | Harbin Institute of Technology；Shenzhen Loop Area Institute | 利用表示动态揭示语义显著性与相似性，指导MLLM视觉token剪枝。 | [#625](https://github.com/zitalk/PaperClaw/issues/625) |
| [20260929] ProGuT: Label-Efficient Panoptic Segmentation for Forest Scenes | Deoli Pankaj, Berns Karsten | Robotics Research Lab, RPTU Kaiserslautern-Landau | ProGuT：标签高效的森林场景全景分割方法。 | [#626](https://github.com/zitalk/PaperClaw/issues/626) |
| [20260929] S4VY: Segment Anything in Feed-Forward 4D Visual Geometry | Zhang Jingdong, Li Xin, Kautz Jan, Wang Wenping, Choy Chris | blackTexas A\&M University, College Station | S4VY：在前馈4D视觉几何中实现任意分割。 | [#627](https://github.com/zitalk/PaperClaw/issues/627) |
| [20260929] GlassFormer: Learning Real-time Glass Segmentation using Radar-Depth Fusion | Grover Suhani, Srivastava Astik, Dinesh Viswas, Sharma Avinash, Krishna Madhava | Robotics Research Center, IIIT Hyderabad, India | GlassFormer利用雷达-深度融合实现实时玻璃分割。 | [#628](https://github.com/zitalk/PaperClaw/issues/628) |
| [20260929] CurvSpec: Adaptive Multi-Curvature Learning for Partial Relevant Video Retrieval | Liu Zhen, Li Letian, Wang Jinpeng, Xie Shuzhao, Huang Yuzhi, Jiang Jingyan, Wang Zhi | Tongji University SIGS, Tsinghua University Harbin Institute of SIGS, Tsinghua University；SIGS, Tsinghua University SIGS, Tsinghua University SIGS, Tsinghua University；matching, but they still typically encode all videos in a single fixed- The rapid growth of online video has driven extensive research on；∗ Contributed equally to this research | CurvSpec：自适应多曲率学习用于部分相关视频检索。 | [#629](https://github.com/zitalk/PaperClaw/issues/629) |
| [20260929] Seeing What Should Be Heard: Diagnosing and Repairing Cross-Modal Shortcuts in Omni-Modal LLMs | Ma Yueran, Lin Ronghao | University of Queensland, Brisbane, Australia；Shenzhen University, Shenzhen, China | 诊断并修复全模态LLM中的跨模态捷径问题。 | [#630](https://github.com/zitalk/PaperClaw/issues/630) |
| [20260929] Dual-Mode Low-Rank Learner with Bridge-Prototype Ensemble for Vision-Language Class-Incremental Learning | He Chiyuan, Qiu Zihuan, Meng Fanman, Wang Chao, Chen Liangjiang, Xu Linfeng, Wu Qingbo, Li Hongliang | University of Electronic Science and Technology of China, Chengdu, China；Qiyuan Lab, Beijing, China | 双模式低秩学习与桥原型集成用于视觉-语言类增量学习。 | [#631](https://github.com/zitalk/PaperClaw/issues/631) |
| [20260929] Degeneracy-Orthogonal Geometric Constraints for LiDAR SLAM | Kim Minseo, Kim Yina, Hwang Jinhwa, Alex Junho Lee | Department of Mechanical Systems Engineering, Sookmyung Women's University, 100 Cheongpa-ro 47-gil, Yongsan-gu, Seoul, Republic of Korea | 面向LiDAR SLAM的退化-正交几何约束方法。 | [#632](https://github.com/zitalk/PaperClaw/issues/632) |
| [20260929] Reprogramming Vision-Language Models via Structured Prompt Reparameterization | Li Zizhao, Cai Chengyi, Mohammed Yaqoob Ansari, Liu Feng, West Joseph, Khoshelham Kourosh | University of Melbourne, Melbourne, Australia | 通过结构化提示重参数化重编程视觉语言模型。 | [#633](https://github.com/zitalk/PaperClaw/issues/633) |
| [20260929] ReWorld-Track: A Recursive Event World Model for Language-Guided Multi-Camera Tracking | Wu Haoyang, Han Shoudong, Li Chaoyue, Chen Sijia, Xie Zhenyang, sihan Wang | Huazhong University of Science and Technology；Zhongnan University of Economics and Law | ReWorld-Track：递归事件世界模型用于语言引导多相机跟踪。 | [#634](https://github.com/zitalk/PaperClaw/issues/634) |
| [20260929] Planning Oriented 3D Scene Completion via Coupled TUDF Occupancy Representation Learning from Partial Observations | Yu Tianyou, Zhao Pengfei, Xu Chao | of Control Science and Engineering, Zhejiang University, Hangzhou 310027 | 面向规划的3D场景补全，从部分观测学习耦合TUDF占据表示。 | [#635](https://github.com/zitalk/PaperClaw/issues/635) |
| [20260929] Perception-Inspired Bayesian Causal Fusion for Audiovisual Source Localization | Kyung Yun Lee, Kim Sungnyun, Sebastian J. Schlecht, Oh Tae-Hyun, Välimäki Vesa | Acoustics Lab, Dept. of Information and Communications Eng., Aalto University, Espoo, Finland；Korea Advanced Institute of Science and Technology (KAIST), Daejeon, South Korea；Multimedia Comms. \& Signal Process., Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany | 感知启发的贝叶斯因果融合用于音视频源定位。 | [#636](https://github.com/zitalk/PaperClaw/issues/636) |
| [20260929] DARE to Mitigate Hallucination: Dual-path Auto-Regressive-aware Editing | Lee Jae-Ho, Lee Jeong-Eun, Park Gyeong-Moon | Korea University, Seoul, Republic of Korea | DARE：双路径自回归感知编辑缓解大视觉语言模型幻觉。 | [#637](https://github.com/zitalk/PaperClaw/issues/637) |
| [20260929] Temporal-Aware Fusion for Robust Outdoor LiDAR Localization | Zhu Minghang, Wang Zhijing, Guo Yuxin, Liu Chen, Huang Yongshu, Li Wen, Ao Sheng, Wang Cheng | Fujian Key Laboratory of Urban Fujian Key Laboratory of Urban Fujian Key Laboratory of Urban；Xiamen University Xiamen University Xiamen University；Fujian Key Laboratory of Urban Fujian Key Laboratory of Urban School of Engineering Mathematics；Xiamen University Xiamen University Bristol, United Kingdom；Fujian Key Laboratory of Urban Fujian Key Laboratory of Urban；Xiamen University Xiamen University | 时序感知融合用于鲁棒室外LiDAR定位。 | [#638](https://github.com/zitalk/PaperClaw/issues/638) |
| [20260929] FineART: Fine-grained Annotated Robotic Trajectory Dataset and Vision-Language-Action Model for Bimanual Manipulation | Choghari Jade, Kooijmans Pepijn, Agarwal Mansi, Yusuf Umut Ciftci, Doriwala Aseem, Weaver Catherine, Sivapurapu Mouli, Yang Kai, Lee Jackson, Wolf Thomas, Mannam Pragna | University of Southern California；Stanford University | FineART：细粒度标注机器人轨迹数据集与双臂操作VLA模型。 | [#639](https://github.com/zitalk/PaperClaw/issues/639) |

## 🔎 观察

- 多模态模型正从静态感知转向动态证据构建，想象与重定位成为提升推理可靠性的新路径。
- 效率优化不再仅依赖token重要性，空间结构与几何约束的保留成为VLA与VLM推理的关键考量。

---

Powered by OpenClaw🦞

---

# [20260928](./202609/20260928.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "partial", "checked_at": "2026-09-29T04:37:41+08:00", "unavailable_sources": ["IEEE Xplore"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，部分来源覆盖受限 · 最近检查：2026-09-29 04:37:41（北京时间）

本轮检索候选论文 100 篇；刊会准入通过 0 篇（排除 100 篇）；本轮 LLM 新筛中 0 篇，复用已收录匹配 0 篇；本轮新增入报 0 篇；目标日累计收录 0 篇。当日未检索到符合条件并纳入日报的论文。 部分来源不可用：IEEE Xplore；本次结果不代表完整覆盖。

## ✨ 今日亮点

- 留一点时间给思考，好的问题值得耐心打磨。

## 🔎 检索说明

- 日报日期是论文检索目标日期；最近检查时间是任务实际执行时间。
- 零结果不代表所有来源当天没有新论文，只表示本次未纳入符合条件的论文。
- 同一日期后续补扫会更新这份日报，不重复创建日报 Issue。

---

Powered by OpenClaw🦞

---
