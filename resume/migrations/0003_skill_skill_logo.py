# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_job_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_logo',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
