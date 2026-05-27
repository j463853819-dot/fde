# FDE Growth Plan Skill

FDE Growth Plan is a learning skill for Forward Deployed Engineer (FDE) development. It helps users learn FDE systematically through configurable learning cycles, daily study prompts, hands-on tasks, knowledge notes, project practice, and interview preparation.

The skill is designed for people who want to understand or transition into roles such as:

- Forward Deployed Engineer
- Forward Deployed AI Engineer
- AI Solutions Engineer
- AI product or delivery roles with customer-facing implementation responsibility

## What It Covers

- FDE role definition and career positioning
- Configurable learning cycles: 4, 8, 12, or 24 weeks
- Day 1 onboarding and capability assessment
- Prompt, RAG, Agent, Workflow, MCP, and Evals foundations
- AI product and customer scenario analysis
- Demo-to-production thinking
- Deployment, monitoring, cost, safety, and production readiness
- Customer requirement discovery and ROI reasoning
- Portfolio and interview preparation

## Directory Structure

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

## Usage

Install or copy this folder into your skills directory, then ask:

```text
今天的FDE学习
```

On the first day, the skill starts with onboarding and asks for:

- Current background
- Learning goal
- Learning cycle
- Daily study time
- Engineering and AI foundations
- Preferred industry scenarios
- Output preferences
- Capability self-assessment

After onboarding, each daily study session includes a topic, explanation, case or source reference, task, acceptance criteria, and follow-up thinking prompts.

## Learning Notes

The script `scripts/update-learning-doc.py` can create or update a local `learning-notes.md` file. This file is intentionally ignored by Git because it contains personal learning history.

Example:

```bash
python3 scripts/update-learning-doc.py --json-file daily.json
```

## Notes

This skill treats product-manager-oriented AI knowledge as useful conceptual grounding, but not as a substitute for hands-on engineering, deployment, observability, and production troubleshooting practice.

## License

MIT

