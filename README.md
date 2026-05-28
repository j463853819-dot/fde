# FDE Growth Plan Skill

## 中文

FDE Growth Plan 是一个面向 FDE（Forward Deployed Engineer，前沿部署工程师）成长的学习 skill。它通过可配置学习周期、每日学习推送、动手任务、学习笔记、项目练习和面试准备，帮助用户系统学习 FDE 所需的复合能力。

这个 skill 适合想了解或转向以下岗位的人：

- 前沿部署工程师
- Forward Deployed AI Engineer
- AI Solutions Engineer
- 面向客户交付和落地的 AI 产品、解决方案或交付岗位

它覆盖 FDE 岗位定义、职业定位、4/8/12/24 周可配置学习周期、Day 1 摸底和能力评估、Prompt/RAG/Agent/Workflow/MCP/Evals 基础、AI 产品与客户场景分析、Demo 到 Production 的生产化思维、部署、监控、成本、安全、生产就绪、客户需求发现、ROI 判断、作品集和面试准备。

使用方式：把这个文件夹安装或复制到你的 skills 目录，然后对助手说：

```text
今天的FDE学习
```

第一天会先进行摸底，了解你的当前背景、学习目标、学习周期、每天学习时长、工程和 AI 基础、偏好的行业场景、输出偏好，以及能力自评。完成摸底后，每天的学习内容会包含主题、概念讲解、案例或资料来源、动手任务、验收标准和进阶思考。

`scripts/update-learning-doc.py` 可以创建或更新本地 `learning-notes.md` 学习笔记。这个文件会被 Git 忽略，因为它包含个人学习记录。

```bash
python3 scripts/update-learning-doc.py --json-file daily.json
```

可选 FDE 知识库接入：这个 skill 不要求用户提前拥有任何个人知识库。如果你已经有 FDE 相关的笔记、文章、案例、岗位 JD、学习资料或客户部署方法论，可以在 Day 1 摸底时告诉助手知识库的路径、标题或摘要。后续每日学习可以把这些资料作为解释、案例、练习任务和个性化学习路线的背景。

## Directory Structure / 目录结构

```text
fde-growth-plan/
├── SKILL.md
├── assets/
│   ├── learning-template.md
│   └── quick-reference.md
├── references/
│   ├── case-library.md
│   ├── fde-frameworks.md
│   ├── knowledge-sources.md
│   ├── learning-cycles.md
│   ├── learning-topics.md
│   └── user-configuration.md
└── scripts/
    ├── mock-deployment.sh
    └── update-learning-doc.py
```

## License / 许可证

MIT
