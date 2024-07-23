# Отдельный "сборочный" образ
FROM python:3.11-slim-bullseye as compile-image
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir poetry \
 && poetry config virtualenvs.in-project true \
 && poetry install --no-interaction --no-ansi


# Образ, который будет непосредственно превращаться в контейнер
FROM python:3.11-slim-bullseye as run-image
COPY --from=compile-image /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
WORKDIR /app
COPY . /app/
CMD ["python", "-m", "bot"]