"""Entrypoint - run the MCP server in stdio or HTTP mode."""

from __future__ import annotations

from . import config
from .server import mcp


def main() -> None:
    transport = config.MCP_TRANSPORT.lower().strip()

    if transport == "http":
        mcp.run(
            transport="streamable-http",
            host=config.MCP_HOST,
            port=config.MCP_PORT
        )
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
