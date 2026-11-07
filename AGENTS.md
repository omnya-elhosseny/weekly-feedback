# Repository Guidelines

## Project Structure

The repository contains product documentation in `_docs/`: `plan.md` is the MVP specification, `architecture.md` describes the intended design, and `tasks.md` is the implementation backlog. The initial Django scaffold lives in `config/`, with the basic health endpoint and test in `health/`. The planned stack is Django with server-rendered templates, PostgreSQL, and Celery/Celery Beat for scheduled weekly cycle changes. Keep future Django apps, templates, static assets, and tests in clearly named project directories.

## Build, Test, and Development

Install dependencies with `python3 -m pip install -r requirements.txt`. Run the Django test suite with `python3 manage.py test` and start the local development server with `python3 manage.py runserver`. SQLite is used as a local scaffold default; PostgreSQL configuration, database, and worker commands will be documented when those tasks are implemented. Do not claim a command passes unless you have run it.

## Style and Naming

Use Python’s standard four-space indentation and Django conventions: `snake_case` for functions and variables, `PascalCase` for classes, and descriptive app and template names. Keep views focused, use Django forms for input validation, and enforce access rules on the server. Build pages with Django templates, HTML, and plain CSS; do not add a frontend framework without updating the product direction. Follow existing formatting and linting configuration when one is introduced rather than adding tools ad hoc.

## Testing

Use Django’s test runner and name test modules `test_*.py`; use descriptive `test_*` methods. Cover both permitted and denied access, especially feedback privacy before retrospectives, submit-before-view behavior, author-only edits, scheduled closure, and admin-only history. Run relevant tests for each change and the full suite before proposing a release.

## Commits and Pull Requests

The available history uses short imperative commit subjects (for example, `Add weekly feedback product plan`). Keep commits focused and use the same style. Pull requests should summarize the behavior changed, link related issues, include test results, and provide screenshots for visible UI changes. Call out configuration or migration steps.

## Work Process

Track tasks as GitHub issues and work on one issue at a time. Commit regularly as work progresses.

## Security and Configuration

Keep secrets and real credentials out of Git; use environment configuration and placeholder-only examples. Preserve the one-team role model and verify authorization in backend code, not only in templates. Treat feedback and participation status as private until the configured retrospective begins.
