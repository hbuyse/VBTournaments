# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VBUserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('_club', models.CharField(max_length=100, db_column='club', blank=True)),
                ('_level', models.CharField(max_length=14, db_column='level', choices=[('hobby', 'Loisir'), ('departmental', 'Départemental'), ('regional_1', 'Régional 1'), ('regional_2', 'Régional 2'), ('national_1', 'National 1'), ('national_2', 'National 2'), ('national_3', 'National 3'), ('professional_a', 'Professionel A'), ('professional_b', 'Professionel B'), ('kids', 'Enfant')])),
                ('_phone', models.CharField(max_length=100, db_column='phone', blank=True)),
                ('_share_mail', models.BooleanField(db_column='share_mail', default=True)),
                ('_share_phone', models.BooleanField(db_column='share_phone', default=False)),
                ('_facebook', models.CharField(max_length=100, db_column='facebook', blank=True)),
                ('_twitter', models.CharField(max_length=100, db_column='twitter', blank=True)),
                ('_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
