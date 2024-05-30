from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
   fields = ('subject',)
   list_display = ('subject',)
   #list_filter = ('subject', 'language_code')
   ordering = ('subject',)
   search_fields = ('subject',)


#admin.site.register(Venue, VenueAdmin)
# admin.site.register(Subject)
