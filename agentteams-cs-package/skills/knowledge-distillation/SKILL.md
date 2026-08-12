---
name: knowledge-distillation
description: Use when generating post-mortem reports for completed tickets, distilling FAQ entries, or writing back knowledge to the knowledge base. Triggered by cs-review.
---

# Knowledge Distillation

对完结工单生成复盘报告，提炼 FAQ 与处理规则，回写知识库形成反馈回路。

## 输入

完结工单全流程记录（含失败/转人工案例）

## 输出

```json
{
  "report": "复盘报告（失败原因、流程断点、优化建议）",
  "new_faqs": [{ "question": "string", "answer": "string" }],
  "rule_updates": [{ "rule": "string", "action": "update|add" }],
  "kb_write_status": "pending|written"
}
```

## 调用条件

- 工单完结后触发
- 由 cs-review 调用
- 知识库写入需经 Manager 审核

## 依赖工具

- 知识库写入 API（向量库）
- 复盘模板

## 失败处理

- 写入失败 → 保留草稿并通知 Manager 人工处理

## 安全边界

- 沉淀前自动脱敏（去除客户隐私信息）
- 写入需审核，防止知识污染

## 复用价值

知识库运营、培训材料生成、质检报告场景通用。

## 协同关系

承接 cs-verify 核验结论，新知识反哺 intent-classification 与 solution-generation（RAG 检索），形成闭环。
