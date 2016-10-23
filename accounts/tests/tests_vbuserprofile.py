#! /usr/bin/env python

__author__ = 'Henri Buyse'


import pytest
import datetime

from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.models import User

from accounts.models import VBUserProfile


key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")


@pytest.mark.django_db
def test_vbu_password():
    jd = user = User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto')
    vbu = VBUserProfile.objects.create(user=jd, key_expires=key_expires)

    # User not in database
    assert check_password({}, 'unknown', '') == None

    # Valid user with wrong password
    assert vbu.user.check_password('incorrect') == False

    # Valid user with correct password
    assert vbu.user.check_password('toto') == True

    # correct password, but user is inactive
    jd.is_active = False
    assert vbu.user.check_password({}) == False

    # Valid user with incorrect password
    assert vbu.user.check_password({}) == False


@pytest.mark.django_db
def test_get_user():
    vbu = VBUserProfile.objects.create(
        user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto'), key_expires=key_expires)

    assert vbu.get_username() != None
    assert vbu.get_username() != str()
    assert vbu.get_username() != "jdoe1"
    assert vbu.get_username() == "jdoe"


@pytest.mark.django_db
def test_get_username():
    vbu = VBUserProfile.objects.create(
        user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto'), key_expires=key_expires)

    assert vbu.get_username() != None
    assert vbu.get_username() != ''
    assert vbu.get_username() == 'jdoe'


@pytest.mark.django_db
def test_get_full_name():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(
        username='jdoe', first_name='John', last_name='Doe'), key_expires=key_expires)

    assert vbu.get_full_name() != None
    assert vbu.get_full_name() != ''
    assert vbu.get_full_name() != 'John'
    assert vbu.get_full_name() != 'Doe'
    assert vbu.get_full_name() == 'John Doe'


@pytest.mark.django_db
def test_get_first_name():
    vbu = VBUserProfile.objects.create(
        user=User.objects.create_user(username='jdoe', first_name='John'), key_expires=key_expires)

    assert vbu.get_first_name() != None
    assert vbu.get_first_name() != ''
    assert vbu.get_first_name() != 'Doe'
    assert vbu.get_first_name() == 'John'


@pytest.mark.django_db
def test_get_last_name():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', last_name='Doe'), key_expires=key_expires)

    assert vbu.get_last_name() != None
    assert vbu.get_last_name() != ''
    assert vbu.get_last_name() != 'John'
    assert vbu.get_last_name() == 'Doe'


@pytest.mark.django_db
def test_get_email():
    vbu = VBUserProfile.objects.create(
        user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr'), key_expires=key_expires)

    assert vbu.get_email() != None
    assert vbu.get_email() != ''
    assert vbu.get_email() == 'jdoe@jdoe.fr'


def test_get_club():
    vbu = VBUserProfile(club='ASMP')

    assert vbu.club != None
    assert vbu.club != ''
    assert vbu.club == 'ASMP'


def test_get_level():
    vbu = VBUserProfile(level='hobby')

    assert vbu.level != None
    assert vbu.level != ''
    assert vbu.level == 'Loisir'


def test_get_phone():
    vbu = VBUserProfile(phone='+330000000000')

    assert vbu.phone != None
    assert vbu.phone != ''
    assert vbu.phone != 330000000000
    assert vbu.phone == '+330000000000'


def test_get_share_mail():
    vbu = VBUserProfile()

    assert vbu.share_mail != None
    assert vbu.share_mail != False
    assert vbu.share_mail == True


def test_get_facebook():
    vbu = VBUserProfile(facebook='jdoe')

    assert vbu.facebook != None
    assert vbu.facebook != ''
    assert vbu.facebook == 'jdoe'


def test_get_twitter():
    vbu = VBUserProfile(twitter='jdoe')

    assert vbu.twitter != None
    assert vbu.twitter != ''
    assert vbu.twitter == 'jdoe'
