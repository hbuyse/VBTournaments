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
from django import forms

from .models import VBUserProfile
from .forms import UserForm


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
    uf = UserForm()

    if request.POST:
        uf = UserForm(request.POST)

        if uf.is_valid():
            # No need to check the integrity of username
            # Already checked with the clean_username method in accounts.forms
            user = User.objects.create_user(username=uf.cleaned_data['username'],
                                            email=uf.cleaned_data['email'],
                                            password=uf.cleaned_data['password1'],
                                            first_name=uf.cleaned_data['first_name'],
                                            last_name=uf.cleaned_data['last_name'])

            VBUserProfile.objects.create(_user=user,
                                         _share_mail=False,
                                         _share_phone=False)

            # Redirect to the 'next' page if 'next' exists (always exists)
            return HttpResponseRedirect(request.GET.get('next') or reverse('core:home'))

    return render_to_response('accounts/register.html', {'form': uf}, context_instance=RequestContext(request))
