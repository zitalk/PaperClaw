# Daily Reports

最近三天日报（最新在前）：

# [20260909](./202609/20260909.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "degraded", "checked_at": "2026-09-10T17:40:24+08:00", "unavailable_sources": ["Semantic Scholar", "Springer Nature"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，但存在异常 · 最近检查：2026-09-10 17:40:24（北京时间）
本轮检索候选论文 160 篇；刊会准入通过 51 篇（排除 109 篇）；本轮 LLM 新筛中 10 篇，复用已收录匹配 8 篇；本轮新增入报 10 篇；目标日累计收录 18 篇。

部分来源不可用：Semantic Scholar、Springer Nature；本次结果不代表完整覆盖。 今日论文呈现多模态融合与跨域感知的显著趋势。视觉语言模型研究聚焦模态差距建模、嵌入扰动鲁棒性及视觉令牌剪枝效率；遥感与工业场景中，多传感器融合、开放世界检测和小目标识别持续深化。三维生成与重建方向涌现测试时引导、NeRF与3DGS双向蒸馏等新方法。此外，合成数据生成与多模态医学分割的鲁棒性也受到关注，整体体现从单一模态向多源协同、从静态推理向自适应优化的演进。

## ✨ 今日亮点

- 视觉语言模型研究从模态差距理论建模延伸至令牌剪枝与嵌入鲁棒性优化
- 遥感与工业感知强调多传感器融合、开放世界检测及小目标识别能力提升
- 三维生成与重建涌现测试时引导、NeRF与3DGS双向蒸馏等跨表示融合方法

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260909] UOT-Gap: A Variational Principle for the Modality Gap in Vision-Language Models via Unbalanced Optimal Transport | Yang Zonglin, Ma Huilan, Zheng Xudan, Xie Yuejun | Guangdong Police College | 提出非平衡最优传输变分原理，建模视觉语言模型模态差距并提升检索性能。 | [#348](https://github.com/zitalk/PaperClaw/issues/348) |
| [20260909] Beyond Similarity: Foundation Models as an Efficient Backbone for Training-Free Composed Video Retrieval | Demidov Dmitry, Muhammad Zaigham Zaheer, Thawakar Omkar, Abdelrahman Mohamed Shaker, Anwer Rao | Mohamed bin Zayed University of Artificial Intelligence, UAE | 利用基础模型作为免训练骨干，实现组合视频检索的查询自适应推理。 | [#349](https://github.com/zitalk/PaperClaw/issues/349) |
| [20260909] StreetDiff: Multi-view Street Scenes Generation via Cross-view Consistent Multi-view Stable Diffusion with Structure Prompts | Zhang Qi, Wang Yanyifan, Zhang Weiyuan, Huang Hui | College of Computer Science and Software Engineering, Shenzhen University, China | 基于跨视图一致多视图扩散与结构提示，生成多视角街景图像。 | [#350](https://github.com/zitalk/PaperClaw/issues/350) |
| [20260909] CLFTv2: Efficient Camera-LiDAR Fusion for Semantic Segmentation via Hierarchical Feature Pyramids | Tahves Toomas, Bellone Mauro, Sell Raivo | Department of Mechanical and Industrial Engineering, Tallinn University of Technology, Tallinn, Estonia (；the FinEst Centre for Smart Cities, Tallinn University of Technology, Tallinn, Estonia；Universitas Mercatorum, Rome, Italy | 通过层次特征金字塔实现高效相机-激光雷达融合语义分割。 | [#351](https://github.com/zitalk/PaperClaw/issues/351) |
| [20260909] From Pixels to Hierarchical Sequences: Quadtree Mask Encoding for Vision-Language Binary Change Detection | An Xiao, Zhang Ruikang, Zhong Chen, Shen Xuli, Sun Jiaxing, Wu Jiang, He Wei | Wuhan University；Peking University；Shanghai Artificial Intelligence Laboratory | 采用四叉树掩码编码将变化检测转化为视觉语言层次序列生成任务。 | [#352](https://github.com/zitalk/PaperClaw/issues/352) |
| [20260909] Layerwise Tunable Lifting Scheme for the Convolutional Neural Network | Yovkochov Abdumannon, Le An, Seo Sungbal, Bae You-Suk, Nguyen Truong | Electrical and Computer Engineering Department, University of California San Diego, La Jolla, CA 92093, USA；Department of Computer Engineering, Tech University of Korea, Siheung 15073, Korea | 提出层间可调提升方案，将双正交小波滤波器嵌入卷积神经网络。 | [#353](https://github.com/zitalk/PaperClaw/issues/353) |
| [20260909] MethaneFuse: Learning from Multi-Sensor Satellite Observations for Methane Plume Detection | Wang Yuyao, Juliana Y. Leung, Niu Di | Department of Electrical and；University of Alberta；Department of Civil and | 融合多传感器卫星观测，在部分传感器缺失下检测甲烷羽流。 | [#354](https://github.com/zitalk/PaperClaw/issues/354) |
| [20260909] Hyperbolic Geometry for Open-World Object Detection in Remote Sensing Imagery | Li Wuzhou, Zhou Jiawei, Wang Shenghang, Li Xiang | School of Computer Science and Artificial Intelligence, Wuhan Textile University, Wuhan, China (；the Electronic Information School, Wuhan University, Wuhan, China (；the Electrical and Computer Engineering, Ohio State University, Columbus, OH, USA (；School of Artificial Intelligence, Wuhan University, Wuhan, China ( | 利用双曲几何建模遥感图像开放世界目标检测与增量学习。 | [#355](https://github.com/zitalk/PaperClaw/issues/355) |
| [20260909] Guiding Image-to-3D Generation with Test-Time Partial Observations | Chen Jerred, Weber Simon, Clark Ronald | University of Oxford | 在测试时引入部分观测引导，提升图像到三维生成的几何保真度。 | [#356](https://github.com/zitalk/PaperClaw/issues/356) |
| [20260909] Beyond One-Size-Fits-All: Sample-Adaptive Strategy Routing for Vision Token Pruning in MLLMs | Liang Haiji, Zhou Pengfei, Wan Zhenglin, Wang Wei, You Yang, Zhao Wangbo | National University of Singapore；InfRec, Cardinal AI Lab；The Hong Kong University of Science and Technology | 提出样本自适应策略路由，实现多模态大模型视觉令牌高效剪枝。 | [#357](https://github.com/zitalk/PaperClaw/issues/357) |
| [20260909] Geometry Without Coordinates: LiDAR Diffusion as a 3D Feature Bridge | Doğan Samed, Leuze Nico, Schöttl Alfred | Department of Electrical Engineering and Information Technology；Munich University of Applied Sciences | 将激光雷达扩散作为三维特征桥，连接二维基础模型与点云语义分割。 | [#358](https://github.com/zitalk/PaperClaw/issues/358) |
| [20260909] SynThermFace: Amplifying Limited Paired Data for Visible-Thermal Face Recognition via Synthetic Data Generation | George Anjith, Unal Adam, Marcel Sebastien | Idiap Research Institute；University of Lausanne (UNIL) | 利用扩散模型合成数据，缓解可见光-热红外人脸识别配对数据稀缺。 | [#359](https://github.com/zitalk/PaperClaw/issues/359) |
| [20260909] Isotropic Embedding Perturbations for Robust Vision Language Encoders | Choi Hyesong, Kim Daeun, Park Song, Kim Taekyung, Heo Byeongho, Yun Sangdoo, Min Dongbo, Han Dongyoon | This work was carried out during Hyesong Choi's internship at NAVER AI Lab；Soongsil Univ；NAVER AI Lab | 通过各向同性嵌入扰动增强视觉语言编码器的跨模态对齐鲁棒性。 | [#360](https://github.com/zitalk/PaperClaw/issues/360) |
| [20260909] When Fusion Fails: Corruption-Aware Rebalanced Fusion for Multi-Modal Medical Image Segmentation | Pei Yuchen, Hu Xiaoyu, Zou Yixiong, Hu Dingwen, Chu Hui, Ma Yutao, Qiu Shijun, Li Gang | Central China Normal University Wuhan China；Huazhong University of Science and Technology Wuhan China；Guangzhou University of Chinese Medicine Guangzhou China；The First Affiliated Hospital of Guangzhou University of Chinese Medicine Guangzhou China；University of North Carolina, Chapel Hill Chapel Hill United States | 针对多模态医学分割中的特征损坏，提出损坏感知重平衡融合策略。 | [#361](https://github.com/zitalk/PaperClaw/issues/361) |
| [20260909] ScopeMamba-YOLO: Widening the Perceptual Scope Inward and Outward for Small Object Detection in Remote Sensing Imagery | Fan Junjie, Mai Yijun, Wei Linduo, Rao Jiayu, Bao Junmin, Jin Qiushi, Li Guijia, Qi Yong | School of Intellectual Property, Nanjing University of Science and Technology, Nanjing, China (；School of Computer Science and Engineering, Nanjing University of Science and Technology, Nanjing, China (；School of Economics and Management, Nanjing University of Science and Technology, Nanjing, China ( | 结合Mamba与YOLO扩展感知范围，提升遥感小目标检测性能。 | [#362](https://github.com/zitalk/PaperClaw/issues/362) |
| [20260909] LogiScope-VQA: Benchmarking Vision-Language Models for Logistics Hazard Identification in Industrial Scenarios | Zhou Hanjing, Yin Mingze, Lian Ying, Ma Jun, Hsieh Chang-Yu, Zhou Yanbing | Zhejiang University | 构建物流危险识别视觉语言基准，评估工业场景多模态推理能力。 | [#363](https://github.com/zitalk/PaperClaw/issues/363) |
| [20260909] VFNet: Multi-View Spatio-Temporal Model for Void Fraction Estimation in Gas-Liquid Two-Phase Flow | Md Adnan Faisal Hossain, Rajeev Raghav, Nishant Kumar, Justin A Weibel, Kumar Satish, Zhu Fengqing | Elmore Family School of Electrical and Computer Engineering, Purdue University；School of Mechanical Engineering, Purdue University；School of Mechanical Engineering, Georgia Institute of Technology | 提出多视角时空模型，从气液两相流图像估计空隙率。 | [#364](https://github.com/zitalk/PaperClaw/issues/364) |
| [20260909] RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting | Wang YuanHang, Cao Xin | University of Technology Sydney | 在NeRF与3D高斯泼溅间建立可靠性路由双向蒸馏框架。 | [#365](https://github.com/zitalk/PaperClaw/issues/365) |

## 🔎 观察

- 视觉语言模型研究正从表征对齐转向模态差距理论建模与推理效率优化，理论深度与工程实用性并重。
- 遥感与工业感知普遍采用多传感器融合与开放世界设定，反映真实部署中对鲁棒性和泛化性的迫切需求。

---

Powered by OpenClaw🦞

---

# [20260908](./202609/20260908.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "degraded", "checked_at": "2026-09-09T20:47:23+08:00", "unavailable_sources": ["Semantic Scholar", "Springer Nature", "IEEE Xplore"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 0} -->

## 📌 今日概况

检索完成，但存在异常 · 最近检查：2026-09-09 20:47:23（北京时间）
本轮检索候选论文 138 篇；刊会准入通过 64 篇（排除 74 篇）；本轮 LLM 新筛中 25 篇，复用已收录匹配 21 篇；本轮新增入报 25 篇；目标日累计收录 46 篇。

部分来源不可用：Semantic Scholar、Springer Nature、IEEE Xplore；本次结果不代表完整覆盖。 今日研究聚焦于视觉-语言模型（VLM）在具身智能、无人机导航和场景理解中的深度应用，同时涵盖3D重建、多模态感知与医学影像分析。多篇工作探索VLM与机器人控制的结合，强调零样本泛化与安全规划。此外，扩散模型、高斯泼溅等生成技术持续推动动态场景重建与深度估计的进步。跨模态融合与不确定性量化成为提升系统鲁棒性的关键手段，整体呈现从感知到决策的端到端智能化趋势。

## ✨ 今日亮点

- VLM驱动具身智能与导航成为热点
- 3D重建与高斯泼溅技术持续演进
- 跨模态融合与零样本泛化受关注

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260908] TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model | Li Anqi, Chen Yuxin, Li Zhaobo, Cao Zhuo, Ren Junli, Tomizuka Masayoshi, Shah Dhruv | University of California, Berkeley；Peking University；Tsinghua University；University of Hong Kong；Princeton University | 提出TANGO模型，利用全身VLA实现人形机器人在杂乱环境中的导航。 | [#300](https://github.com/zitalk/PaperClaw/issues/300) |
| [20260908] Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild | Teng Fei, Wu Sheng, Duan Mengfei, Zhao Guoqiang, Ma Junhui, Luo Kai, Li Siyu, Shi Hao, Li Zhiyong, Yang Kailun | School of Artificial Intelligence and Robotics and the National Engineering Research Center of Robot Visual Perception and Control Technology, Hunan University, China；School of Automation and Electrical Engineering, Zhejiang University of Science and Technology, China；State Key Laboratory of Extreme Photonics and Instrumentation, Zhejiang University, China | Spheriverse利用球面观测进行3D场景理解，支持检测与占用预测。 | [#301](https://github.com/zitalk/PaperClaw/issues/301) |
| [20260908] DXPR: Depth-Based Vision-LiDAR Cross-Modal Place Recognition Using Vision Foundation Models | Han Yungsoo, Jang Youngseok, Roh Seungwon, Seo Jeongyeon, H. Jin Kim | Department of Aerospace Engineering, Seoul National Universuch as bird’s-eye-view (BEV) or range images so that | DXPR基于深度图像表示实现视觉-激光雷达跨模态位置识别。 | [#302](https://github.com/zitalk/PaperClaw/issues/302) |
| [20260908] Prior-free relative 6D pose estimation of multiple object instances | Khodabandehloo Behdad, Caraffa Andrea, Boscaini Davide, Poiesi Fabio | University of Trento, Trento, Italy | 提出无先验的多实例物体相对6D姿态估计方法。 | [#303](https://github.com/zitalk/PaperClaw/issues/303) |
| [20260908] EgoSIS: From Factorized Visual Ego-Transitions to Motion-Canonical Spatial Evidence for UAV Reasoning | Yang Jingpu, Ji Fengxian, Cui Mingxuan, Sun Yilin, Zhang Hang, Zhu Jianhua, Wang Yufeng | Beihang University, Beijing, China；Zhongguancun Academy, Beijing, China；Northeastern University, Shenyang, China；Technology and Engineering Center for Space Utilization, Chinese Academy of Sciences | EgoSIS通过分解自我运动为UAV视频问答提供空间证据。 | [#304](https://github.com/zitalk/PaperClaw/issues/304) |
| [20260908] DSE-VTG: Dual-Side Enhancement for Training-Free Video Temporal Grounding | Cao Zhuo, Zhang Bingqing, Wang Sen, Li Xue | University of Queensland, Australia | DSE-VTG采用双端增强实现免训练视频时间定位。 | [#305](https://github.com/zitalk/PaperClaw/issues/305) |
| [20260908] Leveraging Visual and Geometric Priors for Metric-scale and Complete Vehicle Gaussian Reconstruction from Limited Views | Miao Jinyu, Li Jiusi, He Yifei, Long Miao, Jiang Kun, Yang Mengmeng, Yang Diange | School of Vehicle and Mobility and the State Key Laboratory of Intelligent Green Vehicle and Mobility, Tsinghua University, Beijing, China | 利用视觉几何先验从有限视角重建车辆高斯模型。 | [#306](https://github.com/zitalk/PaperClaw/issues/306) |
| [20260908] MorphoOrgaAgent: A Foundation-Model-Based Multi-Agent System for Autonomous Organoid Analysis | Zhang Hanyi, Hoermann Maximilian, Lion J. Gleiter, Xu Yiling, Bettina Katalin Budai, Kauczor Hans-Ulrich, Marr Carsten, Peng Tingying | Helmholtz AI, Helmholtz Munich - German Research Center for Environmental；School of Computation, Information and Technology, Technical University of；Department of Diagnostic and Interventional Radiology, University Hospital；Institute of AI for Health, Helmholtz Munich - German Research Center for；Department of Medicine III, Ludwig-Maximilian-University Hospital, Munich；Department of Physics, Ludwig-Maximilian-University, Munich, Germany | MorphoOrgaAgent基于基础模型多智能体实现类器官自动分析。 | [#307](https://github.com/zitalk/PaperClaw/issues/307) |
| [20260908] CrossRAFT: Cross-Domain Complex-Valued Feature Extraction for Ultrasound Motion Estimation | Leng Yang, Tang Yuchen, Yiu Kai-Hang, Wu Yik-Chung, Lee Wei-Ning | Department of Electrical and Computer Engineering, The University of Hong Kong, Hong Kong. (；University of Hong Kong-Shenzhen Hospital and Department of Medicine, The University of Hong Kong, Hong Kong (；Department of Electrical and Computer Engineering；School of Biomedical Engineering, The University of Hong Kong, Hong Kong. ( | CrossRAFT提取跨域复数特征用于超声运动估计。 | [#308](https://github.com/zitalk/PaperClaw/issues/308) |
| [20260908] MFVINS: Multiple Fisheye Camera-Based Visual Inertial System | Jang Eunseong, Chung YuJin, Sang Jun Lee, Yoon Jihyun, Jo HyungGi | Division of Electronic Engineering, Jeonbuk National University, Jeonju, South Korea | MFVINS融合多鱼眼相机与IMU构建视觉惯性系统。 | [#309](https://github.com/zitalk/PaperClaw/issues/309) |
| [20260908] Estimating Semantic Ambiguity via Gaussian Context Distributions for VLM-Driven Traversability Analysis | Häuselmann Ramona, Mario A.V. Saucedo, Kanellakis Christoforos, Nikolakopoulos George | Robotics & AI Team, Department of Computer, Electrical and Space；Engineering, Luleå University of Technology, Luleå SE-97187, Sweden | 通过高斯上下文分布估计语义模糊度以分析可通行性。 | [#310](https://github.com/zitalk/PaperClaw/issues/310) |
| [20260908] STSG-VQA: Evidence-Grounded Temporal Question Answering from Surgical Spatio-Temporal Scene Graphs | Li Jing, Sarikaya Duygu | School of Computer Science, University of Leeds, UK ( | STSG-VQA利用时空场景图进行手术视频时间问答。 | [#311](https://github.com/zitalk/PaperClaw/issues/311) |
| [20260908] To Adapt or Not to Adapt? Selective Adaptation for Vision-Language Models | Jiang Siru, Liang Yuwei, Liang Jian, He Ran, Tan Tieniu | School of Advanced Interdisciplinary Sciences, University of Chinese Academy of；NLPR & MAIS, Institute of Automation, Chinese Academy of Sciences, China；School of Artificial Intelligence, University of Chinese Academy of Sciences, China；Nanjing University, China | 提出选择性适应策略以提升视觉-语言模型的分布偏移鲁棒性。 | [#312](https://github.com/zitalk/PaperClaw/issues/312) |
| [20260908] Segment Any Motion with Radar: Robust Multimodal Moving-Object Segmentation and Tracking | Wang Jue, Wang Xuan, Zhou Hao, Zhou Ruixiang, Zhou Yixuan, Yuan Tianshuo, Ma Jieming, Zhang Jie, Luo Fei | Harbin Institute of Technology, Shenzhen, China；Great Bay University, Dongguan, China；Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Shenzhen, China | 结合雷达与RGB-热成像实现多模态运动目标分割跟踪。 | [#313](https://github.com/zitalk/PaperClaw/issues/313) |
| [20260908] CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs | Bui Nhat-Tan, Elangovan Varshini, Arun Reddy Anugu, Mohan Sreyas, Ye Wei, Wang Dilin, Huang JQ, Ranjan Rakesh, Chharia Aviral, Fernando De la Torre | Carnegie Mellon University | CoVeR基于覆盖率剪枝令牌以提升多视图3D推理效率。 | [#314](https://github.com/zitalk/PaperClaw/issues/314) |
| [20260908] A Multi-Modal Perception Pipeline for Object Detection and Tracking in Autonomous Racing | Malvezzi Davide, Pestarino Michele, Cavicchioli Vittoria, Valentina La Gamba, Severi Silvia, Bagni Fabio, Bartoli Luca, Bosi Massimiliano, Gatti Francesco, Verucchi Micaela, Raji Ayoub, Bertogna Marko | University of Modena and Reggio Emilia, Modena, Italy | 面向自动驾驶赛车构建多模态感知流水线用于目标检测跟踪。 | [#315](https://github.com/zitalk/PaperClaw/issues/315) |
| [20260908] EdMCGS: Event-Driven Markov Chain Gaussian Splatting for Extreme-Low-Frame-Rate Dynamic Scene Reconstruction | Wang Yuzhong, Wang Wenmin, Yu Xinxing | Macau University of Science and Technology | EdMCGS利用事件驱动马尔可夫链重建极低帧率动态场景。 | [#316](https://github.com/zitalk/PaperClaw/issues/316) |
| [20260908] MARS-CLIP: Multi-Resolution and Attention Refined Zero-Shot Image Segmentation | Saito Nagito, Ito Shintaro, Ito Koichi, Aoki Takafumi | Graduate School of Information Sciences, Tohoku University, Japan | MARS-CLIP通过多分辨率注意力细化实现零样本分割。 | [#317](https://github.com/zitalk/PaperClaw/issues/317) |
| [20260908] CS-CLIP: Compositional Scene Graph-guided CLIP for Robust Compositional Reasoning | Jeong SeongJun, Jung Minjoon, Woo Suk Choi, Jang Youwon, Zhang Byoung-Tak | Seoul National University | CS-CLIP引入场景图指导以增强组合推理鲁棒性。 | [#318](https://github.com/zitalk/PaperClaw/issues/318) |
| [20260908] Dual-Layer Semantic-Spatial Belief Mapping for Aerial Object Goal Navigation | Xiao Jianqiang, Deng Xiang, Sun Yuexuan, Wu Yanjin, Yan Wenbiao, Nie Liqiang | observations, but their frame-level outputs are often noisy, Existing embodied navigation research has advanced along | 双图层语义-空间信念地图用于无人机目标导航。 | [#319](https://github.com/zitalk/PaperClaw/issues/319) |
| [20260908] Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation | Pavlovic Igor, Wandel Thiemo, Obukhov Anton, Bartolomei Luca, Davydov Andrey, Tosi Fabio, Poggi Matteo, Süsstrunk Sabine, Dai Dengxin | IGOR PAVLOVIC∗†, EPFL, HUAWEI Bayer Lab, Switzerland；THIEMO WANDEL∗, HUAWEI Bayer Lab, Switzerland；ANTON OBUKHOV§, HUAWEI Bayer Lab, Switzerland；LUCA BARTOLOMEI, University of Bologna, Italy；ANDREY DAVYDOV, HUAWEI Bayer Lab, Switzerland；FABIO TOSI, University of Bologna, Italy；MATTEO POGGI, University of Bologna, Italy；DENGXIN DAI, HUAWEI Bayer Lab, Switzerland；Authors’ Contact Information: Igor Pavlovic, EPFL, HUAWEI Bayer Lab, Switzerland；Thiemo Wandel, HUAWEI Bayer Lab, Switzerland; Anton Obukhov, HUAWEI Bayer CCS Concepts: • Computing methodologies → Scene understanding；HUAWEI Bayer Lab, Switzerland; Fabio Tosi, University of Bologna, Italy; Matteo；Poggi, University of Bologna, Italy; Sabine Süsstrunk, EPFL, Switzerland; Dengxin Dai, Additional Key Words and Phrases: Monocular depth estimation, surface nor-；HUAWEI Bayer Lab, Switzerland | Marigold V2重新审视扩散Transformer用于单目深度估计。 | [#320](https://github.com/zitalk/PaperClaw/issues/320) |
| [20260908] Studying Image Tokenizers as Visual Languages in Unified Multimodal Models | Li Siting, Wang Zhengyang, Simon Shaolei Du, Chen Xi, Liu Yang | University of Washington | 研究图像分词器作为统一多模态模型中的视觉语言。 | [#321](https://github.com/zitalk/PaperClaw/issues/321) |
| [20260908] GoDeep: Annotation-Free Open-Vocabulary 3D Scene Understanding via Language-Space Lifting | Betsas Thodoris, Doulamis Anastasios, Georgopoulos Andreas | Laboratory of Photogrammetry, School of Rural, Surveying and Geoinformatics Engineering, NTUA | GoDeep通过语言空间提升实现免标注开放词汇3D分割。 | [#322](https://github.com/zitalk/PaperClaw/issues/322) |
| [20260908] A Joint 2D-3D Statistical Shape Model for Orthopedic Reconstruction | Florence Dell’Aniello Picard, Poudel Pranav, Shehata Nairouz, Lavoie Frédéric, Lombaert Herve | Mila - Quebec AI Institute, Canada；CHUM - University of Montreal Hospital, Canada | 联合2D-3D统计形状模型用于骨科重建。 | [#323](https://github.com/zitalk/PaperClaw/issues/323) |
| [20260908] Concentrate After Imagination: Text-Conditioned Evidence Grounding for Partially Relevant Video Retrieval | Cheng Shuaiqi, You Siyu, Wu Yanbi, Chen Yuxi, Zhang Jiahao, Hu Xuming | The Hong Kong University of Science and Technology (Guangzhou)；University of Electronic Science and Technology of China；The Hong Kong University of Science and Technology | 文本条件证据定位用于部分相关视频检索。 | [#324](https://github.com/zitalk/PaperClaw/issues/324) |
| [20260908] FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute | Xia Hongchi, Cheng Tianhang, Ma Wei-Chiu, Wang Shenlong | University of Illinois Urbana-Champaign；Cornell University | FIRE3D实现分钟级前馈交互式3D场景重建。 | [#325](https://github.com/zitalk/PaperClaw/issues/325) |
| [20260908] Interpretable Hyperspectral Unmixing Framework with Fixed Endmember Prior and Structured Residual Refinement | Guan Ziyi, Zhang Jianping, Liu Qian | of Hunan Province (No. 2025 JJ60883); the Hunan Provincial College Students’ Entrepreneurship Training Program (No. S202510530147 X); and the National College | 提出可解释高光谱解混框架，含固定端元先验与残差细化。 | [#326](https://github.com/zitalk/PaperClaw/issues/326) |
| [20260908] AXS-Net: Interpretable Deep Unfolding for Hyperspectral Image Denoising via Spectral Basis Unmixing and Structured Noise Refinement | Guan Ziyi, Zhang Jianping, Yang Zheng | Xiangtan University, Xiangtan, Hunan, China | AXS-Net通过谱基解混与噪声细化进行高光谱去噪。 | [#327](https://github.com/zitalk/PaperClaw/issues/327) |
| [20260908] Compensating for Scarce Historical Images in Cross-Domain Cultural Heritage Retrieval Using Synthetic Aging | Iwanowski Marcin, Mazgaj Adam, Górski Ferdynand, Szymoniak Sabina | Inst.of Engineering and Technology, Faculty of Physics, Astronomy and Informatics, Nicolaus Copernicus University, ul.Grudziądzka 5, 87-100 Toruń, POLAND；Institute of Control and Industrial Electronics, Warsaw University of Technology, ul.Koszykowa 75, 00-662 Warszawa, POLAND；Department of Computer Science, Czestochowa University of Technology, ul.Dabrowskiego 69, 42-201 Czestochowa, POLAND | 利用合成老化补偿历史图像稀缺的跨域检索。 | [#328](https://github.com/zitalk/PaperClaw/issues/328) |
| [20260908] CASD: Chunk-Aligned Semantic Distillation for Multi-StageRobot Manipulation | Ding Tinghe, Li Jiahao, Wang He | Ant Group | CASD采用块对齐语义蒸馏用于多阶段机器人操作。 | [#329](https://github.com/zitalk/PaperClaw/issues/329) |
| [20260908] Layer Selection in VLMs for Zero-Shot OOD Detection via Multi-Resolution Entropy Estimation | Shyam Nandan Rai, Francesco Di Salvo, Doerrich Sebastian, Ledig Christian | Princeton University, Princeton NJ 08544, USA Springer Heidelberg, Tiergartenstr. 17；ABC Institute, Rupert-Karls-University Heidelberg, Heidelberg, Germany；xAILab Bamberg, University of Bamberg, Bamberg, Germany | 基于多分辨率熵估计选择VLM层以实现零样本OOD检测。 | [#330](https://github.com/zitalk/PaperClaw/issues/330) |
| [20260908] AURORA: Active Uncertainty-Driven Re-Orientation for In-Hand Reconstruction | Zhao Feiyu, Li Yuetong, Xiao Chenxi | School of Information Science School of Information Science；ShanghaiTech University, China ShanghaiTech University, China；School of Information Science；ShanghaiTech University, China | AURORA通过不确定性驱动重定向进行手内重建。 | [#331](https://github.com/zitalk/PaperClaw/issues/331) |
| [20260908] PAPR-Aware Multimodal Token Transmission in MLLM-Based Multiuser Networks | Trabelsi Molka, Zayani Rafik | Univ Rennes, CNRS, IETR, UMR 6164, F-35000 Rennes, France | 研究MLLM多用户网络中PAPR感知的多模态令牌传输。 | [#332](https://github.com/zitalk/PaperClaw/issues/332) |
| [20260908] Safe Task Planning with Long-Term Graph Memory for Embodied Agents | Li Siyuan, Lang Taiyan, Yan Aoqi, Yu Jia, Liu Feifan, Du Yihan, Zheng Yu, Wang Xun, Liu Peng | Faculty of Computing Faculty of Computing；Harbin Institute of Technology Harbin Institute of Technology；Faculty of Computing Engineering Systems and Design；Harbin Institute of Technology Singapore University of Technology and Design；Academy of CASIC Academy of CASIC；Faculty of Computing；Harbin Institute of Technology | 利用长期图记忆实现具身智能体的安全任务规划。 | [#333](https://github.com/zitalk/PaperClaw/issues/333) |
| [20260908] AirAnchor: Bridging Local and Global Spatial Information for Zero-Shot Aerial Vision-and-Language Navigation | Fan Shanwei, Zhang Bin, Xu Zhiwei, Teng Yingxuan, Dai Siqi, Cheng Lin, Fan Guoliang | National Key Laboratory of Cognition and Decision Intelligence for Complex Systems；Institute of Automation, Chinese Academy of Sciences, Beijing, China；School of Artificial Intelligence, University of Chinese Academy of Sciences, Beijing, China；School of Artificial Intelligence, Shandong University, Jinan, Shandong, China | AirAnchor桥接局部与全局空间信息用于零样本空中导航。 | [#334](https://github.com/zitalk/PaperClaw/issues/334) |
| [20260908] Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method | Yu Boao, Chen Zimo, Rao Junreng, Hu Yue, Zhu Zhengqiu, Zhao Yong, Ju Rusheng | National University of Defense Technology；National Key Laboratory of Digital Intelligent Modeling and Simulation | 提出空地协同目标搜索的基准、数据集与智能体方法。 | [#335](https://github.com/zitalk/PaperClaw/issues/335) |
| [20260908] From Coordinates to Candidate Regions: Temporal Change Localization via Region Selection in Remote Sensing Multimodal LLMs | Chung Juwan, Park Sungjune, Kim Yeongyun, Yong Man Ro | Integrated Vision Language Lab, KAIST, South Korea | 从坐标到候选区域，遥感多模态LLM进行时间变化定位。 | [#336](https://github.com/zitalk/PaperClaw/issues/336) |
| [20260908] GALoc: Gravity Aligned Wireframes for Depth-Free Monocular Floorplan Localization | Han Jeahn, Kim Minji, Sohn Jeongbin, Park Jonghyeok, Wüest Matthias, Kim Pyojin | Zurich University of Applied Sciences | GALoc利用重力对齐线框实现无深度单目楼层定位。 | [#337](https://github.com/zitalk/PaperClaw/issues/337) |
| [20260908] Do Input-Level Defenses Transfer to Observation-Level Attacks on VideoLLMs? | Zhu Bangshuo, Song Wei, Cao Yuxin, Wu Yuezhong, Liu Zhiquan, Li Yuekang, Xue Jingling | School of Computer Science and Engineering, University of New South Wales, New South Wales, Australia (；School of Information and Communication Technology, Griffith University, Queensland, Australia (；School of Computing, National University of Singapore, Singapore, Singapore (；College of Computer and Data Science, Fuzhou University, Fuzhou Province, China (；College of Cyber Security, Jinan University, Guangdong Province, China ( | 研究输入级防御对视频LLM观测级攻击的迁移性。 | [#338](https://github.com/zitalk/PaperClaw/issues/338) |
| [20260908] Supervised Cross-Modal Feature Alignment for Zero-Wearable Freezing of Gait Detection in Parkinsonism | Singh Aryan, Biswas Chandan | A prototype of the implementation is available for research purposes at | 监督跨模态特征对齐用于无穿戴帕金森冻结步态检测。 | [#339](https://github.com/zitalk/PaperClaw/issues/339) |
| [20260908] From Glance to Scrutiny: Progressive Distortion Reasoning for Fine-Grained Image Quality Assessment | Zhang Aoting, Gao Mingze, Yang Dongbao, Chen Longyi, Zhang Daoxin, Wu Yi, Hu Yao, Zhou Yu | IIE, Chinese Academy of Sciences；Nankai University；University of Chinese Academy of Sciences | 渐进失真推理用于细粒度图像质量评估。 | [#340](https://github.com/zitalk/PaperClaw/issues/340) |
| [20260908] Human-Centric Image Captioning with Subject-Centered Spatial Understanding | Li Bozhou, Zhang Jiahang, Ding Yue, Guan Yushuo, Zeng Bohan, Ji Yiyan, Chen Xinlong, Shi Yang, Dai Yifan, Wang Yuran, Tong Chengzhuo, Wan Pengfei, Zhang Yuanxing, Zhang Wentao | Human-Centric Image Captioning with Subject-Centered Spatial；Peking University Peking University Chinese Academy of Sciences Kling Team；Peking University Nanjing University Chinese Academy of Sciences Peking University；Shanghai Jiao Tong University Peking University Peking University Kling Team；Kling Team Peking University | 以主体为中心的空间理解生成人类中心图像描述。 | [#341](https://github.com/zitalk/PaperClaw/issues/341) |
| [20260908] Dreaming in Flow: Generative Grounding Feedback for Self-Evolving Unified Multimodal Models | Hao Ke, Liang Yuanzhi, Chen Tingxi, Li Rui, Huang Haibin, Zhang Chi, Gu Yun, Li Xuelong | Shanghai Jiao Tong University, Shanghai, China；Institute of Artificial Intelligence, China Telecom (TeleAI), Shanghai, China；University of Science and Technology of China, Hefei, China | Dreaming in Flow通过生成反馈实现多模态模型自进化。 | [#342](https://github.com/zitalk/PaperClaw/issues/342) |
| [20260908] 3DWay: Generalizing Robot Manipulation via 3D Consistent Waypoints | Huang Ziqin, Li Yingyue, Zhang Chenyangguang, Zhang Ruida, Chen Yuxin, Wang Gu, Liu Xingyu, Tomizuka Masayoshi, Ji Xiangyang | Tsinghua University；University of California, Berkeley | 3DWay通过3D一致路点提升机器人操作泛化能力。 | [#343](https://github.com/zitalk/PaperClaw/issues/343) |
| [20260908] Observe Before You Alert: Adaptive Driver Alerting with Vision-Language Models | Wang Yuhang, Li Lingyao, Zhou Hao | Department of Civil Engineering School of Information；University of South Florida United States University of South Florida United States；Department of Civil Engineering；University of South Florida United States | 基于视觉-语言模型的自适应驾驶员警报系统。 | [#344](https://github.com/zitalk/PaperClaw/issues/344) |
| [20260908] Hyperspectral Anomaly Detection via Group Sparse Low-Rank Tensor Factorization With Automatic Anomaly Grouping | Yu Quan, Dai Yu-Hong, Zhang Xiongjun | School of Mathematics and Statistics, Central China Normal University, Wuhan, China；the Key Laboratory of Nonlinear Analysis and Applications (Ministry of Education), Central China Normal University (；State Key Laboratory of Mathematical Sciences, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, China；School of Mathematical Sciences, University of Chinese Academy of Sciences, Beijing, China ( | 组稀疏低秩张量分解用于高光谱异常检测。 | [#345](https://github.com/zitalk/PaperClaw/issues/345) |

## 🔎 观察

- VLM正从感知走向决策，与机器人控制、导航深度融合，但安全性与泛化仍是挑战。
- 3D重建技术向动态、稀疏视角场景延伸，高斯泼溅与扩散模型成为主流工具。

---

Powered by OpenClaw🦞

---

# [20260907](./202609/20260907.md)
<!-- paperclaw-report: zitalk/PaperClaw -->
<!-- paperclaw-run: {"status": "degraded", "checked_at": "2026-09-09T16:03:54+08:00", "unavailable_sources": ["Springer Nature", "IEEE Xplore"], "unconfigured_sources": [], "filter_fallback": false, "failed_papers": 14} -->

## 📌 今日概况

检索完成，但存在异常 · 最近检查：2026-09-09 16:03:54（北京时间）
本轮检索候选论文 149 篇；刊会准入通过 75 篇（排除 74 篇）；本轮 LLM 新筛中 21 篇，复用已收录匹配 4 篇；本轮新增入报 7 篇；目标日累计收录 11 篇。

部分来源不可用：Springer Nature、IEEE Xplore；本次结果不代表完整覆盖。 有 14 篇匹配论文处理失败，请查看日报失败明细。 本日报汇总目标日期内累计收录的论文。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260907] Context-aware and View-consistent Learning for Multi-view Action Recognition | Trung Thanh Nguyen, Kawanishi Yasutomo, Komamizu Takahiro, Ide Ichiro | 暂无 | 聚焦Multi-view Action Recognition、Context-aware Learning，给出可复现的模型与评测方案。 | [#108](https://github.com/zitalk/PaperClaw/issues/108) |
| [20260907] DAFormer: Enhancing Infrared–Visible UAV Perception via Degradation-Aware Mixture-of-Experts Model | Su Weijian, Han Yuqi, Zheng Zhihui, Wang Zhenwei, Zhang Songqian, Huang Yongdong, Zhang Qiang | 暂无 | 聚焦Unmanned Aerial Vehicles、Mixture-of-Experts，给出可复现的模型与评测方案。 | [#109](https://github.com/zitalk/PaperClaw/issues/109) |
| [20260907] Dual-branch Prompting for Multimodal Machine Translation | Wang Jie, Yang Zhendong, Zong Liansong, Zhang Xiaobo, Wang Dexian, Zhang Ji | 暂无 | 聚焦Multimodal Machine Translation、Dual-Branch Prompting，给出可复现的模型与评测方案。 | [#111](https://github.com/zitalk/PaperClaw/issues/111) |
| [20260907] Learning Speaker-Invariant Visual Features for Lipreading | Li Yu, Xue Feng, Li Shujie, Zhang Jinrui, Guo Dan, Liu Zhi, Hong Richang | 暂无 | 聚焦Cross-Modal Learning、Lipreading，给出可复现的模型与评测方案。 | [#123](https://github.com/zitalk/PaperClaw/issues/123) |
| [20260907] MamMA: A Mamba-Based Pedestrian Trajectory Prediction Algorithm Considering Occupancy Map and Pedestrian Awareness States | Long Juncen, Jin Xiaofeng, Bardaro Gianluca, Mentasti Simone, Matteucci Matteo | Department of Electronics, Information and Bioengineering, Politecnico di Milano, Milan, Italy | 聚焦Pedestrian Trajectory Prediction、Mamba，给出可复现的模型与评测方案。 | [#293](https://github.com/zitalk/PaperClaw/issues/293) |
| [20260907] DroneGround: Open-Vocabulary Drone Payload Characterization Using Synthetic Data and Grounded Vision-Language Models | Pandata Ami, Rajasekhar Punna, Vinod Gopika, Shukla Rohit | Homi Bhabha National Institute；Bhabha Atomic Research Centre | 聚焦Vision-Language Models、Synthetic Data，给出可复现的模型与评测方案。 | [#294](https://github.com/zitalk/PaperClaw/issues/294) |
| [20260907] Cross-modal learning for SAR target recognition using optical vision foundation models | Hirsch Lucas, James R. Hopgood, Khan Javid, Altmann Yoann, Davies Mike | School of Engineering, University of Edinburgh, United Kingdom；School of Engineering and Physical Sciences, Heriot-Watt University, United Kingdom | 聚焦Vision Foundation Models、Synthetic Aperture Radar，给出可复现的模型与评测方案。 | [#295](https://github.com/zitalk/PaperClaw/issues/295) |
| [20260907] TFTrack: A Template-Free Framework for Efficient 3D Point Cloud Tracking | Hu Zhaofeng, Zhou Sifan, Nie Jiahao, Zhao Ziyu, Li Weizi, Liang Ci-jyun | paradigm is redundant, as the previous bounding box center；Stony Brook University；Carnegie Mellon University；anzi University；Southeast University；University of California, Riverside. additional information the full template provides beyond the | 聚焦LiDAR Point Cloud、3D Single Object Tracking，给出可复现的模型与评测方案。 | [#296](https://github.com/zitalk/PaperClaw/issues/296) |
| [20260907] Zero-Shot 3D Plant Organ Segmentation with SAM3 and Semantic NeRFs | Gilson Andreas, Hennig Laura, Pietrzyk Peter | Fraunhofer Institute for Integrated Circuits (IIS), Fürth, Germany；Otto-Friedrich-Universität Bamberg, Germany；Friedrich-Alexander-Universität Erlangen-Nürnberg, Germany | 聚焦Zero-Shot Segmentation、3D Plant Phenotyping，给出可复现的模型与评测方案。 | [#297](https://github.com/zitalk/PaperClaw/issues/297) |
| [20260907] Harnessing CLIP and DINO: An Uncertainty-Aware Cascaded Fusion Network for Generalizable Deepfake Image Detection | Zou Xuechao, Zhou Yi, Li Kai, Zhang Shun, Chen Yuhui, Lang Congyan, Xing Junliang | Beijing Jiaotong University Tsinghua University Ant Group | 聚焦CLIP、Vision Foundation Models，给出可复现的模型与评测方案。 | [#298](https://github.com/zitalk/PaperClaw/issues/298) |
| [20260907] Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection | Luo Pu, Xu Cong, Li Yumei, Zhang Kexin, Jiao Licheng, Ma Wenping, Li Lingling | Xidian University, Xi'an, China | 聚焦Sim-to-Real、LiDAR 3D Object Detection，给出可复现的模型与评测方案。 | [#299](https://github.com/zitalk/PaperClaw/issues/299) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。可通过来源链接查看原文。

| 标题 | 来源 | 失败原因 |
|------|-------|----------|
| Solution for UCF UrbanTwin LUMPI Track: Sim-to-Real Urban LiDAR 3D Object Detection | [2609.07590v1](https://arxiv.org/abs/2609.07590v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| SphereSOD: Geometry-Structure Coupled Learning for 360 Salient Object Detection | [2609.07571v1](https://arxiv.org/abs/2609.07571v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| P$^2$Calib: Utilizing Pattern Priors for LiDAR-Camera Extrinsic Calibration | [2609.07516v1](https://arxiv.org/abs/2609.07516v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| PICANet: Physics-Informed Cascaded Asymmetric Network for Infrared Small Target Detection | [2609.07515v1](https://arxiv.org/abs/2609.07515v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| CrACK: Adversarial Attacks on Cross-Model Consistency in Collaborative Vision Foundation Models | [2609.07499v1](https://arxiv.org/abs/2609.07499v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| Unified Vision-Centric Pedestrian Crossing Action Prediction via Adaptive Patch Projection and Proactive Spatial Rectification | [2609.07420v1](https://arxiv.org/abs/2609.07420v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| Self-Supervised Multi-View 3D Gaze Target Estimation via Probabilistic Ray Marching | [2609.07415v1](https://arxiv.org/abs/2609.07415v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| Federated Binary Gating with Server-Side Vision-Language Inference for Surveillance Anomaly Classification | [2609.07403v1](https://arxiv.org/abs/2609.07403v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| MV-STRIDE: Enabling MLLMs to Master Multi-View Spatial Reasoning via Hierarchical Capability Modeling | [2609.07258v1](https://arxiv.org/abs/2609.07258v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| Proximity-CLIP: Text-Guided Semantic Proximity Learning for Zero-Shot Anomaly Detection | [2609.07229v1](https://arxiv.org/abs/2609.07229v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| Human-Aware Target Tracking and Navigation: Fusing Kinematic State Estimation with Structural Map Constraints | [2609.07091v1](https://arxiv.org/abs/2609.07091v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| DPSF-Net: A Dual-Prior Spatial-Frequency Network for Real-World Remote Sensing Image Dehazing | [2609.06962v1](https://arxiv.org/abs/2609.06962v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis | [2609.06948v1](https://arxiv.org/abs/2609.06948v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |
| Contextual Observer Grounding: Evaluating Situated Spatial Reasoning in Vision-Language Models | [2609.06880v1](https://arxiv.org/abs/2609.06880v1) | 质检未通过: 作者为空或无效; 摘要为空或无效 |


## 🔎 观察

- 多模态融合正从理想对齐设置转向缺失、错位和不确定模态下的鲁棒感知。
- 无人机与多视角视觉持续关注小目标、跨视角关联和复杂环境泛化。

---

Powered by OpenClaw🦞

---
