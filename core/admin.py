#! /usr/bin/env python

__author__ = "Henri Buyse"


from django.contrib import admin
from .models import Event, Tournament


class TournamentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['_event', '_date']}),
        ('Format', {'fields': ['_nb_players', '_sx_players']}),
        ('Level', {'fields': ['_hobby', '_departmental', '_regional', '_national', '_professional', '_kids']})
    ]
    list_display = ('_event', '_date', 'get_vbuser_username', 'get_vbuser_club', '_nb_players', '_sx_players')
    list_filter = ['_date']

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
        (None,           {'fields': ['_name', '_full', '_vbuserprofile', '_night', '_surface']}),
        ('Informations', {'fields': ['_nb_terrains', '_nb_gymnasiums', '_nb_teams', '_website', '_description']}),
        ('Address',      {'fields': ['_name_gymnasium', '_nb_in_street', '_street', '_zip_code', '_city', '_region', '_country']}),
    ]
    list_display = ('_name', 'get_vbuser_username', '_nb_teams', '_nb_terrains', '_city', '_country')

    def get_vbuser_username(self, obj):
        """Get the login of the person who has registered the event"""
        return obj.vbuserprofile.get_username()

    def get_vbuser_club(self, obj):
        """Get the name of the club who has registered the event"""
        return obj.vbuserprofile.get_club()




admin.site.register(Event, EventAdmin)
admin.site.register(Tournament, TournamentAdmin)
