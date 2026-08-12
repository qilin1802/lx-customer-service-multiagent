---
name: solution-generation
description: Use when generating an executable handling plan (refund, exchange, account change) from intent analysis, including approval level determination. Triggered by cs-handler.
---

# Solution Generation

基于意图分析生成可执行处理方案，包含审批等级判定。高风险动作必须走人工审批。

## 输入

意图分析 JSON（来自 cs-intent）

## 输出

```json
{
  "action": "refund|exchange|account_change|escalate",
  "parameters": { "order_id": "string", "amount": "number", "reason": "string" },
  "approval_level": "low|high",
  "rationale": "方案依据（知识库/历史案例引用）",
  "risk_notes": ["金额超限", "首次退款"]
}
```

## 调用条件

- 意图分析完成后触发
- 由 cs-handler 调用
- `approval_level: high` 时必须经 cs-approver 审批后才可执行

## 依赖工具

- RAG 知识库检索（历史案例、FAQ、处理规范）
- 规则引擎（金额阈值、频次检测）

## 失败处理

- 检索无结果 → 标注"无历史参考"，给出保守方案
- 方案生成失败 → 重试 1 次 → 转人工

## 安全边界

- 只生成方案，不执行操作
- 参数范围校验（退款金额上限、订单号格式）

## 复用价值

运维工单处置建议、法务合规建议等决策场景通用。

## 协同关系

承接 cs-intent 意图分析，产出交给执行流程（含 cs-approver 审批）。
