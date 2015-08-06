#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views import generic
from django.core.urlresolvers import reverse

from .models import VBUserProfile


class VBUserProfileListView(generic.ListView):
    template_name = 'accounts/vbprofiles_list.html'
    context_object_name = 'vbprofiles_list'

    def get_queryset(self):
        """Return all events."""
        return VBUserProfile.objects.all()


def vbuserprofile_view(request, username):
    u = User.objects.get(username=username)
    vbup = VBUserProfile.objects.get(_user=u)

    return render_to_response('accounts/vbprofile_detail.html', {'object': vbup})


def login_user(request):
    state = str()
    username = str()
    password = str()

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                # Redirect to the 'next' page if 'next' exists (always exists)
                return HttpResponseRedirect(request.GET.get('next'))

            else:
                state = "Votre compte est désactivé. Contactez un administrateur du site."

        else:
            state = "Votre nom d'utilisateur et/ou votre mot de passe est incorrect."

    return render_to_response('accounts/login.html', {'state': state, 'username': username, 'next': next}, context_instance=RequestContext(request))

