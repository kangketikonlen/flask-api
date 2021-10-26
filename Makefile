.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -prune -exec rm -rf {} \;
	find . -type f -name '*.log' -prune -exec rm -rf {} \;
	find . -type f -name '*.db' -prune -exec rm -rf {} \;
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;
	find . -type d -name "env" -prune -exec rm -rf {} \;
	find . -type d -name "migrations" -prune -exec rm -rf {} \;

install:
	virtualenv env; \
	. env/bin/activate; \
	python -m pip install --upgrade pip
	pip install -r requirements.txt;

migration:
	. env/bin/activate; \
	python manage.py db init; \
	python manage.py db migrate --message 'initial database migration'; \
	python manage.py db upgrade;

tests:
	. env/bin/activate; \
	python manage.py test

run:
	. env/bin/activate; \
	python manage.py run

all: clean install migration tests run
