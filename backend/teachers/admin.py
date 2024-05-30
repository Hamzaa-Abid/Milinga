from django.contrib import admin
from .models import Teacher, TeacherTeaches

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
   fields = ('user', 'videoUrl', 'pricePerHour', 'acceptsBitcoins', 'acceptsFiat')
   list_display = ('user', 'videoUrl', 'pricePerHour', 'acceptsBitcoins', 'acceptsFiat')
   list_filter = ('acceptsBitcoins', 'pricePerHour', 'acceptsFiat')
   ordering = ('user', 'videoUrl', 'pricePerHour', 'acceptsBitcoins', 'acceptsFiat')
   search_fields = ('user', 'videoUrl', 'acceptsBitcoins', 'acceptsFiat')

@admin.register(TeacherTeaches)
class TeacherTeachesAdmin(admin.ModelAdmin):
   fields = ('teacher', 'subject',)
   list_display = ('teacher', 'subject',)
   list_filter = ('subject',)
   ordering = ('teacher', 'subject',)
   search_fields = ('teacher', 'subject',)


#admin.site.register(Venue, VenueAdmin)
#admin.site.register(Event)
