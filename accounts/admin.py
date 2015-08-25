#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.contrib import admin
from .models import VBUserProfile


class VBUserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['_user']}),
        ('User informations', {'fields': ['_club', '_level', '_phone']}),
        ('Share informations', {'fields': ['_share_mail', '_share_phone']}),
        ('Social informations', {'fields': ['_facebook', '_twitter']}),
        ('Activation key informations', {'fields': ['_activation_key', '_key_expires']}),
        ]
    list_display=('get_username', 'get_email', '_club')
    search_fields = ['_user.username', '_user.first_name', '_user.last_name']

    def get_username(self, obj):
        return obj.user.get_username()

    def get_email(self, obj):
        return obj.user.email



admin.site.register(VBUserProfile, VBUserProfileAdmin)
