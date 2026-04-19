# Grok Search MCP

An MCP server that provides a `web_search` tool powered by the [Grok (xAI)](https://docs.x.ai/) API. It uses the official `xai_sdk` Python package to perform real-time web searches and optionally search X (Twitter) posts.

## Features

- **Web Search** — real-time internet search via Grok with citations
- **X Search** — optionally include X / Twitter results (toggle via environment variable)
- **Dual Transport** — runs as a local stdio MCP server *or* a remote Streamable HTTP server
- **Docker Ready** — ships with Dockerfile and docker-compose for one-command deployment

## Prerequisites

- Python 3.11+
- An [xAI API key](https://console.x.ai/team/default/api-keys)

## Configuration

All settings are read from environment variables. Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

| Variable | Required | Default | Description |
|---|---|---|---|
| `XAI_API_KEY` | **Yes** | — | Your xAI API key |
| `XAI_MODEL` | No | `grok-3-mini` | Model name to use for search |
| `XAI_ENABLE_X_SEARCH` | No | `false` | Set to `true` to also search X / Twitter |
| `MCP_TRANSPORT` | No | `stdio` | `stdio` for local use, `http` for network/Docker |
| `MCP_HOST` | No | `0.0.0.0` | Bind address for HTTP mode |
| `MCP_PORT` | No | `8000` | Port for HTTP mode |
| `MCP_PATH` | No | `/mcp` | HTTP endpoint path |

## Local Usage

### Install

```bash
pip install -e .
```

### Run (stdio mode — for Claude Desktop, VS Code, etc.)

```bash
grok-search-mcp
```

Or explicitly:

```bash
MCP_TRANSPORT=stdio grok-search-mcp
```

### Run (HTTP mode — for remote MCP clients)

```bash
MCP_TRANSPORT=http grok-search-mcp
```

The server will listen on `http://0.0.0.0:8000/mcp` by default.

## MCP Client Configuration

### Claude Desktop (stdio)

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "grok-search": {
      "command": "grok-search-mcp",
      "env": {
        "XAI_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### VS Code (stdio)

Add to your `.vscode/mcp.json`:

```json
{
  "servers": {
    "grok-search": {
      "command": "grok-search-mcp",
      "env": {
        "XAI_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### Remote MCP Client (HTTP)

Connect to the Streamable HTTP endpoint:

```
http://<host>:8000/mcp
```

## Docker

### Build and run

```bash
docker build -t grok-search-mcp .
docker run --env-file .env -p 8000:8000 grok-search-mcp
```

### Using docker-compose

```bash
docker compose up
```

The container starts in HTTP mode by default and exposes port `8000`. The MCP endpoint is available at `http://localhost:8000/mcp`.

## Project Structure

```
├── src/grok_search_mcp/
│   ├── __init__.py        # Package marker
│   ├── config.py          # Environment variable parsing
│   ├── xai_service.py     # xai_sdk integration
│   ├── server.py          # FastMCP server & tool definition
│   └── main.py            # Entrypoint (stdio / HTTP switch)
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── pyproject.toml
└── README.md
```

## License

MIT
