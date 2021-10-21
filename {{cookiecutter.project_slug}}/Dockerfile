# =============================================================================
# base
# =============================================================================
FROM python:{{ cookiecutter.python_version }} as base

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    --no-install-recommends libpq-dev &&  \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
COPY entrypoint.sh /usr/local/bin/
RUN poetry config virtualenvs.create false
# =============================================================================
# dev
# =============================================================================
FROM base as base_dev
RUN poetry install --no-root
COPY . /app/
# =============================================================================
# linter
# =============================================================================
FROM base_dev AS linter
RUN black --check --diff .
# =============================================================================
# development
# =============================================================================
FROM base_dev as development
ENV DEBUG true
ENV ALLOWED_HOSTS *
ENV ELASTIC_APM_ENABLED false
ENTRYPOINT ["entrypoint.sh"]
CMD ["dev"]
{% if cookiecutter.use_nameko == "y" -%}
# =============================================================================
# service
# =============================================================================
FROM base_dev as service
ENV DEBUG true
ENV ELASTIC_APM_ENABLED false
CMD ["nameko", "run", "--config", "config.yaml", "services"]
{%- endif %}
{% if cookiecutter.use_scheduler == "y" -%}
# =============================================================================
# Scheduler
# =============================================================================
FROM base_dev as scheduler
ENV DEBUG true
ENV ELASTIC_APM_ENABLED false
CMD ["python", "./config/scheduler.py"]
{%- endif %}
# =============================================================================
# release prod
# =============================================================================
FROM base as release
ENV DEBUG false
RUN poetry install --no-dev --no-root
COPY . /app/
ENTRYPOINT ["entrypoint.sh"]
CMD ["prd"]
