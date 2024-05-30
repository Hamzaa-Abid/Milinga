from django.contrib import admin
from .models import Review

@admin.register(Review)
class ProfileAdmin(admin.ModelAdmin):
    fields = (('reviewed', 'reviewer'),'rating', 'review')
    list_display = ('get_name_reviewed', 'get_name_reviewer', 'rating', 'review')
    list_filter = ('rating',)
    ordering = ('-rating',)
    search_fields = ('reviewed__first_name', 'reviewed__last_name', 'review',)

    def get_name_reviewed(self, obj):
        return obj.reviewed.first_name + ' ' + obj.reviewed.last_name

    def get_name_reviewer(self, obj):
        return obj.reviewer.first_name + ' ' + obj.reviewer.last_name


#admin.site.register(Review, ReviewAdmin)
#admin.site.register(Review)
