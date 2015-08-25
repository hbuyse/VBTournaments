# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'initial_data', app_label='accounts')

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150814_1833'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
