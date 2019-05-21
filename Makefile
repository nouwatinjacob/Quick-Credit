PYTHON_MANAGE := python3 manage.py 

migrations:
	$(PYTHON_MANAGE) makemigrations

migrate:
	$(PYTHON_MANAGE) migrate

install:
	pip install -r requirements.txt

runserver:
	$(PYTHON_MANAGE) runserver

test:
	$(PYTHON_MANAGE) test
	coverage report
	coverage html