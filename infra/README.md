# Infrastructure

Shared infrastructure configuration lives here.

## Local PostgreSQL

Create the local environment file and replace the placeholder password:

```bash
cp infra/.env.example infra/.env
```

Start the projects database from the repository root:

```bash
docker compose -f infra/compose.yaml up -d projects-db
```

Check its status:

```bash
docker compose -f infra/compose.yaml ps
```

Stop the local infrastructure without deleting its data:

```bash
docker compose -f infra/compose.yaml down
```

PostgreSQL is exposed only on `127.0.0.1:5433`. Its data persists in the
Docker-managed `projects-db-data` volume.
