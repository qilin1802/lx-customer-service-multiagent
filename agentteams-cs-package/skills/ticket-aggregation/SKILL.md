---
name: ticket-aggregation
description: Use when ingesting raw customer messages from multiple channels (email, online chat, phone transcription, social media comments), normalizing customer identity, or deduplicating repeated tickets. Triggered by cs-gather.
---

# Ticket Aggregation

跨渠道客服消息聚合与去重。将多渠道原始消息归一化为标准工单，识别同一客户并合并重复工单。

## 输入

```json
{
  "channel": "email|chat|phone|social",
  "session_id": "string",
  "content": "原始消息文本",
  "timestamp": "ISO-8601",
  "customer_hints": { "phone": "string", "email": "string", "username": "string" }
}
```

## 输出

```json
{
  "ticket_id": "TK-2026-0001",
  "channel": "string",
  "customer_id": "CUST-001",
  "customer_contact": "string",
  "summary": "诉求摘要",
  "raw_message": "原始消息",
  "deduplicated": true,
  "merged_from": ["TK-2026-0001-a"]
}
```

## 调用条件

- 新消息到达时触发
- 由 cs-gather 调用
- 同一客户 24 小时内的相似消息执行去重合并

## 依赖工具

- 向量检索（相似度匹配，阈值 ≥ 0.85）
- 客户身份索引（手机号 / 邮箱 / 用户名归一化）

## 失败处理

- 相似度计算异常 → 跳过去重，保守创建新工单并标记 `"deduplicated": false`
- 身份归一化冲突 → 保留全部候选标识，标注"需人工确认"

## 安全边界

- 原始消息含敏感信息（密码 / 卡号）时先脱敏再入库
- 客户联系方式仅用于本工单关联，不外传

## 复用价值

任何多入口业务系统（OA、电商、运维工单）均可复用此聚合模式。

## 协同关系

cs-gather 的专属技能，产出的标准工单 JSON 喂给 cs-intent 进行意图识别。
