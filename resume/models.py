from django.db import models
import datetime


class Job(models.Model):
    company_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField(null=True)
    # company_logo returns a string that, when passed to "static" in an image src, will load the logo.
    # Usage: <img src="{% static job.company_logo %}" />
    company_logo = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return str(self.company_name + " - " + self.job_title)

    def still_employed(self):
        # does Doug still work at this job?
        return self.end_date is None

    def service_time(self):

        years_since = 0
        round_up = 0

        if self.still_employed():
            years_since = datetime.date.today() - self.start_date
        else:
            years_since = self.end_date - self.start_date

        if (years_since.days % 365.25) > 182:
            round_up = 1

        final_answer = int(years_since.days / 365.25) + round_up

        if final_answer == 0:
            return "< 1"
        else:
            return final_answer

    def date_range(self):
        # strftime('%B') means string format the time, using full month name based on locale.  See:
        # http://php.net/manual/en/function.strftime.php
        range_string = self.start_date.strftime('%B') + " " + str(self.start_date.year)

        if self.still_employed():
            range_string += " - today"
        else:
            range_string += " - " + self.end_date.strftime('%B') + " " + str(self.end_date.year)

        return range_string

    def related_skills(self):
        return Skill.objects.filter(jobskilljunction__job=self.pk)


class Accomplishment(models.Model):
    job = models.ForeignKey(Job)
    accomplishment_text = models.CharField(max_length=200)


class SkillType(models.Model):
    type_name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.type_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_type = models.ForeignKey(SkillType)
    skill_logo = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.skill_name


class JobSkillJunction(models.Model):
    job = models.ForeignKey(Job)
    skill = models.ForeignKey(Skill)

    def __unicode__(self):
        return str(self.job) + ' - ' + str(self.skill)