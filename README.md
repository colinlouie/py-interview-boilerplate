# Getting started

Note: This setup is macOS-centric.

After initially cloning (or updating) the repository, you can install/upgrade project dependencies via the following
steps.

## Python 3.12

At the time of writing, this is the latest stable version of Python.

```shell
brew install python@3.12
```

This will install the Python packages required for this project.

```shell
pip3 install --break-system-packages --user --requirement requirements.txt
```

# Development

## Docker Compose

You can choose to launch Docker Compose for any necessary dependencies. I choose to run it in the foreground and watch
the logs.

I have included PostgreSQL (RDBMS), Redis (Cache), and localstack (provides local AWS resources).

```shell
docker compose up
```

If you need to purge the entire Docker environment (relevant for this project), you can do so via:

```shell
docker compose down --volumes
```

## Testing and Debugging

This will execute PyTest, which automatically enumerates test suites in the `test/` directory.

```shell
make test
```

Alternatively, you can use VSCode's debugger option `Python Debugger: Debug Python file` against the test suite (file), in conjunction with breakpoints on your implementation/test code.

## Background

`.env` sets up PYTHONPATH for VSCode's debugger environment.
`.vscode/launch.json` was setup for Python debugging.
