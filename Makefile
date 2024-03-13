.PHONY: run build

run:
	docker run --name netune-backend --rm -d -p 8080:80 netune-backend

build:
	docker build -t netune-backend .
