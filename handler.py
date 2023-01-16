import logging

from wrike_todoist import console

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def run(event, context):
    console.main()
