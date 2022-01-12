SHELL := /usr/bin/env bash

#######
# Help
#######

.DEFAULT_GOAL := help
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

###################
# Conda Enviroment
###################

PY_VERSION := 3.8
CONDA_ENV_NAME ?= venv
TEST_OUTFILE ?= ./graphs/random-graph.png
ACTIVATE_ENV = conda activate ./$(CONDA_ENV_NAME)

.PHONY: build-env
build-env: $(CONDA_ENV_NAME)  ## Build the conda environment
$(CONDA_ENV_NAME):
	conda create -p $(CONDA_ENV_NAME)  --copy -y  python=$(PY_VERSION) python-igraph pycairo
	./$(CONDA_ENV_NAME)/bin/pip install distinctipy

.PHONY: clean
clean:  ## Remove the conda environment and the relevant file
	rm -rf $(CONDA_ENV_NAME)
	rm -rf $(CONDA_ENV_NAME).zip
	rm -rf $(TEST_OUTFILE)

.PHONY: test-env
test-env:  ## Test the conda environment by executing main.py
	./$(CONDA_ENV_NAME)/bin/python main.py
	test -f $(TEST_OUTFILE) && echo "$(TEST_OUTFILE) SUCCESSFULLY CREATED!"
	rm -rf $(TEST_OUTFILE)
