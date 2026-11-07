# Repository Guidelines

## Project Structure

This repository currently contains product documentation: `_docs/plan.md` is the MVP specification, and `_docs/tasks.md` is the implementation backlog. Application code does not exist yet. The planned stack is Django with server-rendered templates, PostgreSQL, and Celery/Celery Beat for scheduled weekly cycle changes. Keep future Django apps, templates, static assets, and tests in clearly named project directories; update this guide when the structure is established.

## Build, Test, and Development

The initial project setup is tracked in GitHub issue #1. Once it is implemented, use the documented project commands; the expected Django test command is `python manage.py test`, and the local development server is `python manage.py runserver`. Add dependency installation, database, and worker commands here when the project scaffold defines them. Do not claim a command passes unless you have run it.

## Style and Naming

Use Python’s standard four-space indentation and Django conventions: `snake_case` for functions and variables, `PascalCase` for classes, and descriptive app and template names. Keep views focused, use Django forms for input validation, and enforce access rules on the server. Build pages with Django templates, HTML, and plain CSS; do not add a frontend framework without updating the product direction. Follow existing formatting and linting configuration when one is introduced rather than adding tools ad hoc.

## Testing

Use Django’s test runner and name test modules `test_*.py`; use descriptive `test_*` methods. Cover both permitted and denied access, especially feedback privacy before retrospectives, submit-before-view behavior, author-only edits, scheduled closure, and admin-only history. Run relevant tests for each change and the full suite before proposing a release.

## Commits and Pull Requests

The available history uses short imperative commit subjects (for example, `Add weekly feedback product plan`). Keep commits focused and use the same style. Pull requests should summarize the behavior changed, link related issues, include test results, and provide screenshots for visible UI changes. Call out configuration or migration steps.

## Security and Configuration

Keep secrets and real credentials out of Git; use environment configuration and placeholder-only examples. Preserve the one-team role model and verify authorization in backend code, not only in templates. Treat feedback and participation status as private until the configured retrospective begins.
