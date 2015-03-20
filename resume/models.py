from django.db import models


class Fruit(models.Model):
    fruit_name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.fruit_name

class Job(models.Model):
    company_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField(null=True)

    def __unicode__(self):
        return self.company_name

    def still_employed(self):
        # does Doug still work at this job?
        return self.end_date is None


class Accomplishment(models.Model):
    job = models.ForeignKey(Job)


class SkillType(models.Model):
    type_name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.type_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_type = models.ForeignKey(SkillType)

    def __unicode__(self):
        return self.skill_name


class JobSkillJunction(models.Model):
    job = models.ForeignKey(Job)
    skill = models.ForeignKey(Skill)

    def __unicode__(self):
        return str(self.job) + ' - ' + str(self.skill)