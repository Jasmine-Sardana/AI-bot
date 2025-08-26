PYTHON=python3

install:
	$(PYTHON) -m pip install -r requirements.txt

run-nutrition:
	$(PYTHON) src/nutrition_api.py

run-chatbot:
	$(PYTHON) src/chatbot.py
