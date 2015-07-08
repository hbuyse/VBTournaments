from django.contrib import admin
from core.models import Organizer, Event, Tournament




class OrganizerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['organizer_login']}),
        ('Informations', {'fields': ['organizer_first_name', 'organizer_last_name', 'organizer_mail', 'organizer_club']}),
    ]
    list_display = ('organizer_login', 'organizer_first_name', 'organizer_last_name', 'organizer_mail', 'organizer_club')
    search_fields = ['organizer_login', 'organizer_first_name', 'organizer_last_name']




class TournamentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['date']}),
        ('Format', {'fields': ['nb_players', 'sx_players']}),
        ('Level', {'fields': ['hobby', 'departmental', 'regional', 'national', 'professional', 'kids']})
    ]
    list_display = ('event', 'date', 'get_organizer_login', 'get_organizer_club', 'nb_players', 'sx_players')
    list_filter = ['date']

    def get_event_name(self, obj):
        """Get the name of the tournaments"""
        return obj.event.name

    def get_organizer_login(self, obj):
        """Get the login of the person who has registered the tournament"""
        return obj.event.organizer.organizer_login

    def get_organizer_club(self, obj):
        """Get the name of the club who has registered the tournament"""
        return obj.event.organizer.organizer_club




class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'organizer']}),
        ('Informations', {'fields': ['nb_terrains', 'nb_gymnasiums', 'nb_teams', 'website', 'description']}),
        ('Address', {'fields': ['name_gymnasium', 'nb_in_street', 'street', 'zip_code', 'city', 'region', 'country']}),
    ]
    list_display = ('name', 'get_organizer_login', 'nb_teams', 'nb_terrains')

    def get_organizer_login(self, obj):
        """Get the login of the person who has registered the event"""
        return obj.organizer.organizer_login

    def get_organizer_club(self, obj):
        """Get the name of the club who has registered the event"""
        return obj.organizer.organizer_club




admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Tournament, TournamentAdmin)