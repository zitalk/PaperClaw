#!/usr/bin/env python3
"""Shared runtime configuration for the personal PaperClaw pipeline."""

from __future__ import annotations

import os
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"
PROMPTS_DIR = SCRIPTS_DIR / "prompts"
DEFAULT_ENV_FILES = (ROOT_DIR / ".env", SCRIPTS_DIR / ".env")


def _load_env_files() -> None:
    for path in DEFAULT_ENV_FILES:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


_load_env_files()


def _env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None or value == "":
        return default
    return value


def _env_bool(name: str, default: bool = False) -> bool:
    value = _env(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def require_env(name: str) -> str:
    value = _env(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def resolve_workspace_root() -> tuple[Path, str | None]:
    configured = _env("RS_WORKSPACE")
    if not configured:
        return ROOT_DIR, None

    candidate = Path(configured).expanduser().resolve()
    if candidate.exists() and (candidate / "scripts").exists():
        return candidate, None

    reason = f"RS_WORKSPACE={configured} is unavailable, fallback to {ROOT_DIR}"
    return ROOT_DIR, reason


def build_runtime_env(extra: dict[str, str] | None = None) -> dict[str, str]:
    env = os.environ.copy()
    proxy_url = _env("RS_PROXY_URL")
    if proxy_url:
        env.setdefault("http_proxy", proxy_url)
        env.setdefault("https_proxy", proxy_url)

    openclaw_bin = _env("OPENCLAW_BIN")
    if openclaw_bin:
        bin_dir = str(Path(openclaw_bin).expanduser().resolve().parent)
        current_path = env.get("PATH", "")
        if bin_dir not in current_path.split(":"):
            env["PATH"] = f"{current_path}:{bin_dir}" if current_path else bin_dir

    if extra:
        env.update(extra)
    return env


def get_proxy_map() -> dict[str, str]:
    env = build_runtime_env()
    proxy_map: dict[str, str] = {}
    if env.get("http_proxy"):
        proxy_map["http"] = env["http_proxy"]
    if env.get("https_proxy"):
        proxy_map["https"] = env["https_proxy"]
    return proxy_map


def install_urllib_proxy() -> None:
    proxy_map = get_proxy_map()
    if proxy_map:
        urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler(proxy_map)))


def _resolve_root_relative_path(value: str, root_dir: Path) -> Path:
    path = Path(value).expanduser()
    return path if path.is_absolute() else (root_dir / path).resolve()


@dataclass(frozen=True)
class PipelineConfig:
    root_dir: Path
    scripts_dir: Path
    prompts_dir: Path
    memory_dir: Path
    pipeline_state_dir: Path
    papers_dir: Path
    figures_dir: Path
    temp_dir: Path
    keep_downloads: bool
    github_repo: str
    github_token: str | None
    github_timeout: int
    github_retry: int
    llm_api_url: str
    llm_api_key: str | None
    llm_model: str
    openclaw_bin: str | None
    feishu_target: str | None
    dingtalk_webhook: str | None
    raw_content_base: str
    arxiv_api: str
    arxiv_user_agent: str
    openalex_api_key: str | None
    semantic_scholar_api_key: str | None
    ieee_api_key: str | None
    elsevier_api_key: str | None
    springer_nature_api_key: str | None
    multisource_enabled: bool
    filter_keywords_path: Path
    filter_prompt_path: Path
    workspace_warning: str | None


def load_config() -> PipelineConfig:
    github_repo = _env("RS_GITHUB_REPO", "zitalk/PaperClaw")
    root_dir, workspace_warning = resolve_workspace_root()
    temp_dir = _resolve_root_relative_path(_env("RS_TEMP_DIR", "tmp"), root_dir)
    return PipelineConfig(
        root_dir=root_dir,
        scripts_dir=root_dir / "scripts",
        prompts_dir=root_dir / "scripts" / "prompts",
        memory_dir=root_dir / "memory",
        pipeline_state_dir=root_dir / "memory" / "pipeline_state",
        papers_dir=root_dir / "papers",
        figures_dir=root_dir / "papers" / "figures",
        temp_dir=temp_dir,
        keep_downloads=_env_bool("RS_KEEP_DOWNLOADS", False),
        github_repo=github_repo,
        github_token=_env("GITHUB_TOKEN"),
        github_timeout=int(_env("GITHUB_TIMEOUT", "15")),
        github_retry=int(_env("GITHUB_RETRY", "2")),
        llm_api_url=_env("LLM_API_URL", "https://api.deepseek.com/chat/completions"),
        llm_api_key=_env("LLM_API_KEY"),
        llm_model=_env("LLM_MODEL", "deepseek-v4-flash"),
        openclaw_bin=_env("OPENCLAW_BIN"),
        feishu_target=_env("FEISHU_TARGET"),
        dingtalk_webhook=_env("DINGTALK_WEBHOOK"),
        raw_content_base=f"https://raw.githubusercontent.com/{github_repo}/main",
        arxiv_api=_env("ARXIV_API_URL", "https://export.arxiv.org/api/query"),
        arxiv_user_agent=_env("ARXIV_USER_AGENT", f"PaperClaw/1.0 (+https://github.com/{github_repo})"),
        openalex_api_key=_env("OPENALEX_API_KEY"),
        semantic_scholar_api_key=_env("SEMANTIC_SCHOLAR_API_KEY"),
        ieee_api_key=_env("IEEE_API_KEY"),
        elsevier_api_key=_env("ELSEVIER_API_KEY"),
        springer_nature_api_key=_env("SPRINGER_NATURE_API_KEY"),
        multisource_enabled=_env_bool("RS_MULTISOURCE_ENABLED", True),
        filter_keywords_path=_resolve_root_relative_path(
            _env("RS_FILTER_KEYWORDS_FILE", "scripts/config/filter_keywords.json"),
            root_dir,
        ),
        filter_prompt_path=_resolve_root_relative_path(
            _env("RS_FILTER_PROMPT_FILE", "scripts/prompts/filter_cross_prompt.md"),
            root_dir,
        ),
        workspace_warning=workspace_warning,
    )


def get_github_client(config: PipelineConfig | None = None) -> Any:
    cfg = config or load_config()
    if not cfg.github_token:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    try:
        from github import Auth, Github
    except ModuleNotFoundError as exc:
        raise RuntimeError("Missing Python dependency: PyGithub") from exc
    return Github(auth=Auth.Token(cfg.github_token), timeout=cfg.github_timeout, retry=cfg.github_retry)


def get_repo(config: PipelineConfig | None = None):
    cfg = config or load_config()
    return get_github_client(cfg).get_repo(cfg.github_repo)
