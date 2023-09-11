install:
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black pandstat/*.py

lint:
	pylint --disable=R,C *.py pandstat/*.py

clean:
	rm -rf dist/ build/ *.egg-info

build:
	python -m build
