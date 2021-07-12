# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

{% if cookiecutter.open_source_license != "Not open source" %}

License {{cookiecutter.open_source_license}}
{% endif %}

## Setup

Requirement, [Poetry](https://python-poetry.org/docs/#installation) for dependency management

For development environment:

```console
poetry install
poetry shell
./manage.py migrate
./start-dev.sh
```

> In container, is required generate the poetry.lock before the build.

Access

http://127.0.0.1:8000

### Tools

**Lint with virtual env enabled**

```console
black .
flake8 .
```

**tests-coverage with virtual env enabld**

```console
coverage run manage.py test -v 2 --noinput --failfast --parallel
coverage report -m
coverage html
```

{% if cookiecutter.use_heroku == "y" -%}
## Publish

To publis on heroku [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

1. Create an instance
2. Send configurations to Heroku
3. Defines a secret key to instance
4. Set DEBUG=False
5. Configure email send service
6. Send the code

```console
heroku create my-new-instance
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBU=False
# email configurations
git push heroku master --force
```
{%- endif %}