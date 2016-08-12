from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import django
import os
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hiren.settings")
django.setup()

from hiren.settings import JSON_DATA
from jobs.models import Keyword, Job


def send_message(job):
    """
    Send email via mailgun
    :param job:
    :return:
    """
    try:
        requests.post("https://api.mailgun.net/v3/" + JSON_DATA['mailgun_domain'] + "/messages",
                      auth=("api", JSON_DATA['mailgun_key']),
                      data={"from": "New Job Post <" + JSON_DATA['mailgun_from'] + ">",
                            "to": [JSON_DATA['mailgun_to']],
                            "subject": "Job about: " + job['keyword'],
                            "text": "Here is a new job post that I got for you! " + job['keyword'] +
                                    ": " + job['link']})
    except Exception as e:
        print(job, e)


def bdjobs():
    """
    BDJob scrapper
    :return result:
    """
    ua = UserAgent(cache=False)
    keywords = Keyword.objects.all()
    headers = {'User-Agent': ua.random}  # because they are blocking :/ without user agent
    html = requests.get('http://jobs.bdjobs.com/jobsearch.asp?fcatId=8&icatId=', cookies={'JOBSRPP': '40'}, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    bunny = soup.find_all(class_='job_title_text')
    jobs = []
    jobs_format = {'keyword': '', 'link': ''}
    for div in bunny:
        for anchor in div.find_all('a'):
            url = 'http://joblist.bdjobs.com/' + anchor.get('href')   # first get the link
            if Job.objects.filter(url=url).exists() is False:  # check for duplicate url that are already scraped
                    hiren = requests.get(url)  # get the job post
                    job_post = BeautifulSoup(hiren.text, 'html.parser')
                    post = job_post.find_all(class_='comp_wrapper')   # get the job contents
                    for keyword in keywords:
                        if re.findall('\\b' + keyword.keyword + '\\b', str(post), re.I):
                            jobs_format['keyword'] = keyword.keyword
                            jobs_format['link'] = url
                            jobs.append(jobs_format)
                    Job.objects.create(url=url)
    return jobs


def job_runner():
    """
    just a dumb function
    :return:
    """
    jobs = bdjobs()
    if jobs:
        for job in jobs:
            send_message(job)
