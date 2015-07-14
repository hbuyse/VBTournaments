from django.contrib import admin
from core.models import UserProfile, Event, Tournament




class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User', {'fields': ['user']}),
        ('Other informations', {'fields': ['club', 'phone']}),
    ]
    list_display = ('get_username', 'get_email', 'club')
    search_fields = ['user.username', 'user.first_name', 'user.last_name']




class TournamentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event', 'date']}),
        ('Format', {'fields': ['nb_players', 'sx_players']}),
        ('Level', {'fields': ['hobby', 'departmental', 'regional', 'national', 'professional', 'kids']})
    ]
    list_display = ('event', 'date', 'get_userprofile_username', 'get_userprofile_club', 'nb_players', 'sx_players')
    list_filter = ['date']

    def get_event_name(self, obj):
        """Get the name of the tournaments"""
        return obj.event.name

    def get_userprofile_username(self, obj):
        """Get the login of the person who has registered the event"""
        return obj.event.userprofile.get_username()

    def get_userprofile_club(self, obj):
        """Get the name of the club who has registered the event"""
        return obj.event.userprofile.club




class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'full', 'userprofile', 'night', 'surface']}),
        ('Informations', {'fields': ['nb_terrains', 'nb_gymnasiums', 'nb_teams', 'website', 'description']}),
        ('Address', {'fields': ['name_gymnasium', 'nb_in_street', 'street', 'zip_code', 'city', 'region', 'country']}),
    ]
    list_display = ('name', 'get_userprofile_username', 'nb_teams', 'nb_terrains')

    def get_userprofile_username(self, obj):
        """Get the login of the person who has registered the event"""
        return obj.userprofile.get_username()

    def get_userprofile_club(self, obj):
        """Get the name of the club who has registered the event"""
        return obj.userprofile.club




admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Tournament, TournamentAdmin)