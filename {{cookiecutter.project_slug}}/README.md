# {{ cookiecutter.project_name }} {{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.description }}

## Setup

**Lint**

```bash
flake8 .
```

**tests-coverage**

```bash
coverage run manage.py test -v 2 --keepdb
coverage report -m
coverage html
```
