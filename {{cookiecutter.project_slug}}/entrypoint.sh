#!/bin/sh

ENV=${ENV:-dev}

echo "Apply database migrations"
python manage.py migrate

if [ "$ENV" = "$1" ]; then
  echo "Development environment ENV is $ENV"
  python manage.py collectstatic --noinput
  python manage.py runserver_plus 0.0.0.0:{{ cookiecutter.server_port }}
else
  echo "Productions environment ENV is prod"
  SECRET_KEY=$(python contrib/secret_gen.py)
  export SECRET_KEY
  gunicorn --bind 0.0.0.0:{{ cookiecutter.server_port }} --workers 1 --log-level INFO {{ cookiecutter.project_slug }}.wsgi:application
fi
