FROM node:24-slim AS web_builder
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME/bin:$PATH"
RUN corepack enable
COPY ./web /web
WORKDIR /web
ENV ASTRO_TELEMETRY_DISABLED=1
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install  --yes --frozen-lockfile
RUN pnpm  build

FROM python:3.14-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY ./api /api
COPY --from=web_builder /web/dist /web/dist

# Install the application dependencies.
WORKDIR /api
RUN uv sync --frozen --no-cache --no-group dev

# Run the application.
CMD ["/api/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]