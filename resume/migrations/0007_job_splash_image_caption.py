# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_job_splash_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='splash_image_caption',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
