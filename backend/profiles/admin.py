from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('user','isTeacher', 'profilePic')
    list_filter = ('isTeacher',)
    ordering = ('user',)
    #search_fields = ('user', 'address')


#admin.site.register(Profile, ProfileAdmin)
#admin.site.register(Event)
