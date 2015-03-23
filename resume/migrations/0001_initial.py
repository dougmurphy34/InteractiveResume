# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomplishment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobSkillJunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job', models.ForeignKey(to='resume.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_type',
            field=models.ForeignKey(to='resume.SkillType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobskilljunction',
            name='skill',
            field=models.ForeignKey(to='resume.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='job',
            field=models.ForeignKey(to='resume.Job'),
            preserve_default=True,
        ),
    ]
