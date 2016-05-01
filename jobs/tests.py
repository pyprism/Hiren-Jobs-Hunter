from django.test import TransactionTestCase
from .models import Keyword, Job


class ModelTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        Job.objects.create(url="http://job.me")
        Keyword.objects.create(keyword="Django")

    def test_job_model(self):
        job = Job.objects.all()
        self.assertEqual(job.count(), 1)
        self.assertEqual(job[0].url, "http://job.me")

    def test_keyword_model(self):
        keywords = Keyword.objects.all()
        self.assertEqual(keywords.count(), 1)
        self.assertEqual(keywords[0].keyword, 'Django')
