from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
   fields = ('sender', 'receiver', 'message', 'time_sent', 'time_read')
   list_display = ('sender', 'receiver', 'message', 'time_sent', 'time_read')
   list_filter = ('sender', 'receiver', 'time_sent', 'time_read')
   ordering = ('time_sent',)
   search_fields = ('message',)


#admin.site.register(Venue, VenueAdmin)
#admin.site.register(Event)
