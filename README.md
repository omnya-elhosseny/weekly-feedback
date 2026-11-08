# Weekly Team Feedback Tool

Minimal Django project scaffold. The health endpoint is available at `/health/`.

## Development

Install the project dependencies:

```sh
python3 -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` to customize local settings. Django reads that
file automatically; values set directly in the process environment take
precedence. The defaults work for local development with SQLite, and are not
intended for production.

Configuration variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Local-only insecure key | Django signing key. Set a unique secret outside local development. |
| `DJANGO_DEBUG` | `true` | Enables Django debug mode when set to `true`, `1`, `yes`, or `on`. |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1,testserver` | Comma-separated hostnames accepted by Django. |
| `DB_ENGINE` | `django.db.backends.sqlite3` | Django database backend. |
| `DB_NAME` | `db.sqlite3` in the project directory | Database name or SQLite file path. |
| `DB_USER` | Empty | Database username. |
| `DB_PASSWORD` | Empty | Database password. |
| `DB_HOST` | Empty | Database host. |
| `DB_PORT` | Empty | Database port. |

Run the health check test and start the development server with:

```sh
python3 manage.py test
python3 manage.py runserver
```
