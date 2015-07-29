#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from geopy.geocoders import Nominatim, GoogleV3
import json

from .models import Tournament, Event
from .forms import EventForm

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


class EventsListView(generic.ListView):
    template_name = 'core/events_list.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        """Return all events."""
        return Event.objects.all()


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'core/event_detail.html'
    context_object_name = 'event'


@login_required
def add_new_event(request):
    if request.method == 'GET':
        form = EventForm()
    elif request.method == 'POST':
        form = EventForm(request.POST)

        print(json.dumps(request.POST, indent=4))

        if form.is_valid():
            userprofile = form.cleaned_data['userprofile']
            name = form.cleaned_data['name']
            nb_terrains = form.cleaned_data['nb_terrains']
            nb_gymnasiums = form.cleaned_data['nb_gymnasiums']
            nb_teams = form.cleaned_data['nb_teams']
            night = form.cleaned_data['night']
            surface = form.cleaned_data['surface']
            name_gymnasium = form.cleaned_data['name_gymnasium']
            nb_in_street = form.cleaned_data['nb_in_street']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']

            geolocator = GoogleV3(api_key="AIzaSyD8HsL7rc6pC6Oo9usD_mCggAq60HdiD7M")
            locations = geolocator.geocode("{nb_in_street} {street}, {city}, {country}".format(nb_in_street=nb_in_street,
                                                                                               street=street,
                                                                                               city=city,
                                                                                               country=country),
                                           exactly_one=True)

            for ac in locations.raw['address_components']:
                nb_in_street = ac["short_name"] if "stree_number" in ac["types"] else nb_in_street
                street = ac["short_name"] if "route" in ac["types"] else street
                city = ac["short_name"] if "locality" in ac["types"] else city
                region = ac["short_name"] if "administrative_area_level_1" in ac["types"] else region
                country = ac["short_name"] if "country" in ac["types"] else country
                zip_code = ac["short_name"] if "postal_code" in ac["types"] else None

            if len(locations.raw) != 1:
                return render(request, 'core/event_form.html', {'form': EventForm(request.POST)})



            e = Event.objects.create(
                vbuser=vbuser,
                name=name,
                nb_terrains=nb_terrains,
                nb_gymnasiums=nb_gymnasiums,
                nb_teams=nb_teams,
                night=night,
                surface=surface,
                name_gymnasium=name_gymnasium,
                nb_in_street=nb_in_street,
                street=street,
                city=city,
                zip_code=zip_code,
                region=region,
                country=country,
                latitude=latitude,
                longitude=longitude,
                description=description,
                website=website,
                full=full
            )

            return HttpResponseRedirect(reverse('event_detail', kwargs={'pk': e.id}))

        print(form.errors)
    return render(request, 'core/event_form.html', {'form': form})
