FROM python:3.12.4-alpine3.19

RUN pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY src ./src
COPY main.py .
COPY alembic ./alembic
COPY alembic.ini .

RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "-m", "main"]