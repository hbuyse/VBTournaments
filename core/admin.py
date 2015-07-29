#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.contrib import admin
from .models import Event, Tournament


class TournamentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event', 'date']}),
        ('Format', {'fields': ['nb_players', 'sx_players']}),
        ('Level', {'fields': ['hobby', 'departmental', 'regional', 'national', 'professional', 'kids']})
    ]
    list_display = ('event', 'date', 'get_vbuser_username', 'get_vbuser_club', 'nb_players', 'sx_players')
    list_filter = ['date']

    def get_event_name(self, obj):
        """Get the name of the tournaments"""
        return obj.event.name

    def get_vbuser_username(self, obj):
        """Get the login of the person who has registered the event"""
        return obj.event.vbuserprofile.get_username()

    def get_vbuser_club(self, obj):
        """Get the name of the club who has registered the event"""
        return obj.event.vbuserprofile.get_club()




class EventAdmin(admin.ModelAdmin):
    # readonly_fields = ("vbuser",)
    fieldsets = [
        (None,           {'fields': ['name', 'full', 'vbuserprofile', 'night', 'surface']}),
        ('Informations', {'fields': ['nb_terrains', 'nb_gymnasiums', 'nb_teams', 'website', 'description']}),
        ('Address',      {'fields': ['name_gymnasium', 'nb_in_street', 'street', 'zip_code', 'city', 'region', 'country']}),
    ]
    list_display = ('name', 'get_vbuser_username', 'nb_teams', 'nb_terrains', 'city', 'country')

    def get_vbuser_username(self, obj):
        """Get the login of the person who has registered the event"""
        return obj.vbuserprofile.get_username()

    def get_vbuser_club(self, obj):
        """Get the name of the club who has registered the event"""
        return obj.vbuserprofile.get_club()




admin.site.register(Event, EventAdmin)
admin.site.register(Tournament, TournamentAdmin)
