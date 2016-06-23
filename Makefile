.PHONY  : all clean install run

VENV        = venv
APP         = ./app.py

all: install

install: $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

run: install
	env FLASK_APP=$(APP) $(VENV)/bin/flask run

clean:
	rm -rf $(VENV) build dist *.egg-info

$(VENV):
	virtualenv $(VENV)
