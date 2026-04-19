"""Configuration loaded from environment variables."""

from __future__ import annotations

import os


def _parse_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in ("1", "true", "yes")


# --- xAI settings ---
XAI_API_KEY: str = os.environ.get("XAI_API_KEY", "")
XAI_MODEL: str = os.environ.get("XAI_MODEL", "grok-3-mini")
XAI_ENABLE_X_SEARCH: bool = _parse_bool(os.environ.get("XAI_ENABLE_X_SEARCH"))

# --- MCP transport settings ---
MCP_TRANSPORT: str = os.environ.get("MCP_TRANSPORT", "stdio")  # "stdio" | "http"
MCP_HOST: str = os.environ.get("MCP_HOST", "0.0.0.0")
MCP_PORT: int = int(os.environ.get("MCP_PORT", "8000"))
MCP_PATH: str = os.environ.get("MCP_PATH", "/mcp")
