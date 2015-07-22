# coding: utf-8

__author__ = "hbuyse"

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
    SURFACE_CHOICES = (('beach', 'Sable'), ('grass', 'Herbe'), ('indoor', 'Intérieur'))

    vbuserprofile = models.ForeignKey(User, related_name='events')
    name = models.CharField(max_length=100, blank=False)

    nb_terrains = models.IntegerField(blank=False)
    nb_gymnasiums = models.IntegerField(blank=False)
    nb_teams = models.SmallIntegerField(blank=False)

    night = models.BooleanField(default=False)
    surface = models.CharField(max_length=10,
                               blank=False,
                               choices=SURFACE_CHOICES)

    name_gymnasium = models.CharField(max_length=255, blank=True)
    nb_in_street = models.CharField(max_length=10, blank=True)
    street = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)
    zip_code = models.CharField(max_length=16, blank=True)
    region = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=False)

    latitude = models.FloatField(blank=True, default=0)
    longitude = models.FloatField(blank=True, default=0)

    # poster         = models.ImageField()
    description = models.TextField(blank=False)
    website = models.URLField(max_length=100, blank=True)

    full = models.BooleanField(default=False)

    def __str__(self):
        return u"{0}".format(self.name)

    def get_all_tournaments_related(self):
        """
        :return: A list of all the tournaments that are related to the event
        """
        return self.tournaments.order_by('date').all()

    def get_vbuserprofile(self):
        """
        :return: The first name and the last_name of the event's organizer (VBUserProfile).
        """
        return self.vbuserprofile

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

    # TODO: Try to get this method (get_all_events) out of the class
    def get_all_events(self):
        """
        :return: a list of all the tournaments
        """
        return Event.objects.all()

    def get_name(self):
        return self.name

    def get_nb_terrains(self):
        return self.nb_terrains

    def get_nb_gymnasiums(self):
        return self.nb_gymnasiums

    def get_nb_teams(self):
        return self.nb_teams

    def get_night(self):
        return self.night

    def get_surface(self):
        return self.surface

    def get_name_gymnasium(self):
        return self.name_gymnasium

    def get_nb_in_street(self):
        return self.nb_in_street

    def get_street(self):
        return self.street

    def get_city(self):
        return self.city

    def get_zip_code(self):
        return self.zip_code

    def get_region(self):
        return self.region

    def get_country(self):
        return self.country

    def get_country_iso(self):
        return self.country[:2].upper()

    def get_description(self):
        return self.description

    def get_website(self):
        return self.website

    def get_full(self):
        return self.full


class Tournament(models.Model):
    """Create a Tournament

    It could have multiple formats of tournaments during the same day.
    One tournament is at ONE place and belongs to ONE VBUserProfile
    """
    TWO_VS_TWO = 2
    THREE_VS_THREE = 3
    FOUR_VS_FOUR = 4
    SIX_VS_SIX = 6

    event = models.ForeignKey('Event', related_name='tournaments')
    date = models.DateField(auto_now=False)

    nb_players = models.PositiveSmallIntegerField(choices=[
                                                      (TWO_VS_TWO, '2x2'),
                                                      (THREE_VS_THREE, '3x3'),
                                                      (FOUR_VS_FOUR, '4x4'),
                                                      (SIX_VS_SIX, '6x6')
                                                  ])
    sx_players = models.CharField(max_length=8,
                                  choices=[
                                      ('male', 'Masculin'),
                                      ('female', 'Féminin'),
                                      ('mixed', 'Mixte')
                                  ])

    price = models.FloatField(blank=False, default=0)

    # Different levels
    hobby = models.BooleanField(default=False)
    departmental = models.BooleanField(default=False)
    regional = models.BooleanField(default=False)
    national = models.BooleanField(default=False)
    professional = models.BooleanField(default=False)
    kids = models.BooleanField(default=False)

    def __str__(self):
        return u"{0} | {1} | {2} | {3}".format(self.event.name, self.date, self.nb_players, self.sx_players)

    def date_in_past(self):
        """
        :return: boolean to check if the date of the tournament is not in the past
        """
        if self.date < datetime.date.today():
            raise models.ValidationError(
                "The date of the tournament {} cannot be in the past!".format(self.event.name))

    def at_least_one_level(self):
        """
        :return: boolean to check the user put at least one level
        """
        levels = [self.hobby, self.departmental, self.regional,
                  self.national, self.professional, self.kids]
        return True if True in levels else False

    def get_event_name(self):
        return self.event.get_details()['name']

    def get_event_id(self):
        return self.event.id

    def get_day(self):
        return self.date.strftime("%d")

    def get_month(self):
        return self.date.strftime("%b")

    def get_event(self):
        return self.event

    def get_date(self):
        return self.date

    def get_nb_players(self):
        return self.nb_players

    def get_sx_players(self):
        return self.sx_players

    def get_hobby(self):
        return self.hobby

    def get_departmental(self):
        return self.departmental

    def get_regional(self):
        return self.regional

    def get_national(self):
        return self.national

    def get_professional(self):
        return self.professional

    def get_kids(self):
        return self.kids

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
