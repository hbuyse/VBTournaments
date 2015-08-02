#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.db import models
from django.contrib.auth.models import User
import datetime

import logging
logging.basicConfig()
logger = logging.getLogger()


class Event(models.Model):

    """Event : details of the tournament(s)

    To one event corresponds MULTIPLE tournaments
    """
    SURFACE_CHOICES = (('sand', 'Sable'), ('grass', 'Herbe'), ('indoor', 'Intérieur'))

    _vbuserprofile = models.ForeignKey('accounts.VBUserProfile', db_column='vbuserprofile', related_name='events')
    _name = models.CharField(db_column='name', max_length=100, blank=False)

    _nb_terrains = models.IntegerField(db_column='nb_terrains', blank=False)
    _nb_gymnasiums = models.IntegerField(db_column='nb_gymnasiums', blank=False)
    _nb_teams = models.SmallIntegerField(db_column='nb_teams', blank=False)

    _night = models.BooleanField(db_column='night', default=False)
    _surface = models.CharField(db_column='surface',
                                max_length=10,
                                blank=False,
                                choices=SURFACE_CHOICES)

    _name_gymnasium = models.CharField(db_column='name_gymnasium', max_length=255, blank=True)
    _nb_in_street = models.CharField(db_column='nb_in_street', max_length=10, blank=True)
    _street = models.CharField(db_column='street', max_length=255, blank=False)
    _city = models.CharField(db_column='city', max_length=255, blank=False)
    _zip_code = models.CharField(db_column='zip_code', max_length=16, blank=True)
    _region = models.CharField(db_column='region', max_length=100, blank=True)
    _country = models.CharField(db_column='country', max_length=50, blank=False)

    _latitude = models.FloatField(db_column='latitude', blank=True, default=0)
    _longitude = models.FloatField(db_column='longitude', blank=True, default=0)

    # poster         = models.ImageField()
    _description = models.TextField(db_column='description', blank=False)
    _website = models.URLField(db_column='website', max_length=100, blank=True)

    _full = models.BooleanField(db_column='full', default=False)

    def __str__(self):
        return u"{0}".format(self.name)

    def get_all_tournaments_related(self):
        """
        :return: A list of all the tournaments that are related to the event
        """
        return self.tournaments.order_by('_date').all()

    # TODO: Try to get this method (get_all_events) out of the class
    def get_all_events(self):
        """
        :return: a list of all the tournaments
        """
        return Event.objects.all()

    def get_address(self):
        """
        Based on the address of the event that have been given by the user, this method return a unicode string that
        will be used by easy_maps in order to show the place on a map

        :return: A unicode string that contains the address of the event
        """
        # address_1 = [self.country, self.region, self.city, self.street, str(self.nb_in_street), self.name_gymnasium]
        address_1 = [self.country, self.region, self.city, self.street, str(self.nb_in_street)]
        address_2 = ", ".join([part_address for part_address in address_1 if part_address])

        address = "{0}\n".format(self.name_gymnasium) if self.name_gymnasium else ""
        address += "{0}, {1}\n".format(self.nb_in_street, self.street)
        address += "{0} {1}\n".format(self.zip_code, self.city)
        address += "{0}\n".format(self.region) if self.region else str()
        address += "{0}".format(self.country)

        return {
            "for_html": address,
            "for_maps": address_2,
        }

    @property
    def vbuserprofile(self):
        """
        :return: The first name and the last_name of the event's organizer (VBUserProfile).
        """
        return self._vbuserprofile

    @vbuserprofile.setter
    def vbuserprofile(self, val):
        self._vbuserprofile = val

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def nb_terrains(self):
        return self._nb_terrains

    @nb_terrains.setter
    def nb_terrains(self, val):
        self._nb_terrains = val

    @property
    def nb_gymnasiums(self):
        return self._nb_gymnasiums

    @nb_gymnasiums.setter
    def nb_gymnasiums(self, val):
        self._nb_gymnasiums = val

    @property
    def nb_teams(self):
        return self._nb_teams

    @nb_teams.setter
    def nb_teams(self, val):
        self._nb_teams = val

    @property
    def night(self):
        return self._night

    @night.setter
    def night(self, val):
        self._night = val

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, val):
        self._surface = val

    @property
    def name_gymnasium(self):
        return self._name_gymnasium

    @name_gymnasium.setter
    def name_gymnasium(self, val):
        self._name_gymnasium = val

    @property
    def nb_in_street(self):
        return self._nb_in_street

    @nb_in_street.setter
    def nb_in_street(self, val):
        self._nb_in_street = val

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, val):
        self._street = val

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, val):
        self._city = val

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, val):
        self._zip_code = val

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, val):
        self._region = val

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, val):
        self._country = val

    @property
    def get_country_iso(self):
        return self._country[:2].upper()

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, val):
        self._latitude = val

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, val):
        self._longitude = val

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, val):
        self._description = val

    @property
    def website(self):
        return self._website

    @website.setter
    def website(self, val):
        self._website = val

    @property
    def full(self):
        return self._full

    @full.setter
    def full(self, val):
        self._full = val


class Tournament(models.Model):

    """Create a Tournament

    It could have multiple formats of tournaments during the same day.
    One tournament is at ONE place and belongs to ONE VBUserProfile
    """
    TWO_VS_TWO = 2
    THREE_VS_THREE = 3
    FOUR_VS_FOUR = 4
    SIX_VS_SIX = 6

    _event = models.ForeignKey('core.Event', db_column='event', related_name='tournaments')
    _date = models.DateField(db_column='date', auto_now=False)

    _nb_players = models.PositiveSmallIntegerField(db_column='nb_players',
                                                   choices=[
                                                       (TWO_VS_TWO, '2x2'),
                                                       (THREE_VS_THREE, '3x3'),
                                                       (FOUR_VS_FOUR, '4x4'),
                                                       (SIX_VS_SIX, '6x6')
                                                   ])
    _sx_players = models.CharField(db_column='sx_players',
                                   max_length=8,
                                   choices=[
                                       ('male', 'Masculin'),
                                       ('female', 'Féminin'),
                                       ('mixed', 'Mixte')
                                   ])

    _price = models.FloatField(db_column='price', blank=False, default=0)

    # Different levels
    _hobby = models.BooleanField(db_column='hobby', default=False)
    _departmental = models.BooleanField(db_column='departmental', default=False)
    _regional = models.BooleanField(db_column='regional', default=False)
    _national = models.BooleanField(db_column='national', default=False)
    _professional = models.BooleanField(db_column='professional', default=False)
    _kids = models.BooleanField(db_column='kids', default=False)

    def __str__(self):
        return u"{0} | {1} | {2} | {3}".format(self.event.name, self.date, self.nb_players, self.sx_players)

    def at_least_one_level(self):
        """
        :return: boolean to check the user put at least one level
        """
        levels = [self.hobby, self.departmental, self.regional,
                  self.national, self.professional, self.kids]
        return True if True in levels else False

    def get_event_name(self):
        return self._event.name

    def get_event_id(self):
        return self._event.id

    def get_day(self):
        return self._date.strftime("%d")

    def get_month(self):
        return self._date.strftime("%b")

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, val):
        self._event = val

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, val):
        """
        :return: boolean to check if the date of the tournament is not in the past
        """
        if self.date < datetime.date.today():
            raise models.ValidationError("The date of the tournament {} cannot be in the past!".format(self.event.name))

        self._date = val

    @property
    def nb_players(self):
        return self._nb_players

    @nb_players.setter
    def nb_players(self, val):
        self._nb_players = val

    @property
    def sx_players(self):
        return self._sx_players

    @sx_players.setter
    def sx_players(self, val):
        self._sx_players = val

    @property
    def hobby(self):
        return self._hobby

    @hobby.setter
    def hobby(self, val):
        self._hobby = val

    @property
    def departmental(self):
        return self._departmental

    @departmental.setter
    def departmental(self, val):
        self._departmental = val

    @property
    def regional(self):
        return self._regional

    @regional.setter
    def regional(self, val):
        self._regional = val

    @property
    def national(self):
        return self._national

    @national.setter
    def national(self, val):
        self._national = val

    @property
    def professional(self):
        return self._professional

    @professional.setter
    def professional(self, val):
        self._professional = val

    @property
    def kids(self):
        return self._kids

    @kids.setter
    def kids(self, val):
        self._kids = val

    def get_list_levels(self):
        l = list()

        if self.hobby:
            l.append("Loisirs")

        if self.departmental:
            l.append("Départemental")

        if self.regional:
            l.append("Régional")

        if self.national:
            l.append("National")

        if self.professional:
            l.append("Professionel")

        if self.kids:
            l.append("Enfant")

        return l
