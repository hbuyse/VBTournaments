from django.shortcuts import render

from django.http import HttpResponse

from .models import Tournament, Event, Organizer

# Create your views here.
def index(request):
    return render(request, 'core/header.html')