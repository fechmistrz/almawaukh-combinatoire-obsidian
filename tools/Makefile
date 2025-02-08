all: venv
	. venv/bin/activate && python3 unvisited_linked.py unvisited_linked.json

venv:
	if ! [ -d venv ]; then python3 -m venv venv; . venv/bin/activate; pip install pywikibot; fi