from celery import shared_task
from jobs.scrapper import bdjobs


@shared_task
def run():
    bdjobs()