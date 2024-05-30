# import json
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.views.generic import TemplateView
# from django.http import HttpResponse
# from . import Calendar
# from .models import Lesson


# class WorkingTime(LoginRequiredMixin, TemplateView):
#     template_name = 'calendarapp/WorkingTime.html'

#     def get_context_data(self, *args, **kwargs):
#        context = super().get_context_data(*args, **kwargs)
#        context['working_times'] = Calendar.getWorkingTimes(teacher=self.request.user)
#        context['my_bookings'] = Calendar.getTeacherEvents(teacher=self.request.user)
#        return context

# class BookLesson(LoginRequiredMixin, TemplateView):
#     template_name = 'calendarapp/BookLesson.html'

#     def get_context_data(self, *args, **kwargs):
#        context = super().get_context_data(*args, **kwargs)
#        oTeacherAvailability = Calendar.getTeacherAvailabilityForStudent(teacher=kwargs['pk'], student=self.request.user)
#        context['working_times'] = oTeacherAvailability['working_times']
#        context['teacher_events'] = oTeacherAvailability['teacher_events']
#        context['my_lessons'] = Calendar.getMyLessonsWithTeacher(user=self.request.user, teacher=kwargs['pk'])
#        return context

# # class AjaxMyAvailability(LoginRequiredMixin, View):
# #     def post(self, request):
# #         oAvailabililty = json.loads(str(request.POST['available_times']))
# #         Calendar.saveAvailabilityFromTimestamps(
# #             user = request.user,
# #             availability = oAvailabililty
# #         )

# #         return HttpResponse("ok")

# # class AjaxTeacherBookEvents(View):
# #     def post(self, request, pk):
# #         oEventsToBook = json.loads(str(request.POST['events']))
# #         Calendar.bookEventsFromTimestamps(
# #             user = request.user,
# #             teacher = pk,
# #             events = oEventsToBook,
# #         )

# #         return HttpResponse("ok")

# # class AjaxTeacherBookEvent(View):
# #     def post(self, request, pk):
# #         oEventToBook = json.loads(str(request.POST['event']))
# #         Calendar.bookEventFromTimestamps(
# #             user = request.user,
# #             teacher_id = pk,
# #             event = oEventToBook,
# #         )

# #         return HttpResponse("ok")

# # class AjaxTeacherAcceptsEvent(View):
# #     def post(self, request):
# #         oEvent = json.loads(str(request.POST['event']))
# #         oCalEvent = CalEvent.objects.get(teacher = request.user, id=oEvent['eventId'])
# #         oCalEvent.teacherConfirmed = True
# #         oCalEvent.save()
# #         return HttpResponse("ok")

# # class AjaxTeacherRejectsEvent(View):
# #     def post(self, request):
# #         oEvent = json.loads(str(request.POST['event']))
# #         CalEvent.objects.get(teacher = request.user, id=oEvent['eventId']).delete()
# #         return HttpResponse("ok")
