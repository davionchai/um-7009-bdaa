install-dev:
	pip install -r requirements-dev.txt

install:
	pip install -r requirements.txt

start:
	streamlit run app.py
