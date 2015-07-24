# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vbuserprofile',
            name='facebook',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='vbuserprofile',
            name='twitter',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
