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
    LEVEL_CHOICES =(('hobby', 'Loisir'),
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

    user = models.OneToOneField(User)

    club = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=10,
                             blank=False,
                             choices=LEVEL_CHOICES)
    phone = models.CharField(max_length=100, blank=True)

    share_mail = models.BooleanField(default=True)
    share_phone = models.BooleanField(default=False)

    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "{0} <{1}>".format(self.get_username(), self.get_email())

    def get_user(self):
        return self.user

    def get_username(self):
        return self.user.get_username()

    def get_full_name(self):
        return self.user.get_full_name()

    def get_first_name(self):
        return self.user.first_name

    def get_last_name(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email

    def get_club(self):
        return self.club

    def get_level(self):
        for l in self.LEVEL_CHOICES:
            if self.level == l[0]:
                return l[1]

    def get_phone(self):
        return self.phone

    def get_share_mail(self):
        return self.share_mail

    def get_share_phone(self):
        return self.share_phone

    def get_facebook(self):
        return self.facebook

    def get_twitter(self):
        return self.twitter
