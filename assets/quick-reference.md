# FDE速查手册

## 常用工具链

### 推理引擎
| 工具 | 用途 | 适用场景 |
|------|------|----------|
| vLLM | 高吞吐推理 | 在线推理、连续批处理 |
| TensorRT-LLM | NVIDIA GPU优化 | 生产环境、最大化GPU利用率 |
| Ollama | 本地快速部署 | 开发调试、个人使用 |
| TGI (HuggingFace) | 大模型推理 | HuggingFace生态 |
| Triton Inference Server | 多模型管理 | 企业级多模型部署 |

### 量化工具
| 工具 | 支持格式 | 适用场景 |
|------|----------|----------|
| AutoGPTQ | GPTQ (INT4) | GPU量化推理 |
| AWQ | AWQ (INT4) | 高精度量化 |
| llama.cpp | GGUF (2-8bit) | CPU/混合推理 |
| bitsandbytes | NF4/INT8 | HuggingFace模型 |

### 监控与可观测性
| 工具 | 用途 |
|------|------|
| Prometheus | 指标采集 |
| Grafana | 可视化仪表板 |
| OpenTelemetry | 分布式追踪 |
| Loki | 日志聚合 |
| Alertmanager | 告警管理 |

### 部署与编排
| 工具 | 用途 |
|------|------|
| Docker | 容器化 |
| Kubernetes | 容器编排 |
| Helm | K8s包管理 |
| Istio | 服务网格 |
| Terraform | 基础设施即代码 |

---

## 常用命令速查

### Docker
```bash
# GPU容器
docker run --gpus all -it --shm-size=8g nvcr.io/nvidia/pytorch:xx.xx-py3

# 多阶段构建
docker build --target runtime -t my-app:latest .

# 容器资源限制
docker run --cpus=4 --memory=8g --gpus='"device=0"' my-app
```

### Kubernetes
```bash
# GPU节点标签
kubectl label nodes <node-name> nvidia.com/gpu.present=true

# 部署推理服务
kubectl apply -f deployment.yaml

# 查看GPU使用
kubectl exec -it <pod> -- nvidia-smi

# HPA配置
kubectl autoscale deployment inference-svc --cpu-percent=80 --min=3 --max=10
```

### vLLM
```bash
# 启动推理服务
python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-3.1-8B --tensor-parallel-size 2

# 请求测试
curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{"model":"meta-llama/Llama-3.1-8B","prompt":"Hello"}'
```

### Prometheus/Grafana
```bash
# 启动
docker-compose up -d prometheus grafana

# 查询指标
curl http://localhost:9090/api/v1/query?query=up
```

---

## 关键技术指标

### 延迟指标
- P50: 50%分位延迟（典型体验）
- P95: 95%分位延迟（大部分用户体验）
- P99: 99%分位延迟（长尾用户体验）
- **目标**: 在线推理P99 < 500ms（对话场景）

### 吞吐量指标
- QPS: 每秒查询数
- TPS: 每秒Token数（生成场景）
- 吞吐量-延迟权衡：批处理大小增加 → 吞吐量↑ 延迟↑

### 资源利用率
- GPU利用率: 理想值 70-95%（太低浪费，太高有瓶颈）
- GPU内存使用：关注显存峰值和碎片率
- KV Cache命中率: 越高越好（影响延迟和吞吐）

### 质量指标
- 错误率: 目标 < 0.1%
- 超时率: 目标 < 0.5%
- 用户满意度: NPS > 50
- 模型输出质量: 定期人工抽检或Evals自动评分

### 成本指标
- Token成本: 每百万Token的价格
- 推理成本/请求: 单次推理的GPU成本
- 成本优化基准: 降低40-60%为良好，60-80%为优秀

---

## FDE工作流速查

### 从研究代码到生产（9-16天）

```
Day 1-2:   代码审计 → 问题清单
Day 3-7:   模块化重构 → 模块化代码（含单元测试）
Day 8-10:  性能优化 → 优化代码（延迟<50ms）
Day 11-14: 基础设施集成 → 可部署系统（K8s）
Day 15-16: 灰度发布 → 生产系统（错误率<0.1%）
```

### 成本构成（典型AI推理服务）

| 项目 | 占比 |
|------|------|
| GPU计算 | 60-70% |
| 内存/存储 | 10-15% |
| 网络带宽 | 5-10% |
| 运维人力 | 10-15% |

---

## Python环境速查

```bash
# 虚拟环境创建与激活
python3 -m venv venv
source venv/bin/activate

# 常用包
pip install torch transformers accelerate bitsandbytes
pip install vllm langchain llama-index
pip install fastapi uvicorn
pip install prometheus_client opentelemetry-api
```

---

## FDE角色定位（记忆卡）

```
FDE不是：高级驻场开发、售前工程师、外包
FDE是：产品探索者、技术-业务翻译官、产研反馈桥

核心公式：
FDE价值 = 技术深度 × 业务理解 × 沟通能力
```
