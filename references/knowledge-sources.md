# FDE学习知识源建议

本文件用于帮助 `fde-growth-plan` 在生成每日学习内容时选择合适知识源。默认假设用户没有个人知识库，优先使用公开资料。只有当用户主动提供 FDE 相关知识库、文章、案例、岗位JD、学习资料或客户部署方法论时，才接入用户自己的资料作为增强。

## 1. 默认知识源原则

默认学习内容应来自三类公开资料：

1. 官方岗位和公司资料：用于校准 FDE/FDSE 的角色定义、职责和招聘要求。
2. 官方/开源工程资料：用于校准 Prompt、RAG、Agent、Evals、部署、推理和生产实践。
3. 行业报告与案例：用于补充企业 AI 落地趋势、服务型增长和组织变化。

不要假设用户已有 AI 通识、AI 产品经理或行业知识库。普通用户只要安装 skill，就应该能直接开始学习。

## 2. 可选 FDE 知识库接入

如果用户提供 FDE 相关知识库路径、资料标题或摘要，可以把它作为个性化增强。适合接入的资料包括：

- FDE/FDSE 相关文章和学习笔记。
- Forward Deployed Engineer、Forward Deployed AI Engineer、AI Solutions Engineer 等岗位 JD。
- 企业 AI 项目交付案例。
- 客户部署、解决方案、售前交付或实施复盘。
- RAG/Agent 项目上线、评估、监控、权限、安全、灰度发布相关资料。
- 个人作品集、面试准备或项目复盘资料。

接入方式：

1. 先读取索引、目录或摘要，不要一次性读取全部 PDF/DOCX。
2. 判断资料对应 FDE 的哪个维度：岗位认知、技术实现、客户交付、生产工程、产品反馈、作品集/面试。
3. 每日学习只引用当天相关的 1-3 份资料。
4. 涉及最新岗位、公司动态、工具版本、模型能力、法规和市场数据时，仍然必须联网核验。
5. 不直接照搬用户资料原文，要转化为 FDE 学习任务、模板、检查表或案例分析。

如果用户提供的是非 FDE 资料，例如 AI 通识、AI 产品经理、行业研究或工程笔记，也可以作为补充背景，但不要把它描述为默认前提。使用时需要说明它只是辅助理解，不替代 FDE 专项资料和动手训练。

## 3. 推荐公开知识源

### FDE岗位与角色认知

| 知识源 | 用途 | 链接 |
|---|---|---|
| OpenAI Forward Deployed Engineer JD | AI FDE职责、客户部署、生产系统、eval反馈 | https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/ |
| Anthropic Forward Deployed Engineer JD | Claude企业部署、客户系统嵌入、生产应用 | https://www.anthropic.com/careers/jobs/4985877008 |
| Palantir FDSE / Early Talent | 经典FDSE角色、客户开放问题、运营结果 | https://www.palantir.com/careers/students-and-early-talent/ |
| a16z Services-Led Growth | AI时代服务型增长、部署和客户现场价值 | https://a16z.com/services-led-growth/ |
| FDE Academy Skill Roadmap | 通用FDE技能清单、企业软件/集成/云DevOps提醒 | https://fde.academy/blog/forward-deployed-engineer-skills |

FDE Academy 可作为补充参考，不作为唯一权威来源。它的价值在于提醒 FDE 不只是 AI 应用开发，还包括 API、数据库、BI、CRM/ERP/SCM 集成、云和 DevOps。但它偏职业培训/路线概览，不是官方岗位 JD，也不是深度工程文档。

### AI应用与Agent基础

| 知识源 | 用途 | 链接 |
|---|---|---|
| OpenAI Cookbook | 示例代码、Evals、RAG、Agent实践 | https://github.com/openai/openai-cookbook |
| OpenAI Platform Docs | 官方API、工具调用、文件检索、评估 | https://platform.openai.com/docs |
| Anthropic Prompt Engineering Docs | Prompt、上下文、Claude使用方法 | https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview |
| Anthropic Building Effective Agents | Workflow vs Agent、生产可控性 | https://www.anthropic.com/engineering/building-effective-agents |
| Anthropic MCP Docs | MCP定义、连接外部工具和数据 | https://docs.anthropic.com/en/docs/mcp |
| Microsoft Generative AI for Beginners | 适合初学者的生成式AI课程 | https://github.com/microsoft/generative-ai-for-beginners |
| Microsoft AI Agents for Beginners | Agent基础课程和练习 | https://github.com/microsoft/ai-agents-for-beginners |

### RAG与评估

| 知识源 | 用途 | 链接 |
|---|---|---|
| OpenAI Evaluation Best Practices | AI应用评估方法 | https://platform.openai.com/docs/guides/evaluation-best-practices |
| LlamaIndex Evaluation Docs | RAG评估、检索评估 | https://docs.llamaindex.ai/en/stable/module_guides/evaluating/ |
| Ragas Metrics | RAG质量指标 | https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/ |
| LangSmith Evaluation | 离线/在线评估和实验管理 | https://docs.langchain.com/langsmith/evaluation |
| NVIDIA RAG Evaluation | 生产级RAG评估参考 | https://docs.nvidia.com/rag/latest/evaluate.html |
| Google Vertex AI RAG Docs | 托管式RAG与企业架构参考 | https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-quickstart |

### 部署、推理与生产工程

| 知识源 | 用途 | 链接 |
|---|---|---|
| vLLM Docs | 高吞吐LLM推理服务、OpenAI兼容API | https://docs.vllm.ai/en/stable/ |
| vLLM Blog | 推理系统架构、吞吐、分布式服务 | https://blog.vllm.ai/ |
| NVIDIA TensorRT-LLM Docs | NVIDIA GPU上的LLM推理优化 | https://docs.nvidia.com/tensorrt-llm/ |
| NVIDIA TensorRT Developer | 低延迟、高吞吐生产推理 | https://developer.nvidia.com/tensorrt |
| Kubernetes GPU Scheduling | GPU节点调度基础 | https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/ |
| Google Cloud RAG Reference Architecture | 企业RAG基础设施架构 | https://docs.cloud.google.com/architecture/rag-genai-agentspace-vertexai |

### 企业AI趋势与商业判断

| 知识源 | 用途 | 链接 |
|---|---|---|
| OpenAI State of Enterprise AI | 企业AI采用趋势 | https://openai.com/index/the-state-of-enterprise-ai-2025-report/ |
| McKinsey State of AI | 企业AI落地、组织和价值趋势 | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai |

## 4. 每日学习如何选择知识源

按主题选择，不要每天堆很多链接：

- 讲 FDE 岗位认知：优先 OpenAI、Anthropic、Palantir、a16z。
- 讲通用能力地图：可补充 FDE Academy，但要说明它是培训机构文章，不是一手岗位定义。
- 讲 Prompt/RAG/Agent/MCP：优先 OpenAI、Anthropic、Microsoft。
- 讲评估：优先 OpenAI Evals、LlamaIndex、Ragas、LangSmith。
- 讲部署和推理：优先 vLLM、NVIDIA、Kubernetes、Google Cloud。
- 讲企业落地趋势：优先 OpenAI 企业报告、McKinsey。
- 用户提供 FDE 相关知识库时：优先作为个性化案例或背景，仍用公开资料校准事实。

