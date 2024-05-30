from django.contrib import admin
from .models import WorkingTime,Lesson

@admin.register(WorkingTime)
class CalAvailableTimeAdmin(admin.ModelAdmin):
    #fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('teacher','working_from', 'working_till')
    list_filter = ('teacher','working_from', 'working_till')
    ordering = ('teacher','working_from', 'working_till')
    #search_fields = ('teacher', 'address')

@admin.register(Lesson)
class CalEventAdmin(admin.ModelAdmin):
    #fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('teacher','student', 'title', 'time_start', 'time_end')
    list_filter = ('teacher','student', 'time_start', 'time_end')
    ordering = ('teacher','student', 'title', 'time_start', 'time_end')
    #search_fields = ('teacher', 'address')


#admin.site.register(Profile, ProfileAdmin)
#admin.site.register(Event)
