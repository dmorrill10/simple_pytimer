PIP :=pip
PYTHON :=python
NAME :=simple_pytimer
LIB_NAME :=simple_pytimer

.PHONY: default
default: install

.PHONY: install
install: requirements.txt
	$(PIP) install -r requirements.txt $(ARGS)

.PHONY: clean
clean:
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
	-find $(LIB_NAME) -name "*.so" -delete
	-rm -rf .cache *.egg .eggs *.egg-info build 2> /dev/null
