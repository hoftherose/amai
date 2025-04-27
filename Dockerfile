FROM python:3.13-bookworm

# Set venv outside of volume and set to path
WORKDIR /usr/src/app
ENV UV_PROJECT_ENVIRONMENT="../.venv"
ENV PATH="/usr/src/.venv/bin:/root/.local/bin/:$PATH"

# Install UV package manager
RUN apt update && apt install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

