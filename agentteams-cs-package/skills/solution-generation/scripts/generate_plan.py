#!/usr/bin/env python3
"""solution-generation skill 配套脚本：方案生成与审批等级判定。"""
import json
import sys

HIGH_AMOUNT = 100.0  # 超过此金额需审批
HIGH_RISK_INTENTS = {"complaint"}
ESCALATE = {"other"}


def generate(intent_analysis):
    """根据意图分析生成处理方案。"""
    intent = intent_analysis.get("intent", "other")
    slots = intent_analysis.get("slots", {})
    amount = slots.get("amount", 0.0)

    if intent in ESCALATE:
        return {
            "action": "escalate",
            "parameters": {"reason": "意图无法自动处理"},
            "approval_level": "high",
            "rationale": "意图不在自动处理范围内，转人工",
            "risk_notes": [],
        }

    plan = {
        "refund": {
            "action": "refund",
            "parameters": {"order_id": slots.get("order_id"), "amount": amount, "reason": "客户申请退款"},
            "approval_level": "high" if amount > HIGH_AMOUNT else "low",
            "risk_notes": ["金额超限"] if amount > HIGH_AMOUNT else [],
        },
        "exchange": {
            "action": "exchange",
            "parameters": {"order_id": slots.get("order_id"), "product": slots.get("product"), "reason": "客户申请换货"},
            "approval_level": "low",
            "risk_notes": [],
        },
        "account_change": {
            "action": "account_change",
            "parameters": {"order_id": slots.get("order_id"), "reason": "客户申请账户变更"},
            "approval_level": "high",
            "risk_notes": ["账户敏感操作"],
        },
        "pre_sales": {
            "action": "escalate",
            "parameters": {"reason": "售前咨询需人工跟进"},
            "approval_level": "low",
            "risk_notes": [],
        },
        "after_sales": {
            "action": "exchange",
            "parameters": {"order_id": slots.get("order_id"), "reason": "售后维修/换新"},
            "approval_level": "low",
            "risk_notes": [],
        },
    }

    result = plan.get(intent, plan["refund"])
    if intent in HIGH_RISK_INTENTS:
        result["approval_level"] = "high"
        result["risk_notes"].append("投诉类需审批")
    result["rationale"] = f"基于意图 {intent} 生成方案，参考知识库历史案例"
    return result


if __name__ == "__main__":
    data = json.load(sys.stdin)
    print(json.dumps(generate(data), ensure_ascii=False, indent=2))
