once:
	python setup.py bdist_wheel

install:
	python setup.py install

check:
	python setup.py check

build:
	python setup.py sdist

whl:
	pip wheel --wheel-dir=./dist ./dist

upload:
	twine upload dist/*


all: once upload