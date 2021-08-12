import random
from time import sleep

import prefect
from prefect import Flow, task


@task
def inc(x):
    sleep(random.random() / 10)
    return x + 1


@task
def dec(x):
    sleep(random.random() / 10)
    return x - 1


@task
def add(x, y):
    sleep(random.random() / 10)
    return x + y


@task(name="sum")
def list_sum(arr):
    logger = prefect.context.get("logger")
    logger.info(f"total sum : {sum(arr)}")
    return sum(arr)


with Flow("getting-started-example") as flow:
    incs = inc.map(x=range(10))
    decs = dec.map(x=range(10))
    adds = add.map(incs, decs)
    total = list_sum(adds)

flow.run()
