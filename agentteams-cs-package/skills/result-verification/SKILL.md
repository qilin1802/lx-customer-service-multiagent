---
name: result-verification
description: Use when verifying business operation results against the system, sending customer satisfaction confirmation, or parsing customer feedback. Triggered by cs-verify.
---

# Result Verification

核验业务操作执行结果，向客户发送满意度确认，解析客户反馈。

## 输入

执行报告 JSON（来自 cs-handler）

## 输出

```json
{
  "verification": "success|failed|partial",
  "checked": ["退款到账", "换货物流已发"],
  "satisfaction": "satisfied|unsatisfied|no_response",
  "escalate": false
}
```

## 调用条件

- 执行报告到达后触发
- 由 cs-verify 调用

## 依赖工具

- 业务系统查询 API（只读）
- 情绪/满意度解析模型

## 失败处理

- 查询不可用 → 标记"待核验"延迟重试
- 客户 24 小时未回应 → `escalate: true` 升级转人工

## 安全边界

- 查询只读不写
- 客户联系方式仅用于本工单确认消息

## 复用价值

工单完结质检、回访系统、SLA 验证场景通用。

## 协同关系

承接 cs-handler 执行报告，结论触发 cs-review 复盘或升级转人工。
