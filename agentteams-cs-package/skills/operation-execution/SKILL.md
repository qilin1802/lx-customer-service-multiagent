---
name: operation-execution
description: Use when executing an approved business operation (refund, exchange, account change) against the business system, with idempotency control and rollback support. Triggered by cs-handler.
---

# Business Operation Execution

执行已批准的业务操作（退款/换货/账户变更），保证幂等、可重试、可回滚。

## 输入

已批准方案 JSON（含 `approval_level` 与审批凭证）

## 输出

```json
{
  "execution_id": "EXE-2026-0001",
  "action": "refund",
  "status": "success|failed|pending_approval",
  "evidence": { "order_id": "string", "refund_no": "string", "amount": "number" },
  "retries": 0,
  "rollback_available": true
}
```

## 调用条件

- 低风险方案直接执行
- 高风险方案必须先获得 cs-approver 的批准凭证（`approval_token`）
- 同一工单不重复执行（幂等键：`ticket_id + action`）

## 依赖工具

- 业务系统 API（Mock 或真实 MCP Server）
- 幂等键存储

## 失败处理

- 执行失败重试 1 次
- 仍失败 → 转人工并记录原因
- 可回滚操作：失败后发起回滚（撤销退款/恢复账户）

## 安全边界

- 幂等控制：同一工单+动作只执行一次
- 凭据由网关统一管理，Worker 不持有密钥
- 审计日志记录每次执行与回滚

## 复用价值

任何需要"安全自动执行"的业务操作（工单关停、资源配置、批量变更）。

## 协同关系

承接收 cs-handler 的方案与审批结果，执行报告交给 cs-verify 核验。
