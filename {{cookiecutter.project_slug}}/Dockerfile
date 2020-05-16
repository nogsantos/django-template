{% if cookiecutter.alpine_image == "y" -%}
FROM python:{{ cookiecutter.python_version }}-alpine
{% elif cookiecutter.alpine_image == "n" -%}
FROM python:{{ cookiecutter.python_version }}
{%- endif %}

ENV PYTHONUNBUFFERED 1

{% if cookiecutter.alpine_image == "y" -%}
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev bash make
{% elif cookiecutter.alpine_image == "n" -%}
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev &&  \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb
{%- endif %}

RUN pip install --upgrade pip
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN mkdir /code
WORKDIR /code

COPY pyproject.toml /code/
COPY poetry.lock /code/

RUN poetry install

ADD . /code/
