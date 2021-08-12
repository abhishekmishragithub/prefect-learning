from prefect import Flow, task


@task(log_stdout=True)
def say_hello():
    print("Hello, world!")


with Flow("hello task") as f:
    say_hello()

f.run()
# you need to create a project in prefect ui before register the flow with p
f.register(project_name="demo")
