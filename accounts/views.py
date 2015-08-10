#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.db import IntegrityError
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

    return render_to_response('accounts/vbprofile_detail.html', {'object': vbup}, context_instance=RequestContext(request))


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
                return HttpResponseRedirect(request.GET.get('next') or reverse('core:home'))

            else:
                state = "Votre compte est désactivé. Contactez un administrateur du site."

        else:
            state = "Votre nom d'utilisateur et/ou votre mot de passe est incorrect."

    return render_to_response('accounts/login.html', {'state': state, 'username': username, 'next': next}, context_instance=RequestContext(request))


def register(request):
    state = str()
    username = str()
    email = str()
    password1 = str()
    password2 = str()

    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1)

                # Redirect to the 'next' page if 'next' exists (always exists)
                return HttpResponseRedirect("/")
            except IntegrityError as e:
                state = "Le nom d'utilisateur {} est déjà pris.".format(username)
        else:
            state = "Les mots de passe ne sont pas identiques."

    return render_to_response('accounts/register.html', {'state': state, 'username': username, 'email': email}, context_instance=RequestContext(request))
