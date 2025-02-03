run-dev:
	ENVIRONMENT=development poetry run uvicorn app.main:app --reload

run-test:
	ENVIRONMENT=test poetry run pytest

docker-up:
	ENVIRONMENT=development docker-compose up -d

docker-down:
	docker-compose down
