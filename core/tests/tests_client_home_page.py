#! /usr/bin/env python

__author__ = "Henri Buyse"


import pytest
from django.test import Client

def test_client_get_home_page():
    c = Client()
    response = c.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_logged_client_get_home_page():
    c = Client()
    c.login(username='test', password='test')
    response = c.get('/')
    assert response.status_code == 200


def test_client_post_home_page():
    c = Client()
    response = c.post('/', {'username': 'john', 'password': 'smith'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_logged_client_post_home_page():
    c = Client()
    c.login(username='test', password='test')
    response = c.post('/', {'username': 'john', 'password': 'smith'})
    assert response.status_code == 200