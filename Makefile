.ONESHELL:

.PHONY: clean install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	virtualenv venv; \
	. env/bin/activate; \
	pip install -r requirements.txt;

tests:
	. env/bin/activate; \
	python manage.py test

run:
	. env/bin/activate; \
	python manage.py run

all: clean install tests run
