CURRENT_DIRECTORY := $(shell pwd)
DOCKER_COMPOSE_FILE_BE := $(CURRENT_DIRECTORY)/backend/docker/docker-compose-local.yml
DOCKER_COMPOSE_FILE_FE := $(CURRENT_DIRECTORY)/frontend/docker-compose.yml

build_backend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) build

build_frontend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_FE) build

start_backend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) up

start_frontend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_FE) up

stop_backend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) stop

stop_frontend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_FE) stop

restart_backend: stop_backend start_backend
restart_frontend: stop_frontend start_frontend

tail:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) logs -f --tail=100

bash:
	docker exec -it api_backend /bin/bash

MODULE=server
test_backend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend pytest $(MODULE)

test_frontend:
	docker-compose -f $(DOCKER_COMPOSE_FILE_FE) run --rm frontend npm run test

shell:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py shell

shell_plus:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py shell_plus

makemigrations:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py makemigrations

migrate:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py migrate

superuser:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py createsuperuser

makemessages:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py makemessages -a

compilemessages:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py compilemessages

load_data:
	docker-compose -f $(DOCKER_COMPOSE_FILE_BE) run --rm presentations_backend python manage.py import_presentations /app/server/presentations/data/prezis.json
