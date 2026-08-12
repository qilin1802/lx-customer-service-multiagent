<!-- ppt-master-schema: design-spec/v1 -->
# 灵犀客服 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 灵犀客服 · 多 Agent 智能客服自主闭环系统 |
| Canvas Format | ppt169 (1280×720) |
| Page Count | 12 |
| Primary Language | zh-CN |
| Target Audience | 比赛评委（AI 架构方向专家）与同行参赛者，熟悉 AI/Agent 概念，关注工程落地 |
| Communication Intent | 先讲清场景价值建立共鸣 → 展示方案设计证明技术能力 → 用可落地性与验证结果说服评委 |
| Desired Audience Outcome | 评委记住三点：多 Agent 闭环已真实跑通；全透明可干预安全可控；知识反哺是独特创新 |
| Core Message / Ask / Action | 基于 AgentTeams 的 6 智能体客服闭环，从多渠道工单到知识沉淀全自动，已跑通端到端验证 |
| Delivery Context | 主讲人现场演讲（比赛答辩），约 15 分钟，辅以在线 Demo 展示 |
| Artifact Afterlife | 评审留档、复赛迭代基础、开源发布素材 |
| Reading Mode | balanced |
| Content Strategy | balanced —— 保留用户提供的四大部分结构和全部内容，重组为演讲叙事节奏，不增删事实 |
| Design Style | 方向 A · 科技蓝图（blueprint 基座 + briefing 模式） |
| Formula Policy | text-only |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | disabled — explicit user instruction |
| Custom Animations | disabled — workflow default |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-08-12 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | ppt169 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64px 四边安全边距 |
| Content Area | 1152 × 592（安全区） |

## III. Visual Theme

### Theme Style

- **Mode**: custom（briefing 基座：结论先行、分块论证、信息密度均衡）
- **Mode References**: briefing
- **Mode Behavior**: 结论先行式论证——每部分先亮出核心主张（"闭环已跑通""全透明可干预""知识反哺"），再分块展开支撑论据；标题采用断言式（"客服在人海，经验在人脑"），页面节奏均匀，无情感化包装，以事实和结构说服评委。
- **Visual style**: custom（blueprint 基座：技术图纸感、网格、直角、mono 标注）
- **Visual Style References**: blueprint
- **Visual Style Behavior**: 技术蓝图美学——浅米白底 + 深蓝主色，发丝线网格与直角色块构成版式骨架，mono 字体做章节标注（"SCENARIO · 01"），架构流程使用几何连线与框体（线条描边，非填充卡通），整体克制、精确、可投影；无渐变、无圆角、无阴影。
- **Theme**: 科技蓝图 · 工程图纸
- **Tone**: 专业、克制、技术自信

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #F7F8FA | 主背景（浅冷白，图纸感） |
| Secondary background | #EDEFF3 | 卡片/区块底 |
| Primary | #002FA7 | 克莱因蓝主色（标题强调、主结构线） |
| Accent | #0057FF | 亮蓝（数据高亮、关键节点） |
| Secondary accent | #B8C4D6 | 辅助蓝灰（次要标注线） |
| Body text | #1A1D24 | 正文 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | 黑体/粗壮 | 微软雅黑 | Inter | sans-serif |
| Body | 黑体/常规 | 微软雅黑 | Inter | sans-serif |

- **Title stack**: "微软雅黑", "PingFang SC", "Noto Sans SC", Inter, sans-serif
- **Body stack**: "微软雅黑", "PingFang SC", "Noto Sans SC", Inter, sans-serif
- **Data stack**: "JetBrains Mono", "Consolas", monospace
- **Role rationale**: Data —— 页面中的 Agent 名称、编号、版本等标注使用等宽字体，强化工程图纸感。

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 22 |
| Title | 44 |
| Subtitle | 30 |
| Annotation | 18 |

## V. Layout Principles

### Page Structure

- **Header area**: 顶部 chrome 行——左侧章节标签（mono 小字），右侧页码（如 03 / 12），底部一条发丝线
- **Content area**: 居中主区，标题区 + 内容网格（16 列网格），各页按内容选用卡片/流程/对比/清单结构
- **Footer area**: 底部保留安全边距，不放置内容，避免与页脚重叠

### Spacing Specification

| Element | Current Project |
| --- | --- |
| Safe margin | 64px |
| Content block gap | 32px |
| Icon-text gap | 12px |

## VI. Icon Usage Specification

- **Primary bundled library**: tabler-outline
- **Stroke Width**: 2

| Icon Path | Suitable Scenarios |
| --- | --- |
| tabler-outline/users | 目标用户、Agent 角色 |
| tabler-outline/mail | 邮件渠道 |
| tabler-outline/message-circle | 在线客服渠道 |
| tabler-outline/phone | 电话转写渠道 |
| tabler-outline/message | 社媒评论渠道 |
| tabler-outline/brand-x | 社媒渠道 |
| tabler-outline/layers | 架构分层 |
| tabler-outline/git-branch | 流程分支、异常分支 |
| tabler-outline/check | 结果验证 |
| tabler-outline/shield-check | 安全边界 |
| tabler-outline/eye | 可观测性 |
| tabler-outline/database | 知识库 |
| tabler-outline/tool | 工具/Skill |
| tabler-outline/api | MCP 接入 |
| tabler-outline/refresh | 知识反哺闭环 |
| tabler-outline/calendar | 落地计划 |

## VII. Visualization Reference List

| Page | Family | Template | Usage |
| --- | --- | --- | --- |

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## IX. Content Outline

### Part 1: 场景与价值

#### Slide 01 - 封面

- **Audience move**: 未知项目 → 建立项目认知
- **Layout**: 全屏深蓝底，标题居中偏左，章节标签顶部，底部副标题与团队信息；标题字大、强调"自主闭环"
- **Title**: 灵犀客服 · 多 Agent 智能客服自主闭环系统
- **Core message**: 这是一个已跑通端到端的多 Agent 客服闭环系统
- **Content**: 主标题"灵犀客服 · 多 Agent 自主闭环系统"；副标题"从多渠道工单聚合到知识沉淀反哺 —— 基于 AgentTeams 的 6 智能体客服闭环，已跑通端到端测试工单"；章节标签"GOAI 智能客服自主闭环赛道"；底部"AI 架构大赛 · 方案答辩"

#### Slide 02 - 场景与痛点

- **Audience move**: 无感 → 共情痛点
- **Layout**: 左侧大标题断言，右侧痛点清单卡片（3-4 项），底部渠道标签
- **Title**: 客服在人海，经验在人脑
- **Core message**: 传统客服的四大痛点：多渠道分散、人工分类、链路不可追溯、知识流失
- **Content**: 大标题"客服在人海，经验在人脑"；痛点卡片：①多渠道工单分散，人工归类耗时 ②意图分类依赖经验，新人上手慢 ③退款换货执行链路长，状态不可追溯 ④复盘知识无处沉淀，离职即失忆；底部标签"邮件 · 在线客服 · 电话转写 · 社媒评论"

#### Slide 03 - 目标用户与业务价值

- **Audience move**: 共情 → 理解价值
- **Layout**: 顶部标题，中间三列价值卡（降本/提速/提质），底部目标用户行
- **Title**: 服务谁，带来什么
- **Core message**: 面向电商/SaaS 客服部门，带来降本、提速、提质三大价值
- **Content**: 目标用户：中小电商客服部、SaaS 平台客服运营团队；价值三卡：降本——减少 70% 重复性人力；提速——工单闭环分钟级；提质——经验沉淀反哺，越用越聪明

#### Slide 04 - 输入输出与行业可复制性

- **Audience move**: 理解价值 → 看见边界与前景
- **Layout**: 顶部标题，中间"输入 → 系统 → 输出"横向流程（SVG 绘制），底部可复制性说明
- **Title**: 输入输出与可复制性
- **Core message**: 输入多渠道消息，输出已处理工单+满意度确认+沉淀知识；模式可迁移多行业
- **Content**: 输入：多渠道消息（邮件/在线客服/电话转写/社媒评论）；系统：6 Agent 闭环；输出：已处理工单 + 满意度确认 + 沉淀知识；可复制性：一个引擎，多行业（电商客服/运维工单/法律咨询/金融审核）

### Part 2: 方案设计

#### Slide 05 - 系统架构

- **Audience move**: 看见价值 → 理解技术路线
- **Layout**: 顶部标题，中间四层横向架构图（SVG：接入层→编排层→执行层→沉淀层），每层右侧标注对应组件
- **Title**: 四层架构 · 全链路闭环
- **Core message**: 以 AgentTeams 为编排基点的四层架构
- **Content**: 接入层：多渠道统一消息模型（cs-gather）；编排层：AgentTeams Manager-Worker + Matrix 房间（任务拆解/上下文传递/状态追踪）；执行层：Skill 抽象能力 + MCP 接业务系统 + RAG 支撑决策；沉淀层：知识库回写 + 反馈回路；标注"AgentTeams 为设计基点"

#### Slide 06 - Agent 分工

- **Audience move**: 理解架构 → 认识团队
- **Layout**: 顶部标题，六宫格卡片（3×2），每卡 Agent 名称 + 职责一行 + 角色标签；cs-handler 卡片高亮
- **Title**: 6 个智能体，各司其职
- **Core message**: 6 个 Worker 身份清晰、边界明确，cs-handler 为团队长
- **Content**: cs-gather 会话聚合（同人归一化/去重）；cs-intent 意图识别（槽位/紧急度）；cs-handler 方案执行（团队长/协调）；cs-approver 审批把关（回滚/审计）；cs-verify 结果核验（满意度确认）；cs-review 案例复盘（FAQ/知识回写）

#### Slide 07 - 协作流程与上下文传递

- **Audience move**: 认识团队 → 看懂协作
- **Layout**: 顶部标题，中间五步横向流程（SVG：聚合→识别→执行→核验→复盘），箭头标注；下方 Matrix 房间示意条
- **Title**: 一条工单，走完闭环
- **Core message**: 工单经五步闭环流转，上下文通过 Matrix 房间全程传递
- **Content**: 五步：聚合工单（cs-gather）→ 意图分级（cs-intent）→ 方案执行（cs-handler，高风险经 cs-approver）→ 核验确认（cs-verify）→ 复盘沉淀（cs-review）；上下文传递：Matrix 房间消息流承载工单/中间结论/工具结果；状态追踪：state.json + MinIO 共享

#### Slide 08 - 结果验证与异常分支

- **Audience move**: 看懂协作 → 信服可靠性
- **Layout**: 顶部标题，上部正常核验路径（SVG 简图），下部异常分支清单（4 条，箭头图标）
- **Title**: 结果核验与异常兜底
- **Core message**: 每单必核验，异常必有兜底，高风险必审批
- **Content**: 正常路径：核验 Worker 查系统确认退款到账 → 满意度确认 → 完结；异常分支：①意图置信度低 → 转人工复核 ②执行失败 → 重试 1 次 → 转人工 ③客户未回应/不满 → 升级转人工 ④大额退款 → cs-approver 人工审批；全程审计日志可回放

### Part 3: Skill 与工具集成

#### Slide 09 - 核心 Skill 设计

- **Audience move**: 信服可靠性 → 认可工程化
- **Layout**: 顶部标题，左列 Skill 名称清单（6 项），右侧两项展开（用途/输入输出/复用价值精简），底部复用价值声明
- **Title**: Skill 即能力抽象层
- **Core message**: 6 个核心 Skill 覆盖闭环全环节，9 要素设计，可复用可发布
- **Content**: Skill 清单：ticket-aggregation（聚合）、intent-classification（意图）、solution-generation（方案）、business-operation-execution（执行）、result-verification（核验）、knowledge-distillation（沉淀）；每个 Skill 含名称/用途/输入输出/调用条件/依赖工具/失败处理/安全边界/复用价值/协同关系 9 要素；复用价值：发布至 AgentTeams 市场，其他企业可导入

#### Slide 10 - MCP / RAG / 可观测

- **Audience move**: 认可工程化 → 看见完整规划
- **Layout**: 顶部标题，三列规划卡（MCP 接入/上下文增强/可观测体系），每卡现状+规划两行
- **Title**: 工具连接与能力规划
- **Core message**: MCP 接工具、RAG 提质量、可观测保信任
- **Content**: MCP：业务系统（订单/退款/账户 API）封装为 MCP Server，经 Higress 网关统一接入，含鉴权/Schema/幂等/审计/降级契约；RAG 与上下文：知识库 RAG 支撑方案生成（4 选 2 已全覆盖：知识库 RAG+共享状态+Agent 记忆+轨迹可观测）；可观测：Matrix 房间全透明（Log/轨迹）已实现，规划 AgentLoop 推理轨迹

### Part 4: 可行性与落地计划

#### Slide 11 - 落地计划与评估指标

- **Audience move**: 看见规划 → 相信能交付
- **Layout**: 顶部标题，三阶段横排（初赛已完成/复赛/决赛），底部评估指标清单
- **Title**: 三阶段落地，指标可量化
- **Core message**: 已完成初赛验证，复赛工程落地，决赛量化评估
- **Content**: 阶段一（已完成）：AgentTeams 部署、6 Worker 创建、测试工单全链路跑通；阶段二（复赛 8.16-9.3）：Mock 业务系统 MCP 化、知识库 RAG、可观测接入、指标跑分；阶段三（决赛 9.22）：自动化率/闭环率/意图准确率/满意度量化，Skill 市场发布；评估指标：自动化率、闭环完成率、意图识别准确率、转人工率、平均处理时长

#### Slide 12 - 收尾

- **Audience move**: 相信能交付 → 记住项目
- **Layout**: 左右分屏：左侧深蓝底宣言（"客服自主闭环，从一条工单开始"），右侧三条 takeaway
- **Title**: 闭环已跑通，知识持续反哺
- **Core message**: 三条 takeaway：多 Agent 闭环已跑通；全透明可干预可审计；知识沉淀反哺闭环
- **Content**: 左侧宣言：客服自主闭环，从一条工单开始；右侧：①多 Agent 闭环已跑通（测试工单端到端验证，可运行 Demo）②全透明可干预（Matrix 全程可见，人工审批回滚）③知识沉淀反哺（复盘→FAQ→RAG，越用越聪明）

## X. Speaker Notes Requirements

- **Generation**: disabled
