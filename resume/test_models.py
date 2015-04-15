__author__ = 'doug'
from django.test import TestCase
from resume.models import Job
import datetime


class JobTestCase(TestCase):
    def setUp(self):
        Job.objects.create(company_name="Floodbat",
                           start_date=datetime.date(2008, 5, 1),
                           end_date=datetime.date(2011, 3, 1),
                           job_title="Hat inspector",
                           job_description="I inspect hats, silly.")
        Job.objects.create(company_name="User Testing",
                           start_date=datetime.date(2011, 1, 1),
                           job_title="Usability Analyst",
                           job_description="making sure web pages are Just So")

    def test_time_of_service_calculation(self):
        this_job = Job.objects.get(company_name="Floodbat")
        self.assertEqual(this_job.service_time(), 3)

    def test_still_employed_function(self):
        this_job = Job.objects.get(company_name="Floodbat")
        self.assertFalse(this_job.still_employed())

    def test_no_longer_employed(self):
        this_job = Job.objects.get(company_name="User Testing")
        self.assertTrue(this_job.still_employed())

    def test_date_range_still_employed(self):
        this_job = Job.objects.get(company_name="Floodbat")
        self.assertNotIn("today", this_job.date_range())

    def test_date_range_no_longer_employed(self):
        this_job = Job.objects.get(company_name="User Testing")
        self.assertIn("today", this_job.date_range())

    """
    This was written to test my testing.  The test failed (and the above succeeded),
        so testing appears to be working properly.

    def test_failure(self):
        self.assertEqual(1, 0)
    """