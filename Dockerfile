FROM python:3.13-slim

# Install uv (fast Python package manager used by this project)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files first so Docker can cache this layer
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# Copy the rest of the application
COPY . .

RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Render provides the $PORT env var at runtime; default to 8000 for local docker run
EXPOSE 8000
CMD uv run uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
