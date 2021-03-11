COMPOSE_EXEC_PYTHON=docker-compose exec web python manage.py

install: start
	make migrate
	make-create-super-user

start:
	docker-compose up -d
	docker-compose start
	docker-compose ps

generate-migrations:
	${COMPOSE_EXEC_PYTHON} makemigrations

migrate:
	${COMPOSE_EXEC_PYTHON} migrate

create-super-user:
	${COMPOSE_EXEC_PYTHON} createsuperuser --noinput