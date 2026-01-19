import logging
import os

import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from wrike_todoist import console


if dsn := os.environ.get("SENTRY_DSN"):
    sentry_sdk.init(dsn=dsn, integrations=[AwsLambdaIntegration()])

logger = logging.getLogger()
logger.setLevel("INFO")


def run_google_calendar(event, context):
    console.google_calendar_todoist_main()


def run_harmonogram(event, context):
    console.harmonogram_main()


def run_github(event, context):
    console.github_todoist_main()
