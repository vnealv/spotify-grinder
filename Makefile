build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti ng01 /bin/sh

shell-web:
	docker exec -ti dg01 /bin/sh

shell-db:
	docker exec -ti ps01 /bin/sh

log-nginx:
	docker-compose logs nginx

log-web:
	docker-compose logs web

log-db:
	docker-compose logs db

collectstatic:
	docker-compose -f docker-compose.yml exec web python manage.py collectstatic --noinput

prune:
	docker system prune

deploy:
	docker-compose -f docker-compose.yml exec web python manage.py check --deploy

makemigrations:
	docker-compose -f docker-compose.yml exec web python manage.py makemigrations

migrate:
	docker-compose -f docker-compose.yml exec web python manage.py migrate
