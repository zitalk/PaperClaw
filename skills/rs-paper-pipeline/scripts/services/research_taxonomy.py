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
    for direction in load_taxonomy()["directions"]:
        if direction["id"] == "training-free" and re.search(
            r"\bnot training[- ]free\b|\bwe (?:fine[- ]tune|train)\b|"
            r"(?:本文|本方法)(?:需要|采用).{0,12}(?:训练|微调)", text, re.I,
        ):
            continue
        if not all(re.search(pattern, text, re.I | re.S) for pattern in direction["all_of"]):
            continue
        categories.append(direction["name"])
        for topic in direction["topics"]:
            if re.search(topic["pattern"], text, re.I):
                topics.append({"id": topic["id"], "name": topic["name"], "category": direction["name"]})
    return {
        "categories": categories,
        "topics": topics,
        "classification_status": "classified" if categories else "pending",
    }
