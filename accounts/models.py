#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.db import models
from django.contrib.auth.models import User
import datetime

import logging
logging.basicConfig()
logger = logging.getLogger()

import re


class VBUserProfile(models.Model):

    """VBUserProfile : person that create a tournament

    To one VBUserProfile corresponds MULTIPLE events
    """
    LEVEL_CHOICES = (('hobby', 'Loisir'),
                     ('departmental', 'Départemental'),
                     ('regional_1', 'Régional 1'),
                     ('regional_2', 'Régional 2'),
                     ('national_1', 'National 1'),
                     ('national_2', 'National 2'),
                     ('national_3', 'National 3'),
                     ('professional_a', 'Professionel A'),
                     ('professional_b', 'Professionel B'),
                     ('kids', 'Enfant'))

    phone_validator = re.compile('^((\+|00)33\s?|0)[12345679](\s?\d{2}){4}$')

    # User stuff
    _user = models.OneToOneField(User)

    # Volley-ball stuff
    _club = models.CharField(db_column='club',
                             max_length=100,
                             blank=True)
    _level = models.CharField(db_column='level',
                              max_length=14,
                              blank=False,
                              choices=LEVEL_CHOICES)

    # Want or not to share your email and phone number?
    _phone = models.CharField(db_column='phone',
                              max_length=100,
                              blank=True)
    _share_mail = models.BooleanField(db_column='share_mail',
                                      default=True)

    # Username on famous social networks
    _facebook = models.CharField(db_column='facebook',
                                 max_length=100,
                                 blank=True)
    _twitter = models.CharField(db_column='twitter',
                                max_length=100,
                                blank=True)

    # Email activation stuff
    _activation_key = models.CharField(max_length=40)
    _key_expires = models.DateTimeField()

    def __str__(self):
        return "{0} <{1}>".format(self.get_username(), self.get_email())

    ################
    # User methods #
    ################

    def get_username(self):
        return self._user.get_username()

    def get_full_name(self):
        return self._user.get_full_name()

    def get_first_name(self):
        return self._user.first_name

    def get_last_name(self):
        return self._user.last_name

    def get_email(self):
        return self._user.email

    def get_is_staff(self):
        return self._user.is_staff

    def get_is_active(self):
        return self._user.is_active

    def get_is_superuser(self):
        return self._user.is_superuser

    def get_last_login(self):
        return self._user.last_login

    def get_date_joined(self):
        return self._user.date_joined

    #########################
    # VBUserProfile methods #
    #########################
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, val):
        self._user = val


    @property
    def club(self):
        return self._club

    @club.setter
    def club(self, val):
        self._club = val


    @property
    def level(self):
        for l in self.LEVEL_CHOICES:
            if self._level == l[0]:
                return l[1]

    @level.setter
    def level(self, val):
        self._level = val


    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, val):
        self._phone = val


    @property
    def share_mail(self):
        return self._share_mail

    @share_mail.setter
    def share_mail(self, val):
        self._share_mail = val


    @property
    def facebook(self):
        return self._facebook

    @facebook.setter
    def facebook(self, val):
        self._facebook = val


    @property
    def twitter(self):
        return self._twitter

    @twitter.setter
    def twitter(self, val):
        self._twitter = val


    @property
    def activation_key(self):
        return self._activation_key

    @activation_key.setter
    def activation_key(self, val):
        self._activation_key = val


    @property
    def key_expires(self):
        return self._key_expires

    @key_expires.setter
    def key_expires(self, val):
        self._key_expires = val
