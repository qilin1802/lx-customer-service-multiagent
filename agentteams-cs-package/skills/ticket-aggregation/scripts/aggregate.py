#!/usr/bin/env python3
"""ticket-aggregation skill 配套脚本：消息归一化 + 相似度去重。"""
import hashlib
import json
import sys
from difflib import SequenceMatcher


def normalize_identity(hints):
    """归一化客户身份标识，返回稳定 customer_id。"""
    phone = (hints.get("phone") or "").strip().replace("-", "").replace(" ", "")
    email = (hints.get("email") or "").strip().lower()
    username = (hints.get("username") or "").strip().lower()
    for key in (phone, email, username):
        if key:
            return "CUST-" + hashlib.sha256(key.encode()).hexdigest()[:10]
    return "CUST-UNKNOWN"


def similarity(a, b):
    """计算两段文本的相似度。"""
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def aggregate(messages, threshold=0.85):
    """聚合消息列表，返回工单列表（含去重合并）。"""
    tickets = []
    for msg in messages:
        customer_id = normalize_identity(msg.get("customer_hints", {}))
        merged = False
        for t in tickets:
            if t["customer_id"] == customer_id:
                sim = similarity(msg["content"], t["raw_message"])
                if sim >= threshold:
                    t["merged_from"].append(msg["session_id"])
                    merged = True
                    break
        if not merged:
            tickets.append({
                "ticket_id": f"TK-{msg.get('timestamp', '')[:10]}-{len(tickets)+1:04d}",
                "channel": msg.get("channel", "unknown"),
                "customer_id": customer_id,
                "customer_contact": msg.get("customer_hints", {}).get("phone", ""),
                "summary": msg["content"][:80],
                "raw_message": msg["content"],
                "deduplicated": False,
                "merged_from": [],
            })
    return tickets


if __name__ == "__main__":
    data = json.load(sys.stdin)
    result = aggregate(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
