# Projects Service

Project management service for Mosquera Soft.

## Requirements

- [uv](https://docs.astral.sh/uv/)

## Install dependencies

From this directory:

```bash
uv sync
```

## Run locally

```bash
uv run fastapi dev src/projects_service/main.py
```

The service will be available at:

- API: http://127.0.0.1:8000
- Documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

## Run tests

```bash
uv run pytest
```
