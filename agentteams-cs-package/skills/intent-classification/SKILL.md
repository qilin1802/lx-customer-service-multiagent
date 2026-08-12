---
name: intent-classification
description: Use when classifying customer ticket intent (refund, exchange, complaint, account change, inquiry), extracting slots (order id, amount, emotion), or grading urgency P0-P2. Triggered by cs-intent.
---

# Intent Classification

客服工单意图识别与分级。识别客户意图、抽取关键槽位、判定紧急度，输出结构化 JSON。

## 输入

标准工单 JSON（来自 cs-gather，或直接会话文本）

## 输出

```json
{
  "intent": "refund|exchange|account_change|complaint|pre_sales|after_sales|other",
  "confidence": 0.95,
  "slots": { "order_id": "string", "product": "string", "amount": "number", "preferred_action": "string" },
  "urgency": "P0|P1|P2",
  "needs_human_review": false
}
```

## 调用条件

- 标准工单就绪时触发
- 由 cs-intent 调用
- 置信度 < 0.7 时输出 `needs_human_review: true`

## 依赖工具

- LLM 分类（Few-shot 提示）
- 规则引擎兜底（关键词匹配：退款/退货/投诉/改地址…）

## 失败处理

- LLM 超时或返回非 JSON → 规则匹配兜底
- 兜底仍无法判定 → 标记 `needs_human_review`，不擅自定级

## 安全边界

- 只做分析，不执行任何操作
- 涉密槽位（密码、验证码）识别后即丢弃，不写入输出

## 复用价值

工单系统、报警分类、邮件路由等文本分类场景通用。

## 协同关系

承接 cs-gather 的标准工单，结果作为 cs-handler 方案生成的决策输入。
