.PHONY: run fmt lint build push

DOCKER_IMAGE_VERSION=0.1

run:
	FLASK_ENV=development flask run

fmt:
	black .
	isort .

lint:
	flake8

build:
	docker build -t docker.io/myimage:$(DOCKER_IMAGE_VERSION) .

push:
	docker push docker.io/myimage:$(DOCKER_IMAGE_VERSION) .
