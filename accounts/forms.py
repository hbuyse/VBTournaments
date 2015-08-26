#! /usr/bin/env python

__author__ = "Henri Buyse"


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.template import Context, Template
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

import datetime

from .models import VBUserProfile


class UserForm(forms.ModelForm):

    first_name = forms.CharField(label="Votre prénom",
                                 required=True,
                                 max_length=100)

    last_name = forms.CharField(label="Votre nom",
                                required=True,
                                max_length=100)

    username = forms.CharField(label="Nom d'utilisateur",
                               required=True,
                               max_length=50)

    email = forms.EmailField(label="Courrier électronique",
                             required=True)

    password = forms.CharField(label="Mot de passe",
                               required=True,
                               widget=forms.PasswordInput(),
                               max_length=50)

    password_check = forms.CharField(label="Vérification du mot de passe",
                                     required=True,
                                     widget=forms.PasswordInput(),
                                     max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password_check')

    # Override of clean method for :
    # * username check,
    # * email check,
    # * password check
    def clean(self):
        data = self.cleaned_data
        print(data)
        if User.objects.filter(username=data['username']).exists():
            raise ValidationError({'username': ["Le nom d'utilisateur {} est déjà pris.".format(data['username'])]})

        if User.objects.filter(email=data['email']).exists():
            raise ValidationError({'email': ["Le courrier électronique {} est déjà utilisé.".format(data['email'])]})

        if not data['password_check']:
            raise ValidationError({'password_check': ["Vous devez confirmer votre mot de passe."]})

        if data['password'] != data['password_check']:
            raise ValidationError({'password_check': ["Les mots de passe ne sont pas identiques."]})

        return self.cleaned_data

    # Override of save method for saving both User and VBUserProfile objects
    def save(self, datas):
        print(datas)
        u = User.objects.create_user(username=datas['username'],
                                     email=datas['email'],
                                     password=datas['password'],
                                     first_name=datas['first_name'],
                                     last_name=datas['last_name']
                                     )
        u.is_active = False
        u.save()

        vbup = VBUserProfile()
        vbup.user = u
        vbup.activation_key = datas['activation_key']
        vbup.key_expires = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=2), "%Y-%m-%d %H:%M:%S")
        vbup.save()

        return u

    # Handling of activation email sending ------>>>!! Warning : Domain name is hardcoded below !!<<<------
    # I am using a text file to write the email (I write my email in the text
    # file with templatetags and then populate it with the method below)
    def sendEmail(self, datas):
        link = "http://" + settings.FQDN + "/activation/" + datas['activation_key']
        c = Context({'activation_link': link, 'username': datas['username']})

        f = open(settings.MEDIA_ROOT + datas['email_path'], 'r')
        t = Template(f.read())
        f.close()
        message = t.render(c)

        # print unicode(message).encode('utf8')
        send_mail(datas['email_subject'], message, 'VBTournaments <tournaments.vb@' +
                  settings.FQDN + '>', [datas['email']], fail_silently=False)

