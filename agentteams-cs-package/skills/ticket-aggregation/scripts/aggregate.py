#!/usr/bin/env python3
"""ticket-aggregation skill 配套脚本：消息归一化 + 三级去重。

去重策略（先精确 → 再相似 → 语义交 LLM）：
- exact    ：归一化后内容哈希相同 → 直接合并（最快，零 LLM）
- similar  ：文本相似度 >= 0.85 → 合并
- semantic ：相似度 0.5 ~ 0.85 → 标记 needs_semantic_check，交 LLM 语义复核

用法：cat messages.json | python aggregate.py
"""
import hashlib
import json
import re
import sys
from difflib import SequenceMatcher

SIMILAR_THRESHOLD = 0.85
SEMANTIC_FLOOR = 0.35


def normalize_identity(hints):
    """归一化客户身份标识，返回稳定 customer_id。"""
    phone = (hints.get("phone") or "").strip().replace("-", "").replace(" ", "")
    email = (hints.get("email") or "").strip().lower()
    username = (hints.get("username") or "").strip().lower()
    for key in (phone, email, username):
        if key:
            return "CUST-" + hashlib.sha256(key.encode()).hexdigest()[:10]
    return "CUST-UNKNOWN"


def normalize_content(text):
    """规范化文本（去空白），用于精确去重。"""
    return re.sub(r"\s+", "", text or "")


def _bigrams(text):
    """字符二元组集合，对中文更稳健、抗重排。"""
    if len(text) < 2:
        return {text}
    return {text[i:i + 2] for i in range(len(text) - 1)}


def similarity(a, b):
    if not a or not b:
        return 0.0
    ratio = SequenceMatcher(None, a, b).ratio()
    ba, bb = _bigrams(a), _bigrams(b)
    if not ba or not bb:
        return ratio
    jaccard = len(ba & bb) / len(ba | bb)
    return max(ratio, jaccard)


def aggregate(messages, threshold=SIMILAR_THRESHOLD):
    tickets = []
    for msg in messages:
        customer_id = normalize_identity(msg.get("customer_hints", {}))
        norm = normalize_content(msg.get("content", ""))
        content_hash = hashlib.sha256(norm.encode()).hexdigest()[:16]

        merged = False
        semantic_candidates = []

        for t in tickets:
            if t["customer_id"] != customer_id:
                continue
            # 1. 精确去重
            if t["_hash"] == content_hash:
                t["merged_from"].append(msg["session_id"])
                t["deduplicated"] = True
                t["dedup_reason"] = "exact"
                merged = True
                break
            # 2. 相似去重
            sim = similarity(norm, normalize_content(t["raw_message"]))
            if sim >= threshold:
                t["merged_from"].append(msg["session_id"])
                t["deduplicated"] = True
                t["dedup_reason"] = "similar"
                merged = True
                break
            # 3. 语义待复核（不阻断，记录候选）
            if sim >= SEMANTIC_FLOOR:
                semantic_candidates.append({
                    "ticket_id": t["ticket_id"],
                    "similarity": round(sim, 2),
                })

        if merged:
            continue

        tickets.append({
            "ticket_id": f"TK-{msg.get('timestamp', '')[:10]}-{len(tickets) + 1:04d}",
            "channel": msg.get("channel", "unknown"),
            "customer_id": customer_id,
            "customer_contact": msg.get("customer_hints", {}).get("phone", ""),
            "summary": msg["content"][:80],
            "raw_message": msg["content"],
            "deduplicated": False,
            "dedup_reason": None,
            "merged_from": [],
            "needs_semantic_check": bool(semantic_candidates),
            "semantic_candidates": semantic_candidates,
            "_hash": content_hash,
        })

    for t in tickets:
        t.pop("_hash", None)
    return tickets


if __name__ == "__main__":
    data = json.load(sys.stdin)
    result = aggregate(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
