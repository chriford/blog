
migrate:
	@python manage.py migrate

migrations:
	@python manage.py makemigrations

collectstatic:
	@python manage.py collectstatic --no-input

superuser:
	@python manage.py createsuperuser

run:
	@python manage.py runserver 8000

django-shell:
	@python manage.py shell

build:
	@docker-compose build

start:
	@docker-compose up -d

start-live:
	@docker-compose up

stop:
	@docker-compose down

kill:
	@docker-compose down -v