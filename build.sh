
#!/usr/bin/env bash
set -o errexit

uv sync --locked --no-dev
uv run --locked python manage.py collectstatic --no-input --settings=config.production
