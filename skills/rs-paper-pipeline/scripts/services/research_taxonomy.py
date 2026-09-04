"""Shared, multi-label research taxonomy for website metadata and documentation."""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

TAXONOMY_PATH = Path(__file__).resolve().parents[1] / "config" / "research_taxonomy.json"


@lru_cache(maxsize=1)
def load_taxonomy() -> dict:
    return json.loads(TAXONOMY_PATH.read_text(encoding="utf-8"))


def public_directions() -> list[dict]:
    return [
        {"id": d["id"], "name": d["name"], "topics": [
            {key: t[key] for key in ("id", "name", "keywords")} for t in d["topics"]
        ]} for d in load_taxonomy()["directions"]
    ]


def classify_research(title: str, summary: str = "", abstract: str = "") -> dict:
    text = "\n".join((title or "", summary or "", abstract or ""))
    categories, topics = [], []
    # Core matches take precedence; extended reading never dilutes core tags.
    directions = sorted(load_taxonomy()["directions"], key=lambda d: bool(d.get("fallback_only")))
    for direction in directions:
        if direction.get("fallback_only") and categories:
            continue
        if direction["id"] == "training-free" and re.search(
            r"\bnot training[- ]free\b|\bwe (?:fine[- ]tune|train)\b|"
            r"(?:本文|本方法)(?:需要|采用).{0,12}(?:训练|微调)", text, re.I,
        ):
            continue
        if not all(re.search(pattern, text, re.I | re.S) for pattern in direction["all_of"]):
            continue
        # Extended reading is flat; relevance rules are not display subtopics.
        # Fail closed if no evidence rule matches, rather than catching all leftovers.
        if direction.get("fallback_only") and not any(
            re.search(pattern, text, re.I) for pattern in direction.get("any_of", [])
        ):
            continue
        matched_topics = [topic for topic in direction["topics"] if re.search(topic["pattern"], text, re.I)]
        categories.append(direction["name"])
        topics.extend({"id": t["id"], "name": t["name"], "category": direction["name"]} for t in matched_topics)
    return {
        "categories": categories,
        "topics": topics,
        "classification_status": "classified" if categories else "pending",
    }
