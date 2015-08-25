#! /usr/bin/env python

__author__ = 'Henri Buyse'


import pytest
import datetime

from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.models import User
from django.test import Client

from accounts.models import VBUserProfile


key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")

@pytest.mark.django_db
def test_vbuserdetail_page():
    c = Client()
    response = c.get('/users/')
    assert response.status_code == 200
