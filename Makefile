django_folder=cd musicstore;

clean:
	@find . -name "*.pyc" -delete

deps:
	@pip install -r requirements.txt

setup: clean deps
	@$(django_folder) python manage.py syncdb --noinput
	@$(django_folder) python manage.py migrate
	@$(django_folder) python manage.py createsuperuser --email="admin@cursorest.com"
	@make run

migrate: clean deps
	@$(django_folder) python manage.py syncdb
	@$(django_folder) python manage.py migrate

run: clean
	@$(django_folder) python manage.py runserver

flake8:
	@flake8 . --exclude='.*migrations' --ignore=E124,E128

remote_migrate:
	@heroku run python musicstore/manage.py syncdb --noinput
	@heroku run python musicstore/manage.py migrate

collectstatic:
	@heroku run python musicstore/manage.py collectstatic --noinput

heroku:
	@git push heroku master

deploy: heroku remote_migrate collectstatic

help:
	grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'
