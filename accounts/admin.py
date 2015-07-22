from django.contrib import admin
from .models import VBUserProfile


class VBUserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('User informations', {'fields': ['club', 'phone']}),
        ('Share informations', {'fields': ['share_mail', 'share_phone']}),
        ]
    list_display=('get_username', 'get_email', 'club')
    search_fields = ['user.username', 'user.first_name', 'user.last_name']

    def get_username(self, obj):
        return obj.user.get_username()

    def get_email(self, obj):
        return obj.user.email



admin.site.register(VBUserProfile, VBUserProfileAdmin)
