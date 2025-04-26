FROM python:3.13-bookworm

RUN apt update && apt install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

COPY pyproject.toml .
COPY uv.lock .

COPY . .
CMD ["uv", "run", "python", "src/main.py"]

