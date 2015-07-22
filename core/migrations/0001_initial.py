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
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('nb_terrains', models.IntegerField()),
                ('nb_gymnasiums', models.IntegerField()),
                ('nb_teams', models.SmallIntegerField()),
                ('night', models.BooleanField(default=False)),
                ('surface', models.CharField(max_length=10)),
                ('name_gymnasium', models.CharField(max_length=255, blank=True)),
                ('nb_in_street', models.CharField(max_length=10, blank=True)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=16, blank=True)),
                ('region', models.CharField(max_length=100, blank=True)),
                ('country', models.CharField(max_length=50)),
                ('latitude', models.FloatField(blank=True, default=0)),
                ('longitude', models.FloatField(blank=True, default=0)),
                ('description', models.TextField()),
                ('website', models.URLField(max_length=100, blank=True)),
                ('full', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('nb_players', models.PositiveSmallIntegerField(choices=[(2, '2x2'), (3, '3x3'), (4, '4x4'), (6, '6x6')])),
                ('sx_players', models.CharField(choices=[('male', 'Masculin'), ('female', 'Féminin'), ('mixed', 'Mixte')], max_length=8)),
                ('price', models.FloatField(default=0)),
                ('hobby', models.BooleanField(default=False)),
                ('departmental', models.BooleanField(default=False)),
                ('regional', models.BooleanField(default=False)),
                ('national', models.BooleanField(default=False)),
                ('professional', models.BooleanField(default=False)),
                ('kids', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='core.Event', related_name='tournaments')),
            ],
        ),
        migrations.CreateModel(
            name='VBUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club', models.CharField(max_length=100, blank=True)),
                ('phone', models.CharField(max_length=100, blank=True)),
                ('share_mail', models.BooleanField(default=True)),
                ('share_phone', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='vbuserprofile',
            field=models.ForeignKey(unique=True, related_name='events', to='core.VBUserProfile'),
        ),
    ]
