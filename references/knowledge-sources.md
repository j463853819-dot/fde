# FDE学习知识源建议

本文件用于帮助 `fde-growth-plan` 在生成每日学习内容时选择合适知识源。知识源分为三类：

1. 用户已有知识库：适合做入门解释、产品判断、场景拆解和模板。
2. 官方/开源资料：适合校准技术定义、工具用法和生产实践。
3. 行业报告/案例：适合补充企业落地趋势、组织变化和商业判断。

## 1. 用户已有知识库怎么用

### AI通识知识库

适合支撑 FDE 学习的前置技术认知，尤其适合非工程背景用户。

注意：如果用户的 AI 通识知识库是按“产品经理视角”写的，要把它定位为产品化技术通识，而不是工程手册。它适合解释概念、边界、产品影响和方案判断，但不能替代代码实现、系统部署、性能调优和生产运维训练。

可迁移到 FDE 的主题：

- 大模型能力边界、Token、上下文、成本和延迟。
- Prompt 与上下文工程。
- RAG 知识库：文档处理、检索、重排、引用、评估。
- Function Calling、MCP、工具调用。
- Workflow 与 Agent 的边界。
- Agent 基础、Skill、Harness、企业 Agent。

建议用法：

- Day 1-14：作为“技术通识解释层”，避免 FDE 学习一开始过重。
- 每日内容中用于回答“这个技术解决什么业务/产品问题”。
- 给产品、运营、咨询、售前背景用户做低门槛解释。
- 在输出中明确区分“产品经理需要理解到什么程度”和“FDE需要进一步动手做到什么程度”。

不适合单独承担的部分：

- 生产级部署。
- GPU推理优化。
- K8s/GPU集群。
- 可观测性、告警、灰度、回滚。
- API工程、数据库、CI/CD和生产故障排查的动手训练。

### AI产品经理知识库

适合支撑 FDE 的客户问题拆解、产品方案、ROI表达、评估体系和作品集。

可迁移到 FDE 的主题：

- AI产品机会判断。
- AI产品设计方法论。
- AI产品架构。
- AI产品评估体系。
- AI产品从0到1。
- AI产品PRD。
- AI产品商业化与成本管理。
- Vibe Coding 原型。
- 客服销售、企业提效、SaaS AI、个人助理 Agent 等案例。
- Agent设计画布、RAG产品方案模板、AI产品上线检查表。

建议用法：

- 第1阶段：帮助用户把 AI 技术和用户场景连起来。
- 第3阶段：作为客户交付实战、ROI、MVP、方案文档的模板来源。
- 第4阶段：作为作品集、面试项目表达和案例包装来源。

不适合单独承担的部分：

- 代码工程化细节。
- 生产运维细节。
- 模型服务性能优化。

## 2. 推荐开放知识库

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
| a16z AI与服务型增长文章 | FDE、服务驱动增长、AI落地模式 | https://a16z.com/services-led-growth/ |
| Palantir Careers / FDSE | 经典FDE/FDSE角色理解 | https://www.palantir.com/careers/students-and-early-talent/ |
| FDE Academy Skill Roadmap | 通用FDE技能清单、企业软件/集成/云DevOps提醒 | https://fde.academy/blog/forward-deployed-engineer-skills |

### FDE Academy文章使用说明

FDE Academy 的 skill roadmap 适合作为补充参考，不作为唯一权威来源。它的价值在于提醒 FDE 不只是 AI 应用开发，还包括：

- Core software development：Python/Java/JavaScript、全栈、API。
- Data handling & analytics：SQL/NoSQL、ETL、BI和Dashboard。
- Cloud & DevOps：AWS/Azure/GCP、CI/CD、Docker、Kubernetes。
- Enterprise integration：CRM/ERP/SCM 等企业系统集成。
- Non-technical skills：客户沟通、项目管理、业务理解、跨团队协作。

使用时要注意：

- 这篇文章偏职业培训/路线概览，不是官方岗位JD，也不是深度工程文档。
- 它对 AI FDE 的模型、RAG、Agent、Evals、推理优化讲得较少，需要用 OpenAI/Anthropic/vLLM/NVIDIA 等资料补齐。
- 它适合放在 Day 1 摸底、能力差距表、职业路线讲解中，帮助用户看到“企业集成和运营现场”这条线。

## 3. 在每日学习里如何选择知识源

按主题选择，不要每天堆很多链接：

- 讲 FDE岗位认知：优先 OpenAI/Anthropic/Palantir/a16z。
- 讲通用能力地图：可补充 FDE Academy，但要说明它是培训机构文章，不是一手岗位定义。
- 讲 Prompt/RAG/Agent/MCP：优先用户AI通识知识库 + OpenAI/Anthropic/Microsoft。
- 讲产品方案/ROI/PRD/案例：优先用户AI产品经理知识库。
- 讲评估：优先 OpenAI Evals、LlamaIndex、Ragas、LangSmith。
- 讲部署和推理：优先 vLLM、NVIDIA、Kubernetes、Google Cloud。
- 讲企业落地趋势：优先 OpenAI企业报告、McKinsey、Google Cloud架构。

## 4. 知识库接入建议

如果用户提供本地知识库路径：

1. 先读取索引或目录，不要一次性读取全部PDF/DOCX。
2. 把知识库内容按 FDE 能力维度映射：技术通识、产品判断、客户交付、生产工程、面试作品集。
3. 每日学习只引用当天相关的1-3份资料。
4. 涉及最新岗位、工具版本、模型能力、法规和公司动态时，必须联网核验。
5. 不直接照搬内部资料原文，要转化为 FDE 学习任务、模板或检查表。
