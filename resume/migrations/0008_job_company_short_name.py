# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_job_splash_image_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_short_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
