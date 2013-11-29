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

help:
	grep '^[^#[:space:]].*:' Makefile | awk -F ":" '{print $$1}'