.PHONY: run build

run:
	docker run --name netune-backend --rm --env-file .env vladislavkn/netune-backend

build:
	docker build -t vladislavkn/netune-backend .

push:
	docker push vladislavkn/netune-backend

dev:
	uvicorn main:app --host 0.0.0.0 --port 8080 --reload