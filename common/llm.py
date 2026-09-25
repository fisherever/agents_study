"""Shared LLM entry point for agents_study concepts."""

from __future__ import annotations

import os

import anthropic
from anthropic.types import Message
from dotenv import load_dotenv

# Load .env once when this module is imported.
# 只在 common 层 load 一次；concept 脚本里不要再 load_dotenv()
load_dotenv()

_client: anthropic.Anthropic | None = None


def _require_env(name: str) -> str:
    """Return an environment variable or raise with a clear message."""
    value = os.environ.get(name)
    if not value:
        raise KeyError(
            f"Missing environment variable {name!r}. "
            "Add it to .env in the repo root or export it in your shell."
        )
    return value


def get_model() -> str:
    """Default model id from ``LLM_MODEL``."""
    return _require_env("LLM_MODEL")


def get_client() -> anthropic.Anthropic:
    """Lazy singleton ``Anthropic`` client from ``LLM_BASE_URL`` / ``LLM_API_KEY``."""
    global _client
    if _client is None:
        _client = anthropic.Anthropic(
            base_url=_require_env("LLM_BASE_URL"),
            api_key=_require_env("LLM_API_KEY"),
        )
    return _client


def chat(
    messages: list[dict],
    system: str | None = None,
    model: str = ...,
) -> Message:
    """Call the Messages API and return the full ``Message`` response.

    ``base_url``, ``api_key``, and the default ``model`` come from environment
    variables ``LLM_BASE_URL``, ``LLM_API_KEY``, and ``LLM_MODEL`` — never
    hard-code them here.
    """
    if model is ...:
        model = get_model()

    client = get_client()

    # --- TODO: implement (see docs/d2-common-llm-skeleton.md in Agent Store) ---
    #
    # Step 1: Build kwargs for client.messages.create:
    #         model=model, messages=messages, max_tokens=256 (match c01 for now)
    # Step 2: If system is not None, add system=system to kwargs
    #         （system 是单独参数，不要误当成一条 user message，除非你在刻意模拟旧写法）
    # Step 3: response = client.messages.create(**kwargs)
    # Step 4: return response   # 类型是 Message，不要只 return response.content
    #
    # 常见坑 / gotchas:
    # - Wrong SDK (OpenAI chat.completions) — this course uses anthropic.messages.create
    # - Creating a new Anthropic() inside chat() — reuse get_client()
    # - Reading LLM_* in c01 — keep env access in this module only

    raise NotImplementedError("Fill in chat() using the TODO steps above.")
