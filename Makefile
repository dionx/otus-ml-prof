# .ONESHELL:

PYTHONPATH = PYTHONPATH=./
POETRY_RUN = poetry run

VENV_DIR = .venv

.PHONY: install
install:
	@echo "Установка окружения"
	@echo "Убедитесь, что у вас установлены python3-full и python3-poetry"
	test -d $(VENV_DIR) || virtualenv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate; poetry install

.PHONY: help
help:
	@echo "Первый питонячий проект"
	@cat Makefile
