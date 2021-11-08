setup:
	# Create python virtualenv & source it
	# source ~/.devops/bin/activate
	python3 -m venv ~/.devops

install:
	# This should be run from inside a virtualenv
	pip install --no-cache-dir --upgrade pip &&\
		pip install --no-cache-dir -r requirements.txt

test:
	# Additional, optional, tests could go here
	python -m pytest -vv

lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	# This is linter for Dockerfiles
	hadolint Dockerfile
	# This is a linter for Python source code linter: https://www.pylint.org/
	# This should be run from inside a virtualenv
	black --line-length 79 --experimental-string-processing .
	flake8 .

all: install lint test