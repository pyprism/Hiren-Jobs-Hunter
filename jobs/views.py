from django.http import HttpResponse
from .scrapper import job_runner


def scheduler(request):
    """
    view for cron based scheduler
    :param request:
    :return:
    """
    job_runner()
    return HttpResponse("Hello bunny :D")

