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
        response = self.client.get(reverse('job_list'))  # as named in urls.py
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No jobs found in database")

''' This doesn't work because the test doesn't process angular.  May need different testing module.
    def test_job_list_with_one_job(self):
        create_job("Some Place", "Worker Bee")
        response = self.client.get(reverse('job_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Some Place")
'''


class JobDetailViewTests(TestCase):
    ''' TODO: Rewrite this test

    def test_job_detail_with_no_jobs(self):
        response = self.client.get(reverse('job_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "seem to exist")
    '''

    def test_job_detail_with_one_job(self):
        local_job = create_job("Some Job", "Worker Bee")
        response = self.client.get(reverse('job_detail', args=(local_job.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Some Job")


class WelcomeViewTests(TestCase):
    def test_welcome_loads(self):
        response = self.client.get(reverse('index', args=()))
        self.assertEqual(response.status_code, 200)


class PortfolioViewTests(TestCase):
    def test_portfolio_loads(self):
        response = self.client.get(reverse('portfolio', args=()))
        self.assertEqual(response.status_code, 200)


#The contact template is called from irf's urls.py, not resume's.  But this test still works.
class ContactViewTests(TestCase):
    def test_contact_loads(self):
        response = self.client.get(reverse('contact', args=()))
        self.assertEqual(response.status_code, 200)