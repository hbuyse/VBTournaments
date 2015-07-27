#! /usr/bin/env python

__author__ = 'Henri Buyse'


import pytest
from models import Event, Tournament


def test_str():
    e = Event.objects.create(name="VolleyBall Day")

    assert print(e) != None
    assert print(e) != ''
    assert print(e) == "VolleyBall Day"


def test_get_all_tournaments_related():
    assert True


def test_get_vbuserprofile():
    vbu = VBUserProfile.objects.create(user=User.objects.create_user(username='jdoe', email='jdoe@jdoe.fr', password='toto'))
    e = Event.objects.create(vbuserprofile=vbu)

    assert e.get_vbuserprofile() != None
    assert e.get_vbuserprofile() != VBUserProfile.objects.create()
    assert e.get_vbuserprofile() == vbu


def get_maps_address():
    assert True


def test_get_all_events():
    assert True


def test_get_name():
    e = Event(name="VolleyBall Day")

    assert e.get_name() != None
    assert e.get_name() != ''
    assert e.get_name() == "VolleyBall Day"


def test_get_nb_terrains():
    e = Event(nb_terrains=6)

    assert e.get_nb_terrains() != None
    assert e.get_nb_terrains() != int()
    assert e.get_nb_terrains() != 9
    assert e.get_nb_terrains() == 6


def test_get_nb_gymnasiums():
    e = Event(nb_gymnasiums=2)

    assert e.get_nb_gymnasiums() != None
    assert e.get_nb_gymnasiums() != int()
    assert e.get_nb_gymnasiums() != 9
    assert e.get_nb_gymnasiums() == 2


def test_get_nb_teams():
    e = Event(nb_teams=36)

    assert e.get_nb_teams() != None
    assert e.get_nb_teams() != int()
    assert e.get_nb_teams() != 9
    assert e.get_nb_teams() == 36



def test_get_night():
    e = Event()

    assert e.get_night() != None
    assert e.get_night() != True
    assert e.get_night() == False



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

    assert e.get_full() != None
    assert e.get_full() != True
    assert e.get_full() == False