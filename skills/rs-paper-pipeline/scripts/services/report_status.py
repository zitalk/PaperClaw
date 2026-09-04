"""Public report provenance and run health; no API credentials or raw errors."""
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone

REPORT_MARKER = "<!-- paperclaw-report: zitalk/PaperClaw -->"


def read_run_status(body: str) -> dict:
    match = re.search(r"<!-- paperclaw-run: (\{[^\n]+\}) -->", body or "")
    if match:
        try:
            value = json.loads(match.group(1))
            return value if isinstance(value, dict) else {}
        except ValueError:
            pass
    return {}


def run_status(stats: dict | None, failed_items: list | None = None) -> dict:
    stats = stats or {}
    sources = stats.get("source_status") or []
    unavailable = [s["name"] for s in sources if s.get("status") == "unavailable"]
    skipped = [s["name"] for s in sources if s.get("status") == "not_configured"]
    warnings = stats.get("filter_warnings") or []
    failed = failed_items or stats.get("failed_items") or []
    status = "degraded" if unavailable or warnings or failed else ("ok" if sources else "unknown")
    return {
        "status": status,
        "checked_at": datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds"),
        "unavailable_sources": unavailable,
        "unconfigured_sources": skipped,
        "filter_fallback": bool(warnings),
        "failed_papers": len(failed),
    }


def status_heading(run: dict) -> str:
    label = {"ok": "检索完成", "degraded": "检索完成，但存在异常", "unknown": "检索统计已生成（来源状态未记录）"}[run["status"]]
    time_text = run["checked_at"].replace("T", " ").replace("+08:00", "（北京时间）")
    return f"{label} · 最近检查：{time_text}"


def status_details(run: dict) -> list[str]:
    lines = []
    if run["unavailable_sources"]:
        lines.append("部分来源不可用：" + "、".join(run["unavailable_sources"]) + "；本次结果不代表完整覆盖。")
    if run["unconfigured_sources"]:
        lines.append("未配置、未参与检索：" + "、".join(run["unconfigured_sources"]) + "。")
    if run["filter_fallback"]:
        lines.append("部分 LLM 输出解析失败，已降级为关键词筛选。")
    if run["failed_papers"]:
        lines.append(f"有 {run['failed_papers']} 篇匹配论文处理失败，请查看日报失败明细。")
    return lines


def run_marker(run: dict) -> str:
    return REPORT_MARKER + "\n<!-- paperclaw-run: " + json.dumps(run, ensure_ascii=False) + " -->"


def daily_encouragement(date: str) -> str:
    quotes = (
        "今天没有新论文，也可以把昨天的一个问题想得更清楚。",
        "研究的进展，常常藏在持续积累的每一个小步里。",
        "不必每天都有新发现，但可以每天多一点理解。",
        "留一点时间给思考，好的问题值得耐心打磨。",
    )
    return quotes[datetime.strptime(date, "%Y%m%d").toordinal() % len(quotes)]
