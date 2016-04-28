from bs4 import BeautifulSoup
import requests
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from jobs.models import Keyword


def send_message(job):
    try:
        requests.post("https://api.mailgun.net/v3/" + JSON_DATA['mailgun_domain'] + "/messages",
                      auth=("api", JSON_DATA['mailgun_key']),
                      data={"from": "Job Alert <" + JSON_DATA['mailgun_from'] + ">",
                            "to": [JSON_DATA['mailgun_to']],
                            "subject": "Yo Hiren!",
                            "text": "Here is a list of post(s) that I got for you! " + job})
    except Exception as e:
        print(job, e)


def bdjobs():
    keywords = Keyword.objects.all()
    html = requests.get('http://joblist.bdjobs.com/jobsearch.asp?fcatId=8', cookies={'JOBSRPP': 40})
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)


send_message("s")