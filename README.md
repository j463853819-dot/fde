# FDE Growth Plan Skill

## English

FDE Growth Plan is a learning skill for Forward Deployed Engineer (FDE) development. It helps users learn FDE systematically through configurable learning cycles, daily study prompts, hands-on tasks, learning notes, project practice, and interview preparation.

The skill is designed for people who want to understand or transition into roles such as:

- Forward Deployed Engineer
- Forward Deployed AI Engineer
- AI Solutions Engineer
- AI product or delivery roles with customer-facing implementation responsibility

It covers FDE role definition, career positioning, configurable learning cycles, Day 1 onboarding and capability assessment, Prompt/RAG/Agent/Workflow/MCP/Evals foundations, AI product and customer scenario analysis, demo-to-production thinking, deployment, monitoring, cost, safety, production readiness, customer requirement discovery, ROI reasoning, portfolio building, and interview preparation.

To use it, install or copy this folder into your skills directory, then ask:

```text
今天的FDE学习
```

On the first day, the skill starts with onboarding and asks for your current background, learning goal, learning cycle, daily study time, engineering and AI foundations, preferred industry scenarios, output preferences, and capability self-assessment. After onboarding, each daily study session includes a topic, explanation, case or source reference, task, acceptance criteria, and follow-up thinking prompts.

The script `scripts/update-learning-doc.py` can create or update a local `learning-notes.md` file. This file is intentionally ignored by Git because it contains personal learning history.

```bash
python3 scripts/update-learning-doc.py --json-file daily.json
```

Optional FDE knowledge base integration: this skill works without any external personal knowledge base. If you already have FDE-related notes, articles, case studies, job descriptions, learning materials, or customer deployment playbooks, you can mention the path, title, or summary during onboarding. The skill can use that material as background context for explanations, examples, practice tasks, and personalized learning plans.

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
