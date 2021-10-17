pwd = $(shell pwd)

setup:
	@echo "export PYTHONPATH: $(pwd)";

test:
	source venv/bin/activate
	python -m unittest discover -s tests;
