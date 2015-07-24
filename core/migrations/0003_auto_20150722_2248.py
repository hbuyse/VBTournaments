# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150722_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='surface',
            field=models.CharField(max_length=10, choices=[('beach', 'Sable'), ('grass', 'Herbe'), ('indoor', 'Intérieur')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='vbuserprofile',
            field=models.ForeignKey(related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
