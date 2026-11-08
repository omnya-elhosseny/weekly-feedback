# Weekly Team Feedback Tool

Minimal Django project scaffold. The health endpoint is available at `/health/`.

## Development

Install the project dependencies:

```sh
python3 -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` to configure local PostgreSQL. Django reads that
file automatically; values set directly in the process environment take
precedence. The values in `.env.example` are placeholders for local use, not
production credentials. Without a `.env` file, Django uses SQLite.

Configuration variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Local-only insecure key | Django signing key. Set a unique secret outside local development. |
| `DJANGO_DEBUG` | `true` | Enables Django debug mode when set to `true`, `1`, `yes`, or `on`. |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,testserver` | Comma-separated hostnames accepted by Django. |
| `DB_ENGINE` | `django.db.backends.sqlite3` | Django database backend. Use `django.db.backends.postgresql` with Compose. |
| `DB_NAME` | `db.sqlite3` in the project directory | Database name or SQLite file path. Compose uses `weekly_feedback` if unset. |
| `DB_USER` | Empty | PostgreSQL username; required by Compose. |
| `DB_PASSWORD` | Empty | PostgreSQL password; required by Compose. |
| `DB_HOST` | Empty | Database host; use `localhost` from the host machine. |
| `DB_PORT` | Empty | Database port; Compose publishes port `5433` by default. |

### PostgreSQL with Docker Compose

Install dependencies, copy the example settings, then replace the database
password placeholder with a local value:

```sh
python3 -m pip install -r requirements.txt
cp .env.example .env
```

Start PostgreSQL and wait until its health check reports `healthy`:

```sh
docker compose up -d db
docker compose ps
```

The database data is stored in the named `postgres_data` volume. Run Django
migrations and start the web server from the host:

```sh
python3 manage.py migrate
python3 manage.py runserver
```

Run Django tests with its isolated test database (for PostgreSQL this is a
separate `test_` database created for the test run):

```sh
python3 manage.py test
```

Stop the database while preserving its data with:

```sh
docker compose down
```

Use `docker compose down -v` only when you intend to delete the local database
volume and all its data. For quick scaffold work without Docker, leave `.env`
absent to use SQLite.

Run the health check test and start the development server with:

```sh
python3 manage.py test
python3 manage.py runserver
```
