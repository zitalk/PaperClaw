#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

from pipeline_config import load_config


CONFIG = load_config()


def _read_text(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"Missing filter asset file: {path}")
    return path.read_text(encoding="utf-8").strip()


def _read_json(path: Path) -> dict:
    if not path.exists():
        raise RuntimeError(f"Missing filter config file: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"Invalid filter config file: {path}")
    return data


def _load_string_list(data: dict, key: str, path: Path) -> list[str]:
    value = data.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(item, str) and item.strip() for item in value):
        raise RuntimeError(f"Invalid '{key}' in filter config: {path}")
    return [item.strip() for item in value]


@lru_cache(maxsize=1)
def load_filter_keywords() -> dict[str, list[str]]:
    data = _read_json(CONFIG.filter_keywords_path)
    return {
        "arxiv_categories": _load_string_list(data, "arxiv_categories", CONFIG.filter_keywords_path),
        "rs_query_terms": _load_string_list(data, "rs_query_terms", CONFIG.filter_keywords_path),
        "rs_signal_patterns": _load_string_list(data, "rs_signal_patterns", CONFIG.filter_keywords_path),
        "broad_signal_patterns": _load_string_list(data, "broad_signal_patterns", CONFIG.filter_keywords_path),
        "visual_context_patterns": _load_string_list(data, "visual_context_patterns", CONFIG.filter_keywords_path),
        "exclusion_patterns": _load_string_list(data, "exclusion_patterns", CONFIG.filter_keywords_path),
        "ai_signal_patterns": _load_string_list(data, "ai_signal_patterns", CONFIG.filter_keywords_path),
    }


@lru_cache(maxsize=1)
def load_filter_prompt_template() -> str:
    template = _read_text(CONFIG.filter_prompt_path)
    if "{{candidate_lines}}" not in template:
        raise RuntimeError(f"Filter prompt template must contain {{candidate_lines}}: {CONFIG.filter_prompt_path}")
    return template


@lru_cache(maxsize=1)
def load_rs_query_terms() -> list[str]:
    return load_filter_keywords()["rs_query_terms"]


@lru_cache(maxsize=1)
def load_arxiv_categories() -> list[str]:
    return load_filter_keywords()["arxiv_categories"]


@lru_cache(maxsize=1)
def load_rs_signal_patterns() -> list[re.Pattern[str]]:
    return [re.compile(pattern) for pattern in load_filter_keywords()["rs_signal_patterns"]]


@lru_cache(maxsize=1)
def load_broad_signal_patterns() -> list[re.Pattern[str]]:
    return [re.compile(pattern) for pattern in load_filter_keywords()["broad_signal_patterns"]]


@lru_cache(maxsize=1)
def load_visual_context_patterns() -> list[re.Pattern[str]]:
    return [re.compile(pattern) for pattern in load_filter_keywords()["visual_context_patterns"]]


@lru_cache(maxsize=1)
def load_exclusion_patterns() -> list[re.Pattern[str]]:
    return [re.compile(pattern) for pattern in load_filter_keywords()["exclusion_patterns"]]


@lru_cache(maxsize=1)
def load_ai_signal_patterns() -> list[re.Pattern[str]]:
    return [re.compile(pattern) for pattern in load_filter_keywords()["ai_signal_patterns"]]


def render_filter_prompt(candidate_lines: list[str]) -> str:
    template = load_filter_prompt_template()
    return template.replace("{{candidate_lines}}", "\n".join(candidate_lines))
