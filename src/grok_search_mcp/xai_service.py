"""Thin wrapper around xai_sdk for web/X search."""

from __future__ import annotations

from xai_sdk import Client
from xai_sdk.chat import user
from xai_sdk.tools import web_search, x_search

from . import config


def search(query: str) -> str:
    """Send *query* to Grok with web_search (and optionally x_search) enabled.

    Returns a formatted string containing the assistant's answer followed by
    any citations extracted from the response.
    """
    if not config.XAI_API_KEY:
        raise RuntimeError(
            "XAI_API_KEY is not set. "
            "Please set the XAI_API_KEY environment variable."
        )

    client = Client(
        api_key=config.XAI_API_KEY,
    )

    tools: list = [web_search()]
    if config.XAI_ENABLE_X_SEARCH:
        tools.append(x_search())

    chat = client.chat.create(
        model=config.XAI_MODEL,
        tools=tools,
    )

    chat.append(user(query))
    response = chat.sample()

    # Build result text
    parts: list[str] = []
    if response.content:
        parts.append(response.content)

    # Append citations if available
    citations = getattr(response, "citations", None)
    if citations:
        parts.append("\n\nCitations:")
        if isinstance(citations, list):
            for citation in citations:
                parts.append(f"  - {citation}")
        else:
            parts.append(f"  {citations}")

    return "\n".join(parts) if parts else "(No results returned)"
