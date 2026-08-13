<!-- ppt-master-schema: design-spec/v1 -->
# 灵犀客服 - Design Spec

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | 灵犀客服 |
| Canvas Format | PPT 16:9 (1280×720) |
| Page Count | 19 |
| Primary Language | zh-CN |
| Target Audience | GOAI 智能客服自主闭环赛道评委 |
| Communication Intent | 先结论后展开：先给一页纸速览，再按评分维度逐章论证 |
| Desired Audience Outcome | 评委认可其多 Agent 协同、Skill 工程与工程落地的真实可信度 |
| Core Message / Ask / Action | 灵犀客服用 6 Agent 闭环实现客服自主闭环，且已跑通端到端实测 |
| Delivery Context | 现场答辩演示 |
| Artifact Afterlife | 初赛方案评审材料，可复用为后续复赛/决赛基础 |
| Reading Mode | presentation |
| Content Strategy | balanced |
| Design Style | 暖色专业风（扁平卡片、留白、数据驱动） |
| Formula Policy | text-only |
| AI Image Acquisition Path | not applicable |
| Generation Mode | continuous |
| Spec Refinement | disabled |
| Speaker Notes | disabled — workflow default |
| Custom Animations | disabled — workflow default |
| Narration Audio | disabled — workflow default |
| Created Date | 2026-08-13 |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 60px |
| Content Area | 60–1220 × 60–660 |

## III. Visual Theme

### Theme Style

- **Mode**: custom
- **Visual style**: custom
- **Theme**: 暖色专业风 —— 奶油底色 + 陶土橙主色 + 琥珀强调
- **Tone**: 专业、亲切、数据驱动

### Color Scheme

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | #FDF4E7 | 奶油暖底，全局背景 |
| Secondary background | #FFFFFF | 卡片/面板表面 |
| Primary | #E8590C | 标题、主按钮、章节强调 |
| Accent | #F5A524 | 琥珀强调、编号、高亮 |
| Secondary accent | #E76F51 | 珊瑚辅助、数据标注 |
| Body text | #3B2C24 | 正文暖深棕 |

## IV. Typography System

### Font Plan

| Role | Character (Reference) | Primary | English if non-English | Fallback tail |
| --- | --- | --- | --- | --- |
| Title | sans / bold | Microsoft YaHei | Arial | SimHei, sans-serif |
| Body | sans / regular | Microsoft YaHei | Arial | SimHei, sans-serif |

- **Title stack**: Microsoft YaHei, SimHei, sans-serif
- **Body stack**: Microsoft YaHei, SimHei, sans-serif

### Font Size Hierarchy

| Purpose | Anchor Size (px) |
| --- | ---: |
| Body | 24 |
| Title | 40 |
| Subtitle | 28 |
| Annotation | 16 |
| Label | 20 |
| Section | 56 |
| Metric | 48 |
| TOC | 32 |

## V. Layout Principles

### Page Structure

- **Header area**: 左上角章节标签（小字）+ 页面标题（大标题），右侧页码
- **Content area**: 卡片化内容区，居中留白，信息分组清晰
- **Footer area**: 底部细线 + 项目名「灵犀客服」小字

### Spacing Specification

| Element | Current Project |
| --- | --- |
| Safe margin | 60px |
| Content block gap | 32px |
| Icon-text gap | 12px |

## VI. Icon Usage Specification

- **Primary bundled library**: none

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Crop Policy | Acquire Via | Status | Reference | text_policy | page_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## IX. Content Outline

### Part 1: 开场

#### Slide 01 - 封面

- **Audience move**: 陌生 → 记住项目名与定位
- **Layout**: 居中大标题 + 副标题 + 底部赛道标签
- **Title**: 灵犀客服
- **Core message**: 多 Agent 智能客服自主闭环系统
- **Content**: 主标题「灵犀客服」，副标题「多 Agent 智能客服自主闭环系统」，底部「GOAI 智能客服自主闭环赛道 · 参赛作品」

#### Slide 02 - P0 一页纸速览

- **Audience move**: 记住项目名 → 快速掌握六要素
- **Layout**: 2×3 六宫格卡片
- **Title**: P0 · 一页纸速览
- **Core message**: 一页讲清项目全貌
- **Content**: 六格卡片：项目名称 / 问题与场景 / 核心解决方案 / 创新点与差异化 / 开放复用价值 / 当前进展

#### Slide 03 - 目录

- **Audience move**: 快速掌握全貌 → 建立章节地图
- **Layout**: 双列编号目录
- **Title**: 目录
- **Core message**: 八章评分框架
- **Content**: 8 章列表（含评分权重标注）

### Part 2: 第一章 场景与价值

#### Slide 04 - 章节页

- **Audience move**: 进入第一章语境
- **Layout**: 章节号 + 标题 + 评分维度卡（25%）
- **Title**: 场景与价值
- **Core message**: 对应评分维度 25%
- **Content**: 第一章 · 场景与价值 · 对应评分维度「场景价值与行业可复制性」25%

#### Slide 05 - 内容页

- **Audience move**: 了解痛点与价值
- **Layout**: 左侧四痛点卡片 + 右侧价值测算大卡
- **Title**: 客服在人海，经验在人脑
- **Core message**: 四大痛点 + 可量化价值
- **Content**: 痛点：多渠道工单分散 / 意图分类靠人工 / 退款换货链路长 / 知识沉淀断层；价值：日 2000 工单 × 70% 自动化 → 月释放约 700 人天

### Part 3: 第二章 方案总览

#### Slide 06 - 章节页

- **Audience move**: 进入方案总览
- **Layout**: 章节号 + 标题
- **Title**: 方案总览
- **Core message**: 端到端主流程
- **Content**: 第二章 · 方案总览

#### Slide 07 - 内容页

- **Audience move**: 理解整体架构
- **Layout**: 四层架构横向流程图
- **Title**: 四层架构，一条闭环
- **Core message**: 接入 → 编排 → 执行 → 沉淀
- **Content**: 接入层（cs-gather 聚合）→ 编排层（Manager-Worker + Matrix）→ 执行层（Skill + MCP + RAG）→ 沉淀层（知识库回写）

### Part 4: 第三章 多 Agent 协同设计

#### Slide 08 - 章节页

- **Audience move**: 进入多 Agent 协同
- **Layout**: 章节号 + 标题 + 评分维度卡（25%）
- **Title**: 多 Agent 协同设计
- **Core message**: 对应评分维度 25%
- **Content**: 第三章 · 多 Agent 协同设计 · 对应评分维度「多 Agent 协同与自主闭环能力」25%

#### Slide 09 - 内容页

- **Audience move**: 理解协同机制与安全边界
- **Layout**: 6 Agent 分工卡 + 底部证据链/审批条
- **Title**: 6 Agent 接力，全程可审计
- **Core message**: 分工 + 证据链 + 审批
- **Content**: 6 Agent 分工表；每单 9 文件证据链；>100 元强制审批 + 幂等 + 回滚；异常经复盘沉淀强约束规则

### Part 5: 第四章 Skill 工程体系

#### Slide 10 - 章节页

- **Audience move**: 进入 Skill 工程
- **Layout**: 章节号 + 标题 + 评分维度卡（25%）
- **Title**: Skill 工程体系
- **Core message**: 对应评分维度 25%（本赛题必选项）
- **Content**: 第四章 · Skill 工程体系 · 对应评分维度「Skill 工程体系与生态复用」25%

#### Slide 11 - 内容页

- **Audience move**: 理解 Skill 规格与复用
- **Layout**: 6 Skill 卡片网格
- **Title**: 6 个 Skill，9 要素规格
- **Core message**: 规则优先 + LLM 兜底 + 可复用
- **Content**: 6 个 Skill（聚合/意图/方案/执行/核验/沉淀），每个含 9 要素规格；规则优先 + LLM 兜底；可发布市场

### Part 6: 第五章 工程落地、运行验证与安全可审计

#### Slide 12 - 章节页

- **Audience move**: 进入工程落地
- **Layout**: 章节号 + 标题 + 评分维度卡（20%）
- **Title**: 工程落地、运行验证与安全可审计
- **Core message**: 对应评分维度 20%
- **Content**: 第五章 · 工程落地、运行验证与安全可审计 · 对应评分维度「工程落地与安全可审计」20%

#### Slide 13 - 内容页

- **Audience move**: 相信系统真实可运行
- **Layout**: 左侧压测数据 + 右侧可观测/合规
- **Title**: 10 单压测，平均 5 分钟
- **Core message**: 实测数据 + 可观测 + 安全治理
- **Content**: 10 单批量压测 10/10 完成，每单约 5 分钟；云监控 AI Agent 可观测接入；合规复盘沉淀强约束规则

### Part 7: 第六章 开放 / 开源计划

#### Slide 14 - 章节页

- **Audience move**: 进入开源计划
- **Layout**: 章节号 + 标题 + 评分维度卡（5%）
- **Title**: 开放 / 开源计划
- **Core message**: 对应评分维度 5%
- **Content**: 第六章 · 开放 / 开源计划 · 对应评分维度「开放 / 开源贡献」5%

#### Slide 15 - 内容页

- **Audience move**: 了解复用与开源
- **Layout**: 三列复用点
- **Title**: 代码开源，Skill 进市场
- **Core message**: 可部署包 + Skill 市场 + 本地部署
- **Content**: 可部署代码包；6 Skill 发布市场；接口契约与文档；本地私有化部署

### Part 8: 第七章 落地计划与进展

#### Slide 16 - 章节页

- **Audience move**: 进入落地计划
- **Layout**: 章节号 + 标题
- **Title**: 落地计划与进展
- **Core message**: 当前进展与整体可行性
- **Content**: 第七章 · 落地计划与进展

#### Slide 17 - 内容页

- **Audience move**: 了解路线图与风险控制
- **Layout**: 三阶段横向路线图
- **Title**: 三阶段，稳步推进
- **Core message**: 已完成 → 复赛 → 决赛
- **Content**: 阶段一（已完成）部署+跑通+压测；阶段二（复赛）MCP 化 + RAG；阶段三（决赛）指标量化 + Skill 市场

### Part 9: 第八章 团队介绍

#### Slide 18 - 章节页

- **Audience move**: 进入团队介绍
- **Layout**: 章节号 + 标题
- **Title**: 团队介绍
- **Core message**: 成员背景与分工
- **Content**: 第八章 · 团队介绍

#### Slide 19 - 内容页

- **Audience move**: 了解团队构成
- **Layout**: 成员卡片
- **Title**: 团队成员
- **Core message**: 成员背景、分工、成果
- **Content**: 成员背景（学校/公司、岗位/专业、核心技能）；团队分工；团队成果（占位待填）

## X. Speaker Notes Requirements

- **Generation**: disabled
