#!/bin/sh -x

export PYTHONPATH=$PYTHONPATH:$(shell pwd)/src/python:$(shell pwd)/etc/python
PYTEST=$(shell pwd)/.venv/bin/pytest

test:
	${PYTEST} -v
