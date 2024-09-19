CURRENT_DIRECTORY := $(shell pwd)
DOCKER_COMPOSE_FILE := $(CURRENT_DIRECTORY)/backend/docker/docker-compose-local.yml

build:
	docker-compose -f $(DOCKER_COMPOSE_FILE) build

start:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up

stop:
	docker-compose -f $(DOCKER_COMPOSE_FILE) stop

restart: stop start

tail:
	docker-compose -f $(DOCKER_COMPOSE_FILE) logs -f --tail=100

bash:
	docker exec -it api_backend /bin/bash

MODULE=server
test:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend pytest $(MODULE)

shell:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py shell

shell_plus:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py shell_plus

makemigrations:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py makemigrations

migrate:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py migrate

superuser:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py createsuperuser

makemessages:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py makemessages -a

compilemessages:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py compilemessages

load_data:
	docker-compose -f $(DOCKER_COMPOSE_FILE) run --rm presentations_backend python manage.py import_presentations /app/server/presentations/data/prezis.json
