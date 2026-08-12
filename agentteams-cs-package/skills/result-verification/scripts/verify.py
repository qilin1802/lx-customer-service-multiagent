#!/usr/bin/env python3
"""result-verification skill 配套脚本：核验执行结果与满意度解析。"""
import json
import sys

# Mock 查询（真实环境替换为 MCP 只读工具）
_VERIFIED_ACTIONS = {"refund": "退款到账", "exchange": "换货物流已发", "account_change": "账户已变更"}


def verify(report):
    """核验执行结果。"""
    if report.get("status") != "success":
        return {"verification": "failed", "checked": [], "satisfaction": "no_response", "escalate": True}

    action = report.get("action")
    checks = [_VERIFIED_ACTIONS.get(action, "操作完成")]
    # Mock：默认核验通过（真实环境查询业务系统比对预期）
    return {"verification": "success", "checked": checks, "satisfaction": "no_response", "escalate": False}


def parse_feedback(text):
    """解析客户满意度回复。"""
    if any(w in text for w in ["满意", "好的", "谢谢", "ok", "可以"]):
        return "satisfied"
    if any(w in text for w in ["不满", "差评", "投诉", "不行", "生气"]):
        return "unsatisfied"
    return "no_response"


if __name__ == "__main__":
    data = json.load(sys.stdin)
    if "feedback" in data:
        print(json.dumps({"satisfaction": parse_feedback(data["feedback"]), "escalate": False},
                         ensure_ascii=False, indent=2))
    else:
        print(json.dumps(verify(data.get("report", {})), ensure_ascii=False, indent=2))
