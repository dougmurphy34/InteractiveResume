# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_accomplishment_accomplishment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomplishment',
            name='accomplishment_text',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
