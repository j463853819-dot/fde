#!/usr/bin/env python3
"""
FDE养成学习文档更新脚本

功能：
1. 创建或更新FDE学习笔记文档
2. 按时间倒序排列内容
3. 确保格式统一完整
4. 支持每日内容自动更新
"""

import os
import sys
import json
import argparse
import re
from datetime import datetime
from pathlib import Path

class FDELearningDocumentManager:
    def __init__(self, doc_path=None):
        """
        初始化学习文档管理器

        Args:
            doc_path: 学习文档路径，默认在skill目录下
        """
        if doc_path is None:
            skill_dir = Path(__file__).resolve().parent.parent
            doc_path = skill_dir / "learning-notes.md"
        self.doc_path = Path(doc_path)
        self.today = datetime.now().strftime("%Y-%m-%d")

    def create_document_if_not_exists(self):
        """如果文档不存在则创建"""
        if not self.doc_path.exists():
            self._create_initial_document()
            print(f"已创建新的学习文档：{self.doc_path}")
        else:
            print(f"使用现有学习文档：{self.doc_path}")

    def _create_initial_document(self):
        """创建初始文档"""
        initial_content = """# FDE养成学习笔记

> 本文档自动生成并更新，记录每日FDE学习内容
> 文档按时间倒序排列，最新内容始终在最上面

---

## 学习体系概述

本学习体系基于FDE能力模型「五横三纵」框架设计，通过每日一条学习内容和动手实践，
在6个月内系统化掌握前沿部署工程师的核心知识和实践技能。

### 学习阶段规划
1. **第一阶段（第1-4周）**: LLM应用全栈筑基
2. **第二阶段（第5-10周）**: 部署与推理优化
3. **第三阶段（第11-18周）**: 客户交付实战
4. **第四阶段（第19-24周）**: 面试冲刺与作品集

### 学习原则
- **每日一条**: 避免信息过载，确保深度消化
- **由浅入深**: 系统性构建完整知识框架
- **案例驱动**: 结合真实AI企业FDE实践
- **实践导向**: 每条内容附带动手任务

---

"""
        self.doc_path.parent.mkdir(parents=True, exist_ok=True)
        self.doc_path.write_text(initial_content, encoding='utf-8')

    def add_daily_content(self, content_data):
        """
        添加每日学习内容

        Args:
            content_data: 包含学习内容的字典，格式如下：
                {
                    "date": "2026-05-27",
                    "title": "今日主题",
                    "core_concept": "核心概念内容",
                    "latest_cases": "最新案例内容",
                    "trend_insights": "趋势洞察内容",
                    "practice_task": "动手任务内容",
                    "advanced_thinking": "进阶思考内容"
                }
        """
        current_content = self.doc_path.read_text(encoding='utf-8')
        daily_content = self._build_daily_content(content_data)

        marker = "## 每日学习记录\n"
        if marker in current_content:
            new_content = current_content.replace(marker, marker + daily_content, 1)
        else:
            parts = current_content.split("---\n", 1)
            if len(parts) == 2:
                new_content = parts[0] + "---\n\n" + marker + daily_content + parts[1]
            else:
                new_content = current_content + "\n\n" + marker + daily_content

        self.doc_path.write_text(new_content, encoding='utf-8')
        print(f"已更新学习文档：{content_data['date']} - {content_data['title']}")

    def _build_daily_content(self, content_data):
        """构建每日内容格式"""
        return f"""
## {content_data['date']} - {content_data['title']}

### 核心概念
{content_data.get('core_concept', '')}

### 最新案例
{content_data.get('latest_cases', '')}

### 趋势洞察
{content_data.get('trend_insights', '')}

### 动手实践
{content_data.get('practice_task', '')}

### 进阶思考
{content_data.get('advanced_thinking', '')}

---

"""

    def get_recent_content(self, days=7):
        """获取最近N天的学习内容"""
        content = self.doc_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        recent_days = []
        current_day_content = []
        in_day_section = False

        for line in lines:
            if line.startswith('## ') and len(line) > 10:
                if in_day_section and current_day_content:
                    recent_days.append('\n'.join(current_day_content))
                    current_day_content = []

                date_str = line[3:13]
                try:
                    content_date = datetime.strptime(date_str, "%Y-%m-%d")
                    days_diff = (datetime.now() - content_date).days
                    if days_diff <= days:
                        in_day_section = True
                        current_day_content.append(line)
                except:
                    in_day_section = False
            elif in_day_section:
                current_day_content.append(line)

        if current_day_content:
            recent_days.append('\n'.join(current_day_content))

        return recent_days

    def get_document_stats(self):
        """获取文档统计信息"""
        content = self.doc_path.read_text(encoding='utf-8')
        lines = content.split('\n')

        learning_days = 0
        for line in lines:
            if re.match(r"^## \d{4}-\d{2}-\d{2} - ", line):
                learning_days += 1

        word_count = len(content.split())

        return {
            "total_days": learning_days,
            "word_count": word_count,
            "last_updated": self.today,
            "document_path": str(self.doc_path)
        }


def load_content_from_args(args):
    """从JSON文件或标准输入读取每日学习内容。"""
    if args.json_file:
        return json.loads(Path(args.json_file).read_text(encoding="utf-8"))
    if args.stdin_json:
        return json.loads(sys.stdin.read())
    return None


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="更新FDE养成学习笔记")
    parser.add_argument("--doc", help="学习笔记路径，默认写入skill目录下的learning-notes.md")
    parser.add_argument("--json-file", help="从JSON文件读取每日学习内容")
    parser.add_argument("--stdin-json", action="store_true", help="从标准输入读取JSON格式每日学习内容")
    parser.add_argument("--test", action="store_true", help="写入一条示例内容")
    args = parser.parse_args()

    print("FDE养成学习文档更新脚本")
    print("=" * 50)

    manager = FDELearningDocumentManager(args.doc)
    manager.create_document_if_not_exists()

    content_data = load_content_from_args(args)
    if content_data:
        manager.add_daily_content(content_data)

    stats = manager.get_document_stats()
    print(f"\n文档统计:")
    print(f"  学习天数: {stats['total_days']}天")
    print(f"  文档字数: {stats['word_count']}字")
    print(f"  最后更新: {stats['last_updated']}")

    # 测试模式：添加示例内容
    if args.test:
        print("\n测试模式：添加示例内容")
        test_content = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "title": "FDE的「五横三纵」能力模型入门",
            "core_concept": """FDE（前沿部署工程师）是AI领域新兴的复合型岗位，其核心使命是"让前沿AI技术精准落地到产业"。FDE能力模型被总结为"五横三纵"：

**五横（五个技能维度）**：
1. 前沿模型理解力：快速阅读论文，一周内将新论文转化为可运行原型
2. 生产级软件工程：模块化设计、TDD、CI/CD
3. 高性能推理优化：量化（INT8/FP4）、蒸馏、Triton/TensorRT
4. 云原生基础设施：K8s、GPU集群管理、自动扩缩容
5. 可观测性与运维：Prometheus、日志、告警、灰度发布

**三纵（贯穿原则）**：
1. 安全性优先：每一层部署都有安全防护
2. 合规性贯穿：AI Act、数据隐私
3. 可重复性保障：版本严格对应，全流程可复现""",
            "latest_cases": """1. **Palantir的FDE模式**：2010年代首创FDE模式，将工程师（Delta团队）派到美军和情报部门客户处常驻。到2016年，FDE数量已超普通工程师。其项目利润率可达80%，核心在于将客户需求抽象为可复用的产品能力。

2. **Google Cloud FDE**：内部招聘模式，FDE拿Google股票（强绑定），反馈闭环最通畅。高阶总包可达$40万+，被视为FDE模式的"黄金标准"。""",
            "trend_insights": """2026年FDE领域核心趋势：

1. **全球招聘暴增**：Indeed数据显示，2025年4月到2026年4月，FDE相关岗位从643个暴增至5330个，同比增长+729%。

2. **企业AI进入"落地焦虑期"**：大量AI项目停留在Demo和试验阶段，企业急需能在现场解决问题、直接交付系统的FDE人才。

3. **国内正在追赶**：360等头部公司已发布FDE岗位，薪资50-100万+，但模式上更偏向"项目交付"，与硅谷"产研前移"仍有差距。""",
            "practice_task": """今日任务：了解FDE行业全景

1. 搜索最新的FDE招聘JD（OpenAI/Anthropic/Google），对比三家公司的要求差异
2. 在LinkedIn上找3-5个FDE的从业者，分析他们的技能组合和职业路径
3. 用表格整理你自己目前的能力和FDE要求之间的差距

验收标准：完成一份FDE技能差距分析表""",
            "advanced_thinking": """1. 如果你现在开始走FDE路线，你最大的优势是什么？最大的短板是什么？
2. 在国内做FDE和在美国做FDE，职业发展路径会有哪些本质差异？
3. FDE这个岗位3年后还会存在吗？还是会演变成其他形式？"""
        }

        manager.add_daily_content(test_content)
        print("测试内容已添加")

    print("\n脚本执行完成")


if __name__ == "__main__":
    main()
