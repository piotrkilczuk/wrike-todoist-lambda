import logging

from wrike_todoist import console


logger = logging.getLogger()
logger.setLevel("INFO")


def run_google_calendar(event, context):
    console.google_calendar_todoist_main()

def run_wrike(event, context):
    console.wrike_todoist_main()
