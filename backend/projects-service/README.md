# Projects Service

Project management service for Mosquera Soft.

## Requirements

- [uv](https://docs.astral.sh/uv/)

## Install dependencies

From this directory:

```bash
uv sync
```

## Configure the database

Create the local environment file and replace the placeholder password:

```bash
cp .env.example .env
```

The local PostgreSQL service is available at `localhost:5433`.

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

## Database migrations

Create a migration after changing SQLModel table models:

```bash
uv run alembic revision --autogenerate -m "describe the schema change"
```

Review the generated migration before applying it:

```bash
uv run alembic upgrade head
```

Inspect the currently applied revision:

```bash
uv run alembic current
```
