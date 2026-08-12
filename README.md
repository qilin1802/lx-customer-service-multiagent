# 灵犀客服 · 多 Agent 智能客服自主闭环系统

GOAI 智能客服自主闭环赛道参赛作品。基于 AgentTeams（HiClaw）多 Agent 协同框架，构建 6 智能体客服闭环：从多渠道工单聚合到知识沉淀反哺，全流程自动化、可观测、可人工干预。

## 目录结构

```
├── 作品简介.md                  # 初赛 500 字作品简介
├── 灵犀客服.pptx                # 最终版方案 PPT（可编辑）
├── 参赛手册.pdf                 # 大赛参赛手册
├── 重要信息.txt                 # 项目笔记（Skill 清单 / Agent Identity）
└── 灵犀客服-比赛PPT/
    ├── ppt/index.html           # 网页版方案 PPT（瑞士风，单文件可演示）
    └── lx-customer-service_ppt169_20260812/   # ppt-master 工程
        ├── design_spec.md       # 设计方案（12 页规划）
        ├── spec_lock.md         # 设计锁（执行锚点）
        ├── svg_output/          # 12 页 SVG 源文件（页面设计权威源）
        ├── svg_final/           # 自包含 SVG 预览
        ├── exports/             # 导出的 PPTX
        ├── icons/               # tabler-outline 图标池
        └── validation/          # 质量检查与导出报告
```

## 核心内容

- **6 Agent 分工**：cs-gather（聚合）/ cs-intent（意图）/ cs-handler（执行，团队长）/ cs-approver（审批）/ cs-verify（核验）/ cs-review（复盘）
- **端到端闭环**：多渠道输入 → 意图分级 → 方案执行（含审批回滚）→ 核验确认 → 复盘沉淀 → 知识反哺
- **技术底座**：AgentTeams + Matrix 房间（全透明）+ DeepSeek LLM + Skill/MCP/RAG

## 运行验证

- 测试工单全链路已跑通（Element 界面可视化验证）
- 本地环境：Windows + WSL2 + Docker Desktop + AgentTeams v1.2.2

## 许可

本项目为参赛作品，方案设计文档与演示材料开放共享。
