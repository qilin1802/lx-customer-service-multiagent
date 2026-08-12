#!/usr/bin/env python3
"""knowledge-distillation skill 配套脚本：复盘报告与 FAQ 提炼。"""
import json
import sys


def distill(ticket_log):
    """从工单日志提炼复盘结论与 FAQ。"""
    report = {
        "case": ticket_log.get("ticket_id", "unknown"),
        "outcome": ticket_log.get("outcome", "success"),
        "failure_reason": ticket_log.get("failure_reason", "无"),
        "bottleneck": ticket_log.get("bottleneck", "无"),
        "suggestion": "优化提示词与知识库覆盖" if ticket_log.get("outcome") == "failed" else "流程顺畅，保持现状",
    }
    faqs = []
    if ticket_log.get("outcome") == "success":
        q = ticket_log.get("customer_question", "")
        a = ticket_log.get("resolution", "")
        if q and a:
            faqs.append({"question": q, "answer": a})
    return {
        "report": json.dumps(report, ensure_ascii=False),
        "new_faqs": faqs,
        "rule_updates": [{"rule": "high_amount_refund_needs_approval", "action": "add"}]
                       if ticket_log.get("needs_approval") else [],
        "kb_write_status": "pending",
    }


if __name__ == "__main__":
    data = json.load(sys.stdin)
    print(json.dumps(distill(data), ensure_ascii=False, indent=2))
