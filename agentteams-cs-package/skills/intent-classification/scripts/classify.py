#!/usr/bin/env python3
"""intent-classification skill 配套脚本：规则优先，先规则后 LLM。

三级路由：
- rule  ：规则高置信（>= 0.7），直接出结论，跳过 LLM，省时省 token
- llm   ：规则中置信（0.3 ~ 0.7）或无信号，附候选意图，交 Agent 用 LLM 复核
- 转人工：仅当高紧急度（P0 投诉）或显式要求人工时 needs_human_review=true

用法：echo '{"content": "客户原始消息"}' | python classify.py
"""
import json
import re
import sys

# 强词：命中即高置信；弱词：需多命中才可信
STRONG_RULES = [
    ("refund", ["退款", "退钱", "退货", "退掉", "全额退", "refund"]),
    ("exchange", ["换货", "换一件", "换大", "换小", "exchange"]),
    ("account_change", ["改地址", "改收货", "换手机号", "改密码", "改绑"]),
    ("complaint", ["投诉", "举报", "差评", "维权", "12315"]),
    ("pre_sales", ["多少钱", "有货吗", "怎么买", "有没有货", "推荐"]),
    ("after_sales", ["坏了", "碎了", "不工作", "失灵", "开不了机", "维修", "没声音", "故障"]),
]
WEAK_RULES = [
    ("refund", ["退", "不要了", "取消订单"]),
    ("exchange", ["换", "尺码", "颜色不对"]),
    ("account_change", ["改", "变更"]),
    ("complaint", ["太过分", "敷衍", "不负责任"]),
    ("pre_sales", ["想买", "下单", "咨询"]),
    ("after_sales", ["有问题", "售后"]),
]
URGENCY_RULES = {
    "P0": ["投诉", "举报", "维权", "12315", "高额", "紧急", "报警"],
    "P1": ["退款", "退钱", "退货", "换货"],
    "P2": ["多少钱", "怎么买", "有货吗", "咨询"],
}
HUMAN_KEYWORDS = ["转人工", "人工客服", "找经理", "我要投诉"]

CONFIDENT = 0.7
LLM_FLOOR = 0.3


def classify(text):
    """返回 (intent, confidence, top_candidates, matched_keywords)。"""
    scores = {}
    matched = {}
    for intent, kws in STRONG_RULES:
        for k in kws:
            if k in text:
                scores[intent] = scores.get(intent, 0) + 2
                matched.setdefault(intent, []).append(k)
    for intent, kws in WEAK_RULES:
        for k in kws:
            if k in text:
                scores[intent] = scores.get(intent, 0) + 1
                matched.setdefault(intent, []).append(k)

    if not scores:
        return "other", 0.0, [], {}

    best = max(scores, key=scores.get)
    top = sorted(scores.items(), key=lambda x: -x[1])
    confidence = min(0.95, 0.3 + 0.2 * scores[best])
    return best, confidence, top, matched


def extract_slots(text):
    slots = {}
    m = re.search(r"(?:订单号|单号)[:：\s]*([A-Za-z0-9\-]{6,30})", text)
    if m:
        slots["order_id"] = m.group(1)
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:元|块|rmb|块钱)", text)
    if m:
        slots["amount"] = float(m.group(1))
    return slots


def urgency(intent, text):
    for level, keywords in URGENCY_RULES.items():
        if any(k in text for k in keywords):
            return level
    return {"refund": "P1", "exchange": "P1", "complaint": "P0"}.get(intent, "P2")


if __name__ == "__main__":
    data = json.load(sys.stdin)
    text = data.get("content", "")
    intent, confidence, top, matched = classify(text)
    slots = extract_slots(text)
    ur = urgency(intent, text)

    if confidence >= CONFIDENT:
        route = "rule"
    else:
        route = "llm"

    needs_human = ur == "P0" or any(k in text for k in HUMAN_KEYWORDS)

    print(json.dumps({
        "intent": intent,
        "confidence": round(confidence, 2),
        "slots": slots,
        "urgency": ur,
        "route": route,
        "needs_llm": route == "llm",
        "needs_human_review": needs_human,
        "candidates": [{"intent": i, "score": s} for i, s in top[:3]],
        "matched_keywords": matched,
    }, ensure_ascii=False, indent=2))
