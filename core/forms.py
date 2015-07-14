# coding: utf-8

__author__ = "hbuyse"

from django import forms
import datetime

from .views import Event, Tournament


class EventForm(forms.ModelForm):

    SURFACE_CHOICES = (('beach', 'Sable'), ('grass', 'Herbe'), ('indoor', 'Intérieur'))

    # userprofile is defined later
    # zip_code is defined later
    # region is defined later
    # latitude is defined later
    # longitude is defined later
    # full is defined later

    name = forms.CharField(label="Nom du tournoi",
                           max_length=100)


    nb_terrains = forms.IntegerField(label="Nombre de gymnases",
                                     min_value=1)
    nb_gymnasiums = forms.IntegerField(label="Nombre de terrains",
                                       min_value=1)
    nb_teams = forms.IntegerField(label="Nombre d'équipes",
                                  min_value=1)
    night = forms.BooleanField(label="Tournoi de nuit",
                               initial=False,
                               required=False)
    surface = forms.ChoiceField(label="Surface",
                                choices=SURFACE_CHOICES,
                                widget=forms.RadioSelect)


    name_gymnasium = forms.CharField(label="Nom du gymnase",
                                     max_length=255,
                                     required=False)
    nb_in_street = forms.CharField(label="Numéro de rue",
                                   max_length=10,
                                   required=False)
    street = forms.CharField(label="Nom de rue",
                             max_length=255)
    city = forms.CharField(label="Ville",
                           max_length=255)
    country = forms.CharField(label="Pays",
                              max_length=50)

    description = forms.CharField(label="Description",
                                  widget=forms.Textarea,
                                  required=False)
    website = forms.URLField(label="Site internet",
                             max_length=100,
                             required=False)

    class Meta:
        model = Event
        fields = '__all__'
        # fields = [
        #     'name',
        #     'nb_terrains',
        #     'nb_gymnasiums',
        #     'nb_teams',
        # ]


class TournamentForm(forms.ModelForm):

    class Meta:
        model = Tournament
        fields = '__all__'
