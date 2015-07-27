#! /usr/bin/env python

__author__ = 'Henri Buyse'


import pytest
from accounts.models import VBUserProfile

from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_vbu_password():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto'))

    # User not in database
    assert check_password({}, 'unknown', '') == None

    # Valid user with wrong password
    assert vbu.get_user().check_password('incorrect') == False

    # Valid user with correct password
    assert vbu.get_user().check_password('toto') == True

    # correct password, but user is inactive
    User.objects.filter(username='jdoe').update(is_active=False)
    assert vbu.get_user().check_password({}, 'jdoe', 'toto') == False
    assert check_password({}, 'jdoe', 'toto') == False

    # Valid user with incorrect password
    assert vbu.get_user().check_password({}, 'jdoe', 'incorrect') == False
    assert check_password({}, 'jdoe', 'incorrect') == False


@pytest.mark.django_db
def test_get_user():
    vbu = VBUserProfile.objects.create(
        user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto'))

    assert vbu.get_user() != None
    assert vbu.get_user() != User.objects.create_user()
    assert vbu.get_user() != User.objects.create_user(username='jdoe')
    assert vbu.get_user() != User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr')
    assert vbu.get_user() != User.objects.create_user(username='jdoe', password='toto')
    assert vbu.get_user() == User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto')


def test_get_username():
    vbu = VBUserProfile.objects.create(
        user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto'))

    assert vbu.get_username() != None
    assert vbu.get_username() != ''
    assert vbu.get_username() == 'jdoe'


@pytest.mark.django_db
def test_get_full_name():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', first_name='John', last_name='Doe'))

    assert vbu.get_full_name() != None
    assert vbu.get_full_name() != ''
    assert vbu.get_full_name() != 'John'
    assert vbu.get_full_name() != 'Doe'
    assert vbu.get_full_name() == 'John Doe'


@pytest.mark.django_db
def test_get_first_name():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', first_name='John'))

    assert vbu.get_first_name() != None
    assert vbu.get_first_name() != ''
    assert vbu.get_first_name() != 'Doe'
    assert vbu.get_first_name() == 'John'


@pytest.mark.django_db
def test_get_last_name():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', last_name='Doe'))

    assert vbu.get_last_name() != None
    assert vbu.get_last_name() != ''
    assert vbu.get_last_name() != 'John'
    assert vbu.get_last_name() == 'Doe'


@pytest.mark.django_db
def test_get_email():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr'))

    assert vbu.get_email() != None
    assert vbu.get_email() != ''
    assert vbu.get_email() == 'jdoe@jdoe.fr'


def test_get_club():
    vbu = VBUserProfile(club='ASMP')

    assert vbu.get_club() != None
    assert vbu.get_club() != ''
    assert vbu.get_club() == 'ASMP'


def test_get_level():
    vbu = VBUserProfile(level='hobby')

    assert vbu.get_level() != None
    assert vbu.get_level() != ''
    assert vbu.get_level() == 'Loisir'


def test_get_phone():
    vbu = VBUserProfile(phone='+330000000000')

    assert vbu.get_phone() != None
    assert vbu.get_phone() != ''
    assert vbu.get_phone() != 330000000000
    assert vbu.get_phone() == '+330000000000'


def test_get_share_mail():
    vbu = VBUserProfile()

    assert vbu.get_share_mail() != None
    assert vbu.get_share_mail() != False
    assert vbu.get_share_mail() == True


def test_get_share_phone():
    vbu = VBUserProfile()

    assert vbu.get_share_phone() != None
    assert vbu.get_share_phone() != True
    assert vbu.get_share_phone() == False


def test_get_facebook():
    vbu = VBUserProfile(facebook='jdoe')

    assert vbu.get_facebook() != None
    assert vbu.get_facebook() != ''
    assert vbu.get_facebook() == 'jdoe'


def test_get_twitter():
    vbu = VBUserProfile(twitter='jdoe')

    assert vbu.get_twitter() != None
    assert vbu.get_twitter() != ''
    assert vbu.get_twitter() == 'jdoe'
