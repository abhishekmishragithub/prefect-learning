# prefect-learning

This repo has basic examples of [prefect](https://www.prefect.io/)

## Install prefect

---

Create a separate environment if you prefer. You can use [miniconda](https://docs.conda.io/en/latest/miniconda.html), [pipenv](https://pipenv.pypa.io/en/latest/) or [virtualenv](https://virtualenv.pypa.io/en/latest/)

To install prefect run

```shell
pip install prefect
```

to install it via conda or pienv refer the prefect [doc](https://docs.prefect.io/core/getting_started/installation.html#installation)

## Running local prefct server & dashboard GUI

---
before starting the server, first run

```shell
prefect backend server
```

This will configure prefect for local [orchestration](https://docs.prefect.io/orchestration/).

To start the server, run

```shell
prefect server start
```

It will start the local server with UI. You can check the dashboard at [localhost:8080](localhost:8080)

You can also specify the port number by giving the option `--ui-port port_number`

example: `prefect server start --ui-port 8085`

## Running a prefect agent

---

At least one prefect agent is required if you want to run a flow from server.

To run a local agent, run

```shell
prefect agent local start
```

Before running flow, you need to create project (from UI) so that you can register a flow to a project.

Once a project is created, you can register a flow with the server by calling `flow.register()` (inside a your program/code)
