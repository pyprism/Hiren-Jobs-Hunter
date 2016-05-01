from celery import shared_task
from jobs.scrapper import job_runner


@shared_task
def run():
    job_runner()