#!/usr/bin/env python3
"""operation-execution skill 配套脚本：幂等执行模拟业务操作。"""
import hashlib
import json
import sys
import time

# Mock 业务系统（真实环境替换为 MCP 工具调用）
_MOCK_DB = {}


def _idempotency_key(ticket_id, action):
    return hashlib.sha256(f"{ticket_id}:{action}".encode()).hexdigest()


def _call_business_api(action, params):
    """模拟调用业务系统 API。真实环境由 MCP Server 提供。"""
    time.sleep(0.1)  # 模拟网络延迟
    if action == "refund":
        return {"refund_no": f"RF-{int(time.time())}", "status": "success"}
    if action == "exchange":
        return {"exchange_no": f"EX-{int(time.time())}", "status": "success"}
    if action == "account_change":
        return {"change_no": f"AC-{int(time.time())}", "status": "success"}
    raise ValueError(f"未知操作: {action}")


def execute(plan, approval_token=None):
    """执行方案。返回执行报告。"""
    action = plan["action"]
    params = plan.get("parameters", {})

    if plan.get("approval_level") == "high" and not approval_token:
        return {"execution_id": None, "action": action, "status": "pending_approval",
                "evidence": {}, "retries": 0, "rollback_available": True}

    key = _idempotency_key(params.get("order_id", "?"), action)
    if key in _MOCK_DB:
        return {**_MOCK_DB[key], "retries": 0, "note": "幂等命中，未重复执行"}

    last_error = None
    for attempt in range(2):  # 重试 1 次
        try:
            result = _call_business_api(action, params)
            report = {
                "execution_id": f"EXE-{int(time.time())}",
                "action": action,
                "status": "success",
                "evidence": {**params, **result},
                "retries": attempt,
                "rollback_available": True,
            }
            _MOCK_DB[key] = report
            return report
        except Exception as e:  # noqa: BLE001
            last_error = str(e)

    return {"execution_id": None, "action": action, "status": "failed",
            "evidence": {"error": last_error}, "retries": 1, "rollback_available": True}


if __name__ == "__main__":
    data = json.load(sys.stdin)
    print(json.dumps(execute(data.get("plan", {}), data.get("approval_token")),
                     ensure_ascii=False, indent=2))
