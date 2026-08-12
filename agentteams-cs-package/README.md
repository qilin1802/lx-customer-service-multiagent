# AgentTeams 客服闭环 · 可执行部署包

GOAI 智能客服自主闭环赛道 · 复赛代码包。基于 AgentTeams（HiClaw）v1.2.2 的可复现客服多 Agent 系统。

## 结构

```
agentteams-cs-package/
├── README.md              # 本文件：部署说明
├── deploy/                # 部署配置（env 文件，含密钥需自行替换）
│   ├── agentteams-controller.env
│   └── agentteams-manager.env
├── manager/               # Manager Agent 配置快照
│   ├── SOUL.md            # Manager 身份定义
│   ├── AGENTS.md          # Manager 操作规范
│   ├── HEARTBEAT.md       # Manager 巡检清单
│   ├── TOOLS.md           # 技能速查
│   └── state.json         # 状态台账（示例）
├── workers/               # Worker Identity 清单（6 个 Agent 的 SOUL.md）
│   ├── cs-gather-SOUL.md
│   ├── cs-intent-SOUL.md
│   ├── cs-handler-SOUL.md
│   ├── cs-approver-SOUL.md
│   ├── cs-verify-SOUL.md
│   └── cs-review-SOUL.md
└── skills/                # 核心 Skill 清单（9 要素设计，可发布至 AgentTeams 市场）
    ├── ticket-aggregation/       # S01 工单聚合去重
    ├── intent-classification/    # S02 意图识别分级
    ├── solution-generation/      # S03 处理方案生成
    ├── operation-execution/      # S04 业务操作执行（幂等）
    ├── result-verification/      # S05 结果核验确认
    └── knowledge-distillation/   # S06 案例复盘沉淀
```

## Agent Identity 清单

| Agent | 职能 | 能力边界 | 协同关系 |
|---|---|---|---|
| cs-gather | 会话聚合 | 多渠道接入、同人归一化、去重合并 | 产出标准工单 → cs-intent |
| cs-intent | 意图识别 | 分类、槽位抽取、紧急度分级 | 承接 cs-gather → cs-handler |
| cs-handler | 方案执行（团队长） | 方案生成、业务执行、流程协调 | 协调 cs-approver/cs-verify |
| cs-approver | 审批把关 | 高风险审批、回滚、审计 | 服务 cs-handler 的审批请求 |
| cs-verify | 结果核验 | 结果确认、满意度解析、升级处理 | 承接 cs-handler → cs-review |
| cs-review | 案例复盘 | 复盘报告、FAQ 提炼、知识回写 | 承接 cs-verify → 知识反哺 |

## 部署步骤（Windows + Docker Desktop）

```powershell
# 1. 前置：Docker Desktop + WSL2
# 2. 安装 AgentTeams（官方脚本）
Set-ExecutionPolicy Bypass -Scope Process -Force; $wc=New-Object Net.WebClient; $wc.Encoding=[Text.Encoding]::UTF8; iex $wc.DownloadString('https://raw.githubusercontent.com/agentscope-ai/AgentTeams/main/install/agentteams-install.ps1')

# 3. 用 deploy/ 下的 env 配置替换生成的文件
#    - agentteams-controller.env → C:\Users\<user>\agentteams-controller.env
#    - agentteams-manager.env    → C:\Users\<user>\agentteams-manager.env
#    注意：LLM API Key 与 Token 需替换为自己的

# 4. 重建控制器容器（env 修改后生效）
docker rm -f agentteams-controller
docker run -d --name agentteams-controller --network agentteams-net ...（见文档）

# 5. 访问 Element：http://127.0.0.1:18088
```

## Skill 安装

```powershell
# 将 skills/ 下目录复制到 Manager 工作区（分发所有 Worker）
Copy-Item skills\* C:\Users\<user>\agentteams-manager\worker-skills\ -Recurse

# 或逐个给 Worker 配置（Element 中对话式安装）
```

## 端到端测试

1. Element 登录（admin）
2. 发送测试工单，例如：
   > 你好，我上周买的手机壳碎了，订单号 20260801001，金额 59 元，想退货退款
3. 观察 cs-gather → cs-intent → cs-handler → cs-verify 接力流转
4. 大额退款（>100 元）会触发 cs-approver 审批节点

## 依赖

- AgentTeams (HiClaw) ≥ v1.2.2
- Python ≥ 3.10（Skill 脚本）
- LLM：DeepSeek / 通义千问（OpenAI 兼容接口）
