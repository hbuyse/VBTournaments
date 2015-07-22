# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vbuserprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='event',
            name='vbuserprofile',
            field=models.ForeignKey(to='accounts.VBUserProfile', related_name='events'),
        ),
        migrations.DeleteModel(
            name='VBUserProfile',
        ),
    ]
