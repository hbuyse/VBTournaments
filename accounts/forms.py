#! /usr/bin/env python

__author__ = "Henri Buyse"


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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

    password1 = forms.CharField(label="Mot de passe",
                                required=True,
                                widget=forms.PasswordInput(),
                                max_length=50)

    password2 = forms.CharField(label="Vérification du mot de passe",
                                required=True,
                                widget=forms.PasswordInput(),
                                max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def clean_username(self):
        data = self.cleaned_data['username']

        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("Le nom d'utilisateur {} est déjà pris.".format(data))

        return data

    def clean_email(self):
        data = self.cleaned_data['email']

        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Le courrier électronique {} est déjà utilisé.".format(data))

        return data

    def clean_password2(self):
        data1 = self.cleaned_data['password1']
        data2 = self.cleaned_data['password2']

        if not data2:
            raise forms.ValidationError("Vous devez confirmer votre mot de passe.")

        if data1 != data2:
            raise forms.ValidationError("Les mots de passe ne sont pas identiques.")

        return data2