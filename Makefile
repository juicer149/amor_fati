PYTHONPATH := src
PYTHON := python3

.PHONY: create-activity run test check

create-activity:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m amorfati.utils.create_activity

run:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m amorfati.cli.main

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -v

check:
	$(PYTHON) -m compileall -q src tests
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -v
