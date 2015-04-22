# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_skill_skill_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomplishment',
            name='accomplishment_text',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
