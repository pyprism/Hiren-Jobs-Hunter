from bs4 import BeautifulSoup
import requests
import django
import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from jobs.models import Keyword, Job


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
    html = requests.get('http://joblist.bdjobs.com/jobsearch.asp?fcatId=8', cookies={'JOBSRPP': '40'})
    soup = BeautifulSoup(html.text, 'html.parser')
    bunny = soup.find_all(class_='job_title_text')
    jobs = []
    jobs_format = {'keyword': '', 'link': ''}
    urls = Job.objects.all()
    for div in bunny:
        for anchor in div.find_all('a'):
            url = 'http://joblist.bdjobs.com/' + anchor.get('href')
            for obj in urls:  # filter duplicate url that are already send
                if not url == obj.url:
                    print('x')
                    hiren = requests.get(url)
                    job_post = BeautifulSoup(hiren.text, 'html.parser')
                    post = job_post.find_all(class_='comp_wrapper')
                    for keyword in keywords:
                        if re.findall('\\b' + keyword.keyword + '\\b', str(post), re.I):
                            jobs_format['keyword'] = keyword.keyword
                            jobs_format['link'] = url
                            jobs.append(jobs_format)
                            Job.objects.create(url=url)
    return jobs

print(bdjobs())