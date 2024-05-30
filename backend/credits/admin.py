from django.contrib import admin
from .models import Credits

@admin.register(Credits)
class VCreditsAdmin(admin.ModelAdmin):
   fields = ('teacher', 'owner', 'credits', 'date')
   list_display = ('teacher', 'owner', 'credits', 'date')
   list_filter = ('teacher', 'owner', 'credits', 'date')
   ordering = ('teacher', 'owner', 'date')
   search_fields = ('teacher', 'owner', 'date')


#admin.site.register(Venue, VenueAdmin)
#admin.site.register(Event)
