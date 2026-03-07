FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project

COPY . .

RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"

CMD ["pytest"]