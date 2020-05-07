#!/bin/sh
set -euo pipefail

poetry run python manage.py migrate

exec poetry run python manage.py runserver 0.0.0.0:8000