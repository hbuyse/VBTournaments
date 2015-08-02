#! /usr/bin/env python

__author__ = "Henri Buyse"


from django import forms
from django.forms.widgets import NumberInput, RadioSelect
import datetime

from .views import Event, Tournament


class EventForm(forms.ModelForm):

    SURFACE_CHOICES = (('beach', 'Sable'), ('grass', 'Herbe'), ('indoor', 'Intérieur'))

    surface = forms.ChoiceField(widget=forms.RadioSelect(), choices=SURFACE_CHOICES)

    class Meta:

        model = Event

        fields = ['_name', '_nb_terrains', '_nb_gymnasiums', '_nb_teams', '_night', '_surface', '_name_gymnasium',
                  '_nb_in_street', '_street', '_city', '_country', '_description', '_website']

        labels = {
            'city': 'Ville',
            'country': 'Pays',
            'description': 'Description',
            'full': 'Complet',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'name': 'Nom du tournoi',
            'name_gymnasium': 'Nom du gymnase',
            'nb_gymnasiums': 'Nombre de terrains',
            'nb_in_street': 'Numéro de rue',
            'nb_teams': 'Nombre d\'équipes',
            'nb_terrains': 'Nombre de gymnases',
            'night': 'Tournoi de nuit',
            'price': 'Prix par équipe',
            'region': 'Région',
            'street': 'Nom de rue',
            'surface': 'Surface',
            'website': 'Site internet',
            'zip_code': 'Code postal',
        }

        widgets= {
            # 'description': forms.Textarea(),
            'nb_gymnasiums': NumberInput(attrs={'min': '1'}),
            'nb_teams': NumberInput(attrs={'min': '1'}),
            'nb_terrains': NumberInput(attrs={'min': '1'}),
            # 'surface': RadioSelect(choices=SURFACE_CHOICES, empty_label=None),
        }


class TournamentForm(forms.ModelForm):

    class Meta:
        model = Tournament
        fields = '__all__'
