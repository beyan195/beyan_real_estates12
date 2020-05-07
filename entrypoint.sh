#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn -w 4 beyan_real_estates.wsgi:application --bind 0.0.0.0:8000
