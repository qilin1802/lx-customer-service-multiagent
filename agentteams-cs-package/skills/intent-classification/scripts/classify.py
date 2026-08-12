#!/usr/bin/env python3
"""intent-classification skill 配套脚本：规则兜底意图识别。"""
import json
import re
import sys

RULES = [
    ("refund", ["退款", "退钱", "退货", "退掉", "refund"]),
    ("exchange", ["换货", "换一个", "换件", "exchange"]),
    ("account_change", ["改地址", "换手机号", "改密码", "改绑", "账户变更"]),
    ("complaint", ["投诉", "差评", "举报", "太过分", "垃圾"]),
    ("pre_sales", ["多少钱", "有货吗", "怎么买", "咨询", "推荐"]),
    ("after_sales", ["坏了", "碎了", "不工作", "失灵", "维修", "售后"]),
]

URGENCY_RULES = {
    "P0": ["投诉", "高额", "人身", "紧急", "报警"],
    "P1": ["退款", "换货", "退货"],
    "P2": ["咨询", "多少钱", "怎么买"],
}


def classify(text):
    """规则引擎兜底分类，返回 (intent, confidence)。"""
    best = ("other", 0.0)
    for intent, keywords in RULES:
        hits = sum(1 for k in keywords if k in text)
        if hits and hits > best[1]:
            best = (intent, min(0.8, hits * 0.4))
    return best


def extract_slots(text):
    """抽取订单号与金额槽位。"""
    slots = {}
    m = re.search(r"(?:订单号|单号)[:：\s]*([A-Za-z0-9\-]{6,30})", text)
    if m:
        slots["order_id"] = m.group(1)
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:元|块|rmb)", text)
    if m:
        slots["amount"] = float(m.group(1))
    return slots


def urgency(intent, text):
    for level, keywords in URGENCY_RULES.items():
        if any(k in text for k in keywords):
            return level
    return {"refund": "P1", "exchange": "P1", "complaint": "P0"}.get(intent, "P2")


if __name__ == "__main__":
    text = json.load(sys.stdin).get("content", "")
    intent, conf = classify(text)
    print(json.dumps({
        "intent": intent,
        "confidence": conf,
        "slots": extract_slots(text),
        "urgency": urgency(intent, text),
        "needs_human_review": conf < 0.7,
    }, ensure_ascii=False, indent=2))
