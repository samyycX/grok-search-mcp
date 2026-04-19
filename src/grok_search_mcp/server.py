"""MCP server definition with a single web_search tool."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from .xai_service import search

mcp = FastMCP("grok-search-mcp")


@mcp.tool()
def web_search(query: str) -> str:
    """Search the web using Grok (xAI).

    Performs a real-time web search (and optionally an X / Twitter search)
    through the Grok API and returns the answer together with citations.

    Args:
        query: The search query string.
    """
    try:
        return search(query)
    except RuntimeError as exc:
        return f"Configuration error: {exc}"
    except Exception as exc:
        return f"Search failed: {exc}"
