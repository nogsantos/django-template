#!/bin/sh

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
gunicorn --bind 0.0.0.0:{{ cookiecutter.server_port }} --workers 1 --log-level INFO {{ cookiecutter.project_slug }}.wsgi:application
