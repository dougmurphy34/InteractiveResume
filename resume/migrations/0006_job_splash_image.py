# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20150417_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='splash_image',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
