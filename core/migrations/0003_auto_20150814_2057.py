# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'initial_data', app_label='core')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tournament__starting_time'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
