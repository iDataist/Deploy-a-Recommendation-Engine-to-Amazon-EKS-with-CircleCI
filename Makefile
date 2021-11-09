setup:
	# Create python virtualenv & source it
	# source ~/.devops/bin/activate
	python3 -m venv ~/.devops

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install --requirement requirements.txt

lint:
	hadolint Dockerfile
	# black --line-length 79 --experimental-string-processing .

test:
	python -m pytest -vv

all: install lint test