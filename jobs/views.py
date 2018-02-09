from django.http import HttpResponse
from .scrapper import job_runner
from .models import Job
from datetime import datetime, timedelta


def scheduler(request):
    """
    view for cron based scheduler
    :param request:
    :return:
    """
    job_runner()
    return HttpResponse("Hello bunny :D")


def cleaner(request):
    """
    Cron endpoint for db cleanup
    :param request:
    :return:
    """
    last_month = datetime.today() - timedelta(days=30)
    job = Job.objects.filter(created_at__lte=last_month)
    job.delete()
    return HttpResponse("Bunny Nuked!")

