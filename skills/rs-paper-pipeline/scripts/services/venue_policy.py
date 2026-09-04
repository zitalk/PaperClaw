"""Deterministic publication admission; never infer quality from abstract text."""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

POLICY_PATH = Path(__file__).resolve().parents[1] / "config" / "venue_policy.json"
ARXIV_ID = re.compile(r"(?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?", re.I)
NON_MAIN = re.compile(r"\b(?:workshops?|demos?|demonstrations?|tutorials?|companion|abstracts?)\b", re.I)


@lru_cache(maxsize=1)
def load_policy() -> dict:
    return json.loads(POLICY_PATH.read_text(encoding="utf-8"))


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", str(value or "")).casefold().replace("&", " and ")
    return re.sub(r"[\W_]+", " ", value).strip()


def _matches(venue: str, entry: dict) -> bool:
    key = normalize(venue)
    aliases = [entry["name"], entry.get("abbr", ""), *entry.get("aliases", [])]
    if entry.get("kind") == "conference":
        if NON_MAIN.search(venue):
            return False
        key = re.sub(r"\b(?:19|20)\d{2}\b|\b\d+(?:st|nd|rd|th)\b", "", key)
        key = re.sub(r"^proceedings (?:of )?(?:the )?", "", key.strip())
        key = re.sub(r"\s+", " ", key).strip()
        # Common metadata spelling: full conference name followed by (ACRONYM).
        abbrev = normalize(entry.get("abbr", ""))
        if abbrev and key.endswith(" " + abbrev):
            key = key[:-(len(abbrev) + 1)].strip()
    return any(key == normalize(alias) for alias in aliases if alias)


def _dois(candidate: dict) -> list[str]:
    values = [candidate.get("doi"), candidate.get("paper_id"), candidate.get("arxiv_id"), candidate.get("url")]
    return [re.sub(r"^(?:doi:|https?://(?:dx\.)?doi\.org/)", "", str(v).strip().lower()) for v in values if v]


def allowed_venue(venue: str, dois: list[str] | None = None) -> dict | None:
    for entry in load_policy()["allow"]:
        if _matches(venue, entry) or any(
            doi.startswith(prefix) for doi in (dois or []) for prefix in entry.get("doi_prefixes", [])
        ):
            return entry
    return None


def venue_decision(candidate: dict) -> tuple[bool, str]:
    # arXiv always bypasses the venue gate, including merged published versions.
    # Database provider names or the word 'arXiv' in a title are not proof.
    if any(ARXIV_ID.fullmatch(str(candidate.get(k) or "")) for k in ("arxiv_id", "paper_id")):
        return True, "arxiv_exempt"
    url = str(candidate.get("url") or "")
    match = re.fullmatch(r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf)/(.+?)(?:\.pdf)?", url, re.I)
    if match and ARXIV_ID.fullmatch(match.group(1)):
        return True, "arxiv_exempt"
    venues = [candidate.get("venue", ""), *(candidate.get("venues") or [])]
    if any(NON_MAIN.search(v) for v in venues if v):
        return False, "non_main_publication"
    for venue in venues:
        entry = allowed_venue(venue, _dois(candidate))
        if entry:
            return True, f"allowlist: {entry['abbr']}"
    return False, "venue_not_allowlisted" if any(venues) else "venue_unknown"


def filter_venues(candidates: list[dict]) -> tuple[list[dict], list[dict]]:
    admitted, excluded = [], []
    for candidate in candidates:
        allowed, reason = venue_decision(candidate)
        if allowed:
            admitted.append(candidate)
        else:
            excluded.append({**candidate, "venue_policy_reason": reason})
    return admitted, excluded
