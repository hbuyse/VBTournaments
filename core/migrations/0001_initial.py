# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('_name', models.CharField(max_length=100, db_column='name')),
                ('_nb_terrains', models.IntegerField(db_column='nb_terrains')),
                ('_nb_gymnasiums', models.IntegerField(db_column='nb_gymnasiums')),
                ('_nb_teams', models.SmallIntegerField(db_column='nb_teams')),
                ('_night', models.BooleanField(db_column='night', default=False)),
                ('_surface', models.CharField(choices=[('sand', 'Sable'), ('grass', 'Herbe'), ('indoor', 'Intérieur')], max_length=10, db_column='surface')),
                ('_name_gymnasium', models.CharField(max_length=255, db_column='name_gymnasium', blank=True)),
                ('_nb_in_street', models.CharField(max_length=10, db_column='nb_in_street', blank=True)),
                ('_street', models.CharField(max_length=255, db_column='street')),
                ('_city', models.CharField(max_length=255, db_column='city')),
                ('_zip_code', models.CharField(max_length=16, db_column='zip_code', blank=True)),
                ('_region', models.CharField(max_length=100, db_column='region', blank=True)),
                ('_country', models.CharField(max_length=50, db_column='country')),
                ('_latitude', models.FloatField(db_column='latitude', default=0, blank=True)),
                ('_longitude', models.FloatField(db_column='longitude', default=0, blank=True)),
                ('_description', models.TextField(db_column='description')),
                ('_website', models.URLField(max_length=100, db_column='website', blank=True)),
                ('_full', models.BooleanField(db_column='full', default=False)),
                ('_vbuserprofile', models.ForeignKey(to='accounts.VBUserProfile', db_column='vbuserprofile', related_name='events')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('_date', models.DateField(db_column='date')),
                ('_nb_players', models.PositiveSmallIntegerField(choices=[(2, '2x2'), (3, '3x3'), (4, '4x4'), (6, '6x6')], db_column='nb_players')),
                ('_sx_players', models.CharField(choices=[('male', 'Masculin'), ('female', 'Féminin'), ('mixed', 'Mixte')], max_length=8, db_column='sx_players')),
                ('_price', models.FloatField(db_column='price', default=0)),
                ('_hobby', models.BooleanField(db_column='hobby', default=False)),
                ('_departmental', models.BooleanField(db_column='departmental', default=False)),
                ('_regional', models.BooleanField(db_column='regional', default=False)),
                ('_national', models.BooleanField(db_column='national', default=False)),
                ('_professional', models.BooleanField(db_column='professional', default=False)),
                ('_kids', models.BooleanField(db_column='kids', default=False)),
                ('_event', models.ForeignKey(to='core.Event', db_column='event', related_name='tournaments')),
            ],
        ),
    ]
