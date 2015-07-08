# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nb_terrains', models.PositiveSmallIntegerField()),
                ('nb_gymnasiums', models.PositiveSmallIntegerField()),
                ('nb_teams', models.PositiveSmallIntegerField()),
                ('night', models.BooleanField(default=False)),
                ('surface', models.CharField(max_length=30)),
                ('name_gymnasium', models.CharField(blank=True, max_length=255)),
                ('nb_in_street', models.PositiveSmallIntegerField(blank=True)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.PositiveIntegerField()),
                ('region', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('website', models.URLField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('organizer_login', models.CharField(max_length=30)),
                ('organizer_first_name', models.CharField(max_length=50)),
                ('organizer_last_name', models.CharField(max_length=50)),
                ('organizer_club', models.CharField(blank=True, max_length=100)),
                ('organizer_mail', models.EmailField(max_length=254)),
                ('organizer_share_mail', models.BooleanField(default=False)),
                ('organizer_share_phone', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('nb_players', models.CharField(max_length=3)),
                ('sx_players', models.CharField(max_length=8)),
                ('hobby', models.BooleanField(default=False)),
                ('departmental', models.BooleanField(default=False)),
                ('regional', models.BooleanField(default=False)),
                ('national', models.BooleanField(default=False)),
                ('professional', models.BooleanField(default=False)),
                ('kids', models.BooleanField(default=False)),
                ('event', models.ForeignKey(related_name='tournaments', to='core.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(related_name='events', to='core.Organizer'),
        ),
    ]
