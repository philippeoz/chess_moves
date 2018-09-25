#!/bin/sh
python manage.py migrate && \
python manage.py collectstatic --noinput && \
gunicorn backend.wsgi:application -b 0.0.0.0:8000 --workers 3 --log-level=info