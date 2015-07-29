#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import VBUserProfile

# Create your views here.
class VBUserProfileListView(generic.ListView):
    template_name = 'accounts/vbprofiles_list.html'
    context_object_name = 'vbprofiles_list'

    def get_queryset(self):
        """Return all events."""
        return VBUserProfile.objects.all()


class VBUserProfileDetailView(generic.DetailView):
    model = VBUserProfile
    template_name = 'accounts/vbprofile_detail.html'
    context_object_name = 'vbuserprofile'