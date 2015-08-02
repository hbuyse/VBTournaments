#! /usr/bin/env python

__author__ = 'Henri Buyse'


import pytest
from core.models import Event, Tournament
from accounts.models import VBUserProfile

from django.contrib.auth.models import User



def test_get_all_tournaments_related():
    assert True


@pytest.mark.django_db
def test_get_vbuserprofile():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto'))
    e = Event.objects.create(name="VolleyBall Day",
                             nb_terrains=1,
                             nb_gymnasiums=1,
                             nb_teams=1,
                             street="Zozo",
                             city="test",
                             country="France",
                             vbuserprofile=vbu)

    assert e.vbuserprofile != None

    jdoe1 = User.objects.create_user(username="jdoe1")
    assert e.vbuserprofile != VBUserProfile.objects.create(user=jdoe1)
    assert e.vbuserprofile == vbu


def get_maps_address():
    assert True


def test_get_all_events():
    assert True


def test_get_name():
    e = Event(name="VolleyBall Day")

    assert e.name != None
    assert e.name != ''
    assert e.name == "VolleyBall Day"


def test_get_nb_terrains():
    e = Event(nb_terrains=6)

    assert e.nb_terrains != None
    assert e.nb_terrains != int()
    assert e.nb_terrains != 9
    assert e.nb_terrains == 6


def test_get_nb_gymnasiums():
    e = Event(nb_gymnasiums=2)

    assert e.nb_gymnasiums != None
    assert e.nb_gymnasiums != int()
    assert e.nb_gymnasiums != 9
    assert e.nb_gymnasiums == 2


def test_get_nb_teams():
    e = Event(nb_teams=36)

    assert e.nb_teams != None
    assert e.nb_teams != int()
    assert e.nb_teams != 9
    assert e.nb_teams == 36


def test_get_night():
    e = Event()

    assert e.night != None
    assert e.night != True
    assert e.night == False


def test_get_surface():
    assert True


def test_get_name_gymnasium():
    assert True


def test_get_nb_in_street():
    assert True


def test_get_street():
    assert True


def test_get_city():
    assert True


def test_get_zip_code():
    assert True


def test_get_region():
    assert True


def test_get_country():
    assert True


def test_get_country_iso():
    assert True


def test_get_description():
    assert True


def test_get_website():
    assert True


def test_get_full():
    e = Event()

    assert e.full != None
    assert e.full != True
    assert e.full == False
