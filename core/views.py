from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Tournament, Event, Organizer

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


class EventsList(generic.ListView):
    template_name = 'core/events_list.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        """Return all events."""
        return Event.objects.all()