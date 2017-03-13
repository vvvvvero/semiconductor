SHELL := /bin/bash

init:
  python3 setup.py develop
  pip install -r requirements.txt

test:
  rm -f .coverage
  nosetests $(NOSE_ARGS) ./tests/

sure:
  # Think how to setup sure

travis:
  nosetests --with-coverage ./tests/

tdaemon:
	tdaemon -t nose ./tests/ --custom-args="--with-growl"

publish:
	python3 setup.py sdist bdist_wheel upload
