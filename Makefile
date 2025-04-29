.PHONY: create-activity run tests

create-activity:
	python3 -m amorfati.utils.create_activity

run:
	python3 -m amorfati.cli.main

tests:
	pytest tests

