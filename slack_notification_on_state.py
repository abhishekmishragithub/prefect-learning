"""
This script will just send a slack noitfication on task Success or Failure
You should create a slack app (add it to your workspace), select a channel
you want to send a notifcation to and enable the incoming webhooks
in api.slack.com
"""

from prefect import Flow, task
from prefect.engine.state import Failed, Success
from prefect.utilities.notifications import slack_notifier

# add the slack webhooks to config file
# see : https://docs.prefect.io/core/advanced_tutorials/slack-notifications.html#using-your-url-to-get-notifications
handler = slack_notifier(only_states=[Failed, Success])  # we can call it early


@task(state_handlers=[handler])
def add(x: int, y: int) -> int:
    """add numbers"""
    return x + y


with Flow("hello task") as f:
    add(10, 15)


f.run()
# you need to create a project in prefect ui before registering the flow
f.register(project_name="demo")
