# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150723_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='vbuserprofile',
            name='level',
            field=models.CharField(max_length=10, choices=[('hobby', 'Loisir'), ('departmental', 'Départemental'), ('regional_1', 'Régional 1'), ('regional_2', 'Régional 2'), ('national_1', 'National 1'), ('national_2', 'National 2'), ('national_3', 'National 3'), ('professional_a', 'Professionel A'), ('professional_b', 'Professionel B'), ('kids)', 'Enfant')], default='hobby'),
            preserve_default=False,
        ),
    ]
