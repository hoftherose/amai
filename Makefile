install:
	uv sync

run-dev:
	uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

run:
	uv run uvicorn src.main:app --port 8000

docker_up:
	docker compose up -d

