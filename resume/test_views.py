__author__ = 'doug'
from django.core.urlresolvers import reverse
import datetime
from resume.models import Job
from django.test import TestCase


def create_job(company_name, job_title):
    this_date = datetime.date.today()
    return Job.objects.create(company_name=company_name, start_date=this_date, job_title=job_title)


class JobListViewTests(TestCase):
    def test_job_list_with_no_jobs(self):
        # TODO 5): custom error message.  There should never be zero jobs in the db.
        response = self.client.get(reverse('job_list')) #as named in urls.py
        self.assertEqual(response.status_code, 200)

    def test_job_list_with_one_job(self):
        create_job("Some Place", "Worker Bee")
        response = self.client.get(reverse('job_list'))
        self.assertEqual(response.status_code, 200)


class JobDetailViewTests(TestCase):
    """ TODO: This correctly does not return a 200 (because no job selected), but
            I need to handle this error gracefully
    def test_job_detail_with_no_jobs(self):
        response = self.client.get(reverse('job_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
    """
    def test_job_list_with_one_job(self):
        local_job = create_job("Some Job", "Worker Bee")
        response = self.client.get(reverse('job_detail', args=(local_job.id,)))
        self.assertEqual(response.status_code, 200)