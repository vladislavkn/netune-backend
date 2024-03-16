.PHONY: run build

run:
	docker run --name netune-backend --rm -d -p 8080:80 --env-file .env netune-backend

build:
	docker build -t netune-backend .

dev:
	uvicorn main:app --host 0.0.0.0 --port 8080 --reload