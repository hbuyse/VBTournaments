# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150712_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]
