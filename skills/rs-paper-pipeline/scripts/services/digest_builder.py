#!/usr/bin/env python3
from __future__ import annotations

import json
import re

from clients.llm_client import call_llm
from services.paper_analysis import is_valid_institution_text
from services.report_status import daily_encouragement, run_marker, run_status, status_details, status_heading


def extract_author(body: str) -> str:
    match = re.search(r"\| \*\*作者\*\* \|([^|]+)\|", body or "")
    return match.group(1).strip() if match else "-"


def extract_institution(body: str) -> str:
    match = re.search(r"\| \*\*(?:单位|机构)\*\* \|([^|]+)\|", body or "")
    return match.group(1).strip() if match else "-"


def is_invalid_digest_field(value: str) -> bool:
    normalized = (value or "").strip()
    return normalized in {"", "-", "待提取", "未知", "Unknown", "N/A"}


def is_invalid_digest_institution(value: str) -> bool:
    return not is_valid_institution_text(value)


def validate_papers_for_digest(papers: list[dict]) -> list[str]:
    errors: list[str] = []
    for paper in papers:
        title = extract_report_title(paper)
        authors = extract_author(paper.get("body") or "")
        if is_invalid_digest_field(authors) or "et al." in authors:
            errors.append(f"{title}: 作者信息不合格")
    return errors


def display_institution(body: str) -> str:
    institution = extract_institution(body)
    return "暂无" if is_invalid_digest_institution(institution) else institution


def extract_report_title(issue: dict) -> str:
    body = issue.get("body") or ""
    match = re.search(r"^#\s*\[(\d{8})\]\s+(.+)$", body, re.MULTILINE)
    if match:
        return f"[{match.group(1)}] {match.group(2).strip()}"
    return issue.get("title") or ""


def extract_paper_date(issue: dict) -> str | None:
    for label in issue.get("labels", []):
        name = label.get("name", "") if isinstance(label, dict) else ""
        if re.fullmatch(r"\d{8}", name):
            return name

    body = issue.get("body") or ""
    body_match = re.search(r"\[(\d{8})\]", body)
    if body_match:
        return body_match.group(1)

    title_match = re.match(r"^\[(\d{8})\]\s+", issue.get("title") or "")
    return title_match.group(1) if title_match else None


def build_digest_with_llm(date: str, papers: list, stats: dict | None = None, failed_items: list[dict] | None = None) -> str:
    failed_items = failed_items or (stats or {}).get("failed_items") or []
    health = run_status(stats, failed_items)
    if not papers and (stats or {}).get("llm_selected_count", 0):
        health["status"] = "degraded"
    items = []
    for i, paper in enumerate(papers, 1):
        labels = [label["name"] for label in paper.get("labels", []) if label["name"] not in [date, "日报"]]
        items.append(
            {
                "idx": i,
                "issue": paper["number"],
                "title": extract_report_title(paper),
                "authors": extract_author(paper.get("body") or ""),
                "institution": display_institution(paper.get("body") or ""),
                "labels": labels,
                "url": paper["html_url"],
            }
        )

    if not items:
        candidate_count = (stats or {}).get("candidate_count", 0)
        llm_selected_count = (stats or {}).get("llm_selected_count", len(failed_items or []))
        overview_text = (
            f"{status_heading(health)}\n\n"
            f"今日共检索候选论文 {candidate_count} 篇；"
            f"{_venue_stats_text(stats)}"
            f"关键词+LLM 智能匹配研究方向论文 {llm_selected_count} 篇；"
            "最终纳入日报 0 篇。"
        )
        if failed_items:
            overview_text += "当日筛中论文均未通过处理或质检，未纳入日报。"
        elif llm_selected_count:
            overview_text += "存在匹配论文，但没有成功归档记录，需要核查，不能视为正常零结果。"
        else:
            overview_text += "当日未检索到符合条件并纳入日报的论文。"
        overview_text += " " + " ".join(status_details(health))

        lines = [f"# 日报 {date}", "", run_marker(health), "", "## 📌 今日概况", "", overview_text, ""]
        append_failed_items(lines, failed_items)
        lines += [
            "## ✨ 今日亮点",
            "",
            "- " + (daily_encouragement(date) if health["status"] != "degraded" else "本次有异常，请查看来源状态及失败明细；不能将部分结果当作完整检索结果。"),
            "",
            "## 🔎 检索说明",
            "",
            "- 日报日期是论文检索目标日期；最近检查时间是任务实际执行时间。",
            "- 零结果不代表所有来源当天没有新论文，只表示本次未纳入符合条件的论文。",
            "- 同一日期后续补扫会更新这份日报，不重复创建日报 Issue。",
            "",
            "---",
            "",
            "Powered by OpenClaw🦞",
        ]
        return "\n".join(lines)

    prompt = (
        "你是多模态视觉与无人机视觉论文日报编辑。请基于给定论文列表输出严格JSON：\n"
        "{\n"
        '  "overview": "120-180字，概述今日研究趋势",\n'
        '  "highlights": ["3条，每条20-40字"],\n'
        '  "one_liners": [{"idx":1,"summary":"每篇一句话，25-45字"}],\n'
        '  "observations": ["2条，偏分析判断，每条24-48字"]\n'
        "}\n"
        "要求：中文、客观、不要编造细节。\n\n"
        f"日期: {date}\n候选: {json.dumps(items, ensure_ascii=False)}"
    )
    output = call_llm(prompt, max_tokens=1800, timeout=240)
    match = re.search(r"\{[\s\S]*\}", output)
    data = {"overview": "", "highlights": [], "one_liners": []}
    if match:
        try:
            data = json.loads(match.group(0))
        except Exception:
            pass

    one_liners = {
        item.get("idx"): item.get("summary", "")
        for item in data.get("one_liners", [])
        if isinstance(item, dict)
    }

    overview_text = data.get("overview") or "今日论文围绕多模态视觉、显著目标检测、跨视角跟踪与无人机感知展开。"
    candidate_count = (stats or {}).get("candidate_count")
    llm_selected_count = (stats or {}).get("llm_selected_count")
    included_count = len(items)

    if candidate_count is None:
        candidate_count = included_count
    if llm_selected_count is None:
        llm_selected_count = included_count

    overview_text = (
        f"{status_heading(health)}\n"
        f"今日共检索候选论文 {candidate_count} 篇；"
        f"{_venue_stats_text(stats)}"
        f"关键词+LLM 智能匹配研究方向论文 {llm_selected_count} 篇；"
        f"最终纳入日报 {included_count} 篇。\n\n{' '.join(status_details(health))} {overview_text}"
    )

    lines = [f"# 日报 {date}", "", run_marker(health), "", "## 📌 今日概况", "", overview_text, ""]

    highlights = data.get("highlights") or []
    if highlights:
        lines += ["## ✨ 今日亮点", ""]
        for highlight in highlights[:3]:
            lines.append(f"- {highlight}")
        lines.append("")

    lines += ["## 🗂 今日文章列表", "", "| 标题 | 作者 | 单位 | 一句话概括 | Issue |", "|---|---|---|---|---|"]
    for i, paper in enumerate(items, 1):
        summary = one_liners.get(i) or (
            f"聚焦{('、'.join(paper['labels'][:2]) if paper['labels'] else '多模态视觉方法')}，给出可复现的模型与评测方案。"
        )
        lines.append(
            f"| {paper['title']} | {paper['authors']} | {paper['institution']} | {summary} | [#{paper['issue']}]({paper['url']}) |"
        )

    append_failed_items(lines, failed_items)

    observations = data.get("observations") or [
        "多模态融合正从理想对齐设置转向缺失、错位和不确定模态下的鲁棒感知。",
        "无人机与多视角视觉持续关注小目标、跨视角关联和复杂环境泛化。",
    ]
    lines += ["", "## 🔎 观察", ""]
    for observation in observations[:2]:
        lines.append(f"- {observation}")

    lines += ["", "---", "", "Powered by OpenClaw🦞"]
    return "\n".join(lines)


def _venue_stats_text(stats: dict | None) -> str:
    if not stats or "venue_excluded_count" not in stats:
        return ""
    return (
        f"刊会准入通过 {stats.get('venue_admitted_count', 0)} 篇"
        f"（排除 {stats['venue_excluded_count']} 篇）；"
    )


def append_failed_items(lines: list[str], failed_items: list[dict] | None) -> None:
    if not failed_items:
        return

    lines += ["", "## ⚠️ 未纳入日报的匹配论文", ""]
    lines.append("以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。可通过来源链接查看原文。")
    lines.append("")
    lines.append("| 标题 | 来源 | 失败原因 |")
    lines.append("|------|-------|----------|")
    for item in failed_items:
        title = item.get("title", "Unknown")
        aid = item.get("paper_id") or item.get("arxiv_id", "")
        error = item.get("error") or item.get("reason") or "未知"
        source_url = item.get("url") or ""
        source_link = f"[{aid}]({source_url})" if aid and source_url else (aid or "-")
        lines.append(f"| {title} | {source_link} | {error} |")
    lines.append("")
