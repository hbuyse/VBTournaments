# coding: utf-8

__author__ = "hbuyse"

from django.db import models
import datetime

import logging
logging.basicConfig()
logger = logging.getLogger()


"""Organizer : person that create a tournament

To one organizer corresponds MULTIPLE events
"""


class Organizer(models.Model):
    organizer_login = models.CharField(max_length=30)
    organizer_first_name = models.CharField(max_length=50)
    organizer_last_name = models.CharField(max_length=50)
    organizer_club = models.CharField(max_length=100, blank=True)
    organizer_mail = models.EmailField(max_length=254)
    # organizer_phone       =
    organizer_share_mail = models.BooleanField(default=False)
    organizer_share_phone = models.BooleanField(default=False)

    def __str__(self):
        """
        Display for Python2
        :return: Unicode string
        """
        return "{0} - {1} {2} ({3}) - {4}".format(self.organizer_login, self.organizer_first_name,
                                                  self.organizer_last_name, self.organizer_mail, self.organizer_club)

    def get_entire_name(self):
        return "{0} {1}".format(self.organizer_first_name, self.organizer_last_name)

    def get_login(self):
        return "{0}".format(self.organizer_login)

    def get_details(self):
        """
        :return: A dictionary about all the details of the organizer
        """
        return {
            "login": self.organizer_login,
            "first_name": self.organizer_first_name,
            "last_name": self.organizer_last_name,
            "club": self.organizer_club,
            "mail": self.organizer_mail,
            "share_mail": self.organizer_share_mail,
            "share_phone": self.organizer_share_phone,
        }

    def get_number_events_organized(self):
        """
        :return: The number of events that were organized by the organizer
        """
        nb_tournaments = 0
        for event in self.events.all():
            nb_tournaments += event.tournaments.count()

        return {
            "events": self.events.count(),
            "tournaments": nb_tournaments,
        }

    def login_existing(self):
        """
        Raise an exception if the login already exists
        """
        if Organizer.objects.filter(organizer_login=self.organizer_login):
            logger.error('The login {} is already taken by someone.'.format(self.organizer_login))
            raise models.ValidationError("This login is already used by someone.")

    def mail_existing(self):
        """
        Raise an exception if the mail is already used by someone
        """
        if Organizer.objects.filter(organizer_mail=self.organizer_mail):
            logger.error('The email address {} is already taken by someone. Cannot be used by two logins.'.format(
                         self.organizer_mail))
            raise models.ValidationError("This email address is already used by someone.")


"""Event : details of the tournament(s)

To one event corresponds MULTIPLE tournaments
"""


class Event(models.Model):
    organizer = models.ForeignKey(Organizer, related_name='events')
    name = models.CharField(max_length=100)

    nb_terrains = models.PositiveSmallIntegerField()
    nb_gymnasiums = models.PositiveSmallIntegerField()
    nb_teams = models.PositiveSmallIntegerField()

    night = models.BooleanField(default=False)
    surface = models.CharField(max_length=30,
                               choices=[
                                   ('beach', 'Beach'),
                                   ('grass', 'Grass'),
                                   ('indoor', 'Indoor')
                               ])

    name_gymnasium = models.CharField(max_length=255, blank=True)
    nb_in_street = models.PositiveSmallIntegerField(blank=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=16)
    region = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50)

    # poster         = models.ImageField()
    # inscription    = models.FileField()
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

    def get_organizer_name(self):
        """
        :return: The first name and the last_name of the event's organizer.
        """
        return "{0}".format(self.organizer.get_entire_name())

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
        address = address + "{0}, {1}\n".format(self.nb_in_street, self.street)
        address = address + "{0} {1}\n".format(self.zip_code, self.city)
        address = address + "{0}\n".format(self.region) if self.region else address
        address = address + "{0}".format(self.country)

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

    def get_organizer(self):
        return self.organizer

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


"""Create a Tournament

It could have multiple formats of tournaments during the same day.
One tournament is at ONE place and belongs to ONE organizer
"""


class Tournament(models.Model):
    event = models.ForeignKey(Event, related_name='tournaments')

    date = models.DateField(auto_now=False)

    nb_players = models.CharField(max_length=3)
    sx_players = models.CharField(max_length=8)

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
            raise models.ValidationError("The date of the tournament {} cannot be in the past!".format(self.event.name))

    def at_least_one_level(self):
        """
        :return: boolean to check the user put at least one level
        """
        levels = [self.hobby, self.departmental, self.regional, self.national, self.professional, self.kids]
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
