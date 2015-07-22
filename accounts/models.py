# coding: utf-8

__author__ = "hbuyse"

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
    phone_validator = re.compile('^((\+|00)33\s?|0)[12345679](\s?\d{2}){4}$')

    user = models.OneToOneField(User)

    club = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)

    share_mail = models.BooleanField(default=True)
    share_phone = models.BooleanField(default=False)

    def __str__(self):
        return "{0} <{1}>".format(self.get_username(), self.get_email())

    def get_user(self):
        return self.user

    def get_username(self):
        return self.user.get_username()

    def get_first_name(self):
        return self.user.get_first_name()

    def get_last_name(self):
        return self.user.get_last_name()

    def get_email(self):
        return self.user.email

    def get_club(self):
        return self.club

    def get_phone(self):
        return self.phone

    def get_share_mail(self):
        return self.share_mail

    def get_share_phone(self):
        return self.share_phone