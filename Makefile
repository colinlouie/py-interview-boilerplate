#!/bin/sh -x

export PYTHONPATH=$(shell pwd)/src/python:$(shell pwd)/etc/python
PYTEST=${HOME}/Library/Python/3.12/bin/pytest

test:
	${PYTEST} -v
