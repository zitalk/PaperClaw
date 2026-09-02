# Daily Reports

最近三天日报（最新在前）：

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
