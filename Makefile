install-dev:
	pip install -r requirements-dev.txt

install:
	pip install -r requirements.txt

init: install
	python start.py

start: init
	streamlit run app.py

