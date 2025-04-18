# Makefile for managing the Django HTMX Books project

# Environment-specific Docker Compose commands
DOCKER_COMPOSE_DEV = docker compose
DOCKER_COMPOSE_PROD = docker compose --env-file .env.prod -f docker-compose.prod.yml

# Development commands
up:  ## Start development environment with build
	$(DOCKER_COMPOSE_DEV) up -d --build

down:  ## Stop and remove development containers and volumes
	$(DOCKER_COMPOSE_DEV) down -v

migrate:  ## Apply database migrations
	$(DOCKER_COMPOSE_DEV) exec web python manage.py migrate --noinput

makemigrations:  ## Create new database migrations
	$(DOCKER_COMPOSE_DEV) exec web python manage.py makemigrations

createsuperuser:  ## Create a Django superuser
	$(DOCKER_COMPOSE_DEV) exec web python manage.py createsuperuser

check:  ## Run Django system checks
	$(DOCKER_COMPOSE_DEV) exec web python manage.py check

logs:  ## Show logs from development containers
	$(DOCKER_COMPOSE_DEV) logs

ps:  ## Show running development containers
	$(DOCKER_COMPOSE_DEV) ps

# Production commands
prod-up:  ## Start production environment with build
	$(DOCKER_COMPOSE_PROD) up -d --build

prod-down:  ## Stop and remove production containers and volumes
	$(DOCKER_COMPOSE_PROD) down -v

prod-migrate:  ## Apply migrations in production
	$(DOCKER_COMPOSE_PROD) exec web python manage.py migrate --noinput

prod-collectstatic:  ## Collect static files in production
	$(DOCKER_COMPOSE_PROD) exec web python manage.py collectstatic --noinput

prod-ps:  ## Show running production containers
	$(DOCKER_COMPOSE_PROD) ps

# Declare all targets as phony to avoid conflicts with files of the same name
.PHONY: up down migrate makemigrations createsuperuser check logs ps \
	prod-up prod-down prod-migrate prod-collectstatic prod-ps
