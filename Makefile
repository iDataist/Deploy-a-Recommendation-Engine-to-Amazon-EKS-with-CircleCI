setup:
	# Create python virtualenv & source it
	# source ~/.devops/bin/activate
	python3 -m venv ~/.devops

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	# hadolint Dockerfile --ignore DL3013
	black --line-length 79 --experimental-string-processing .

test:
	python -m pytest -vv

all: install lint test