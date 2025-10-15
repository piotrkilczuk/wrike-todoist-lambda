import logging

from wrike_todoist import console


logger = logging.getLogger()
logger.setLevel("INFO")


def run_google_calendar(event, context):
    console.google_calendar_todoist_main()


def run_harmonogram(event, context):
    console.harmonogram_main()


def run_github(event, context):
    console.github_todoist_main()
