#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from django.template import RequestContext
from django.views import generic
from django.core.urlresolvers import reverse
from django import forms

from django.conf import settings

import hashlib
import random
import datetime

from .models import VBUserProfile
from .forms import UserForm


class VBUserProfileListView(generic.ListView):
    template_name = 'accounts/vbprofiles_list.html'
    context_object_name = 'vbprofiles_list'

    def get_queryset(self):
        """Return all events."""
        return VBUserProfile.objects.all()


def vbuserprofile_view(request, username):
    try:
        u = User.objects.get(username=username)
        vbup = VBUserProfile.objects.get(_user=u)
    except User.DoesNotExist:
        raise Http404("L'utilisateur {} n'existe pas.".format(username))

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
    if request.user.is_authenticated():
        return redirect('core:home')

    uf = UserForm()

    if request.method == 'POST':
        uf = UserForm(request.POST)

        if uf.is_valid():
            datas = dict()
            datas['first_name'] = uf.cleaned_data['first_name']
            datas['last_name'] = uf.cleaned_data['last_name']
            datas['username'] = uf.cleaned_data['username']
            datas['email'] = uf.cleaned_data['email']
            datas['password1'] = uf.cleaned_data['password1']

            # We will generate a random activation key
            salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:5]
            usernamesalt = datas['username']
            if isinstance(usernamesalt, str):
                usernamesalt = usernamesalt
            datas['activation_key'] = hashlib.sha1(str(salt + usernamesalt).encode('utf8')).hexdigest()

            # Settings the email path and subject
            datas['email_path'] = "/mail/activation_email.txt"
            datas['email_subject'] = "Activation de votre compte sur " + settings.FQDN

            uf.sendEmail(datas)  # Send validation email
            uf.save(datas)  # Save the user and his profile

            request.session['registered'] = True  # For display purposes

            # Redirect to the 'next' page if 'next' exists (always exists)
            return HttpResponseRedirect(request.GET.get('next') or reverse('core:home'))

    return render_to_response('accounts/register.html', {'form': uf}, context_instance=RequestContext(request))


# View called from activation email. Activate user if link didn't expire (48h default), or offer to
# send a second link if the first expired.
def activation(request, activation_key):
    # Initiate activation values
    activation_expired = False
    already_active = False

    # Grab the profile based on the activation key
    try:
        vbup = VBUserProfile.objects.get(_activation_key=activation_key)
    except VBUserProfile.DoesNotExist:
        raise Http404("La clé d'activation donnée n'est liée à aucun utilisateur.")

    # Check if the user is not active
    if vbup.user.is_active == False:
        if timezone.now() > vbup.key_expires:
            # Display : offer to user to have another activation link (a link in
            # template sending to the view new_activation_link)
            activation_expired = True
        else:
            # Activation successful
            vbup.user.is_active = True
            vbup.user.save()

    # If user is already active, simply display error message
    else:
        already_active = True

    return render_to_response('accounts/activation.html',
                              {'activation_expired': activation_expired, 'already_active': already_active},
                              context_instance=RequestContext(request))


def new_activation_link(request, username):
    datas = dict()
    uf = UserForm()

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("L'utilisateur {} n'existe pas.".format(username))

    if user is not None and user.is_active == False:
        datas['username'] = user.username
        datas['email'] = user.email
        datas['email_path'] = "/mail/activation_email.txt"
        datas['email_subject'] = "Nouveau lien d'activation " + settings.FQDN

        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:5]
        usernamesalt = datas['username']
        if isinstance(usernamesalt, str):
            usernamesalt = usernamesalt
        datas['activation_key'] = hashlib.sha1(str(salt + usernamesalt).encode('utf8')).hexdigest()

        try:
            vbup = VBUserProfile.objects.get(_user=user)
            vbup.activation_key = datas['activation_key']
            vbup.key_expires = datetime.datetime.strftime(
                datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
            vbup.save()
        except VBUserProfile.DoesNotExist:
            raise Http404("L'utilisateur {} n'a pas de profil. Contactez un administrateur.".format(user.username))

        uf.sendEmail(datas)
        request.session['new_link'] = True  # Display : new link send

    return HttpResponseRedirect(reverse('core:home'))
