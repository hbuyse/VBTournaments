# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vbuserprofile',
            name='_activation_key',
            field=models.CharField(max_length=40, default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vbuserprofile',
            name='_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 14, 18, 33, 49, 928481, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
