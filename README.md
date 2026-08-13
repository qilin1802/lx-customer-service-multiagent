# 灵犀客服 · 多 Agent 智能客服自主闭环系统

GOAI 智能客服自主闭环赛道参赛作品。基于 AgentTeams（HiClaw）多 Agent 协同框架，构建 6 智能体客服闭环，实现「多渠道工单接入 → 意图识别分级 → 方案生成执行（含人工审批）→ 结果核验 → 案例复盘 → 知识反哺」的端到端自动化。

## 目录结构

```
├── README.md                    # 本文件
├── 作品简介.md                  # 初赛 500 字作品简介
├── 灵犀客服.pptx                # 初赛方案 PPT（19 页暖色版，主交付物）
│
├── agentteams-cs-package/       # 可执行部署代码包
│   ├── deploy/                  # 控制器/Manager env 配置
│   ├── manager/                 # Manager 身份/规范/状态快照
│   ├── workers/                 # 6 个 Worker 的 SOUL.md（Agent Identity 清单）
│   └── skills/                  # 6 个核心 Skill（SKILL.md + 脚本）
│
└── 灵犀客服-比赛PPT/            # 初赛 PPT 生成工程（ppt-master：SVG 源 + 导出）
```

## 多 Agent 系统

6 个职能 Worker + 团队 `cs-team`（Manager-Worker 双层架构，Matrix 房间协同）：

| Agent | 角色 | 职能 |
|---|---|---|
| cs-gather | worker | 多渠道消息聚合、去重归一化 |
| cs-intent | worker | 意图识别、槽位抽取、紧急度分级 |
| cs-handler | team_leader | 方案生成、业务执行、流程协调 |
| cs-approver | worker | 高风险动作（>100 元退款）审批与回滚 |
| cs-verify | worker | 结果核验、满意度确认 |
| cs-review | worker | 案例复盘、FAQ 提炼、知识回写 |

**协同机制**：上下文经 Matrix 房间传递；状态登记在 `state.json` + MinIO 共享；每单沉淀 9 份证据文件（gather/intent/spec/execution/approval/verification/confirmation/review/result）。

## Skill 工程体系

6 个核心 Skill，每个含 9 要素规格（名称/用途/输入输出/调用条件/依赖工具/失败处理/安全边界/复用价值/协同关系）：

| Skill | 职能 | 脚本策略 |
|---|---|---|
| ticket-aggregation | 工单聚合去重 | 三级去重（精确/相似/语义）+ bigram 相似度 |
| intent-classification | 意图识别分级 | 规则优先 + 三级路由（rule/llm/human）|
| solution-generation | 方案生成 | 金额阈值 + 审批等级判定 |
| operation-execution | 业务操作执行 | 幂等键 + 重试 + 回滚 |
| result-verification | 结果核验 | 执行结果比对 + 满意度解析 |
| knowledge-distillation | 复盘沉淀 | 复盘报告 + FAQ 提炼 + 知识回写 |

## 运行验证（实测数据）

- **单笔 A/B 对照**：59 元 LOW 自动放行 vs 199 元 HIGH 人工审批，阈值边界（100 元）验证通过。
- **批量压测**：10 单串行退款，10/10 完成（5 LOW 自动 + 5 HIGH 逐单审批），每单约 5 分钟。
- **合规复盘**：发现并修正「虚构 Manager 批量预授权」越权问题，沉淀强约束规则 `KB-RULE-APPROVAL-AUTH-INTEGRITY` 至知识库。

## 可观测性

接入阿里云云监控 CMS 2.0「AI Agent 可观测」（service.name=`agentteams-manager`），产出真实链路数据：单次会话 10 次 LLM 调用、TTFT 2.02s、TPOT 0.006s/token。

## 技术底座

AgentTeams（HiClaw）+ Matrix 房间（全透明）+ DeepSeek LLM + Skill + MinIO + 阿里云云监控。

> 注：MCP（业务系统接入）与 RAG（知识库检索）为**阶段二规划**，当前业务操作为 Mock API，方案生成为规则脚本。

## 落地路线图

- **阶段一（已完成）**：环境部署、6 Worker 组队、端到端跑通、10 单压测、可观测接入。
- **阶段二（复赛）**：Mock 业务系统 MCP 化、知识库 RAG。
- **阶段三（决赛）**：自动化率/闭环率/意图准确率量化、Skill 市场发布。

## 本地运行

Windows + WSL2 + Docker Desktop + AgentTeams v1.2.2，部署步骤见 `agentteams-cs-package/README.md`。

## 许可

本项目为参赛作品，方案设计文档与演示材料开放共享。
