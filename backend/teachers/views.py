# from django.core.paginator import Paginator
# from django.shortcuts import render

# from profiles.models import Profile
# from teachers.models import Teacher as Teacher
# from teachers.models import TeacherTeaches as TeacherTeaches
# from teachers.forms import TeacherForm

# from subjects.models import Subject
# from teachers.forms import TeacherTeachesFormSet

# from django.db import transaction

# from django.views import View

# # from silk.profiling.profiler import silk_profile

# class TeacherList(View):
#     # @silk_profile(name='View Teacher List')
#     def get(self, request):
#         filter_subject_id = request.GET.get('subject')
#         try:
#             Subject.objects.get(id=filter_subject_id)
#         except Subject.DoesNotExist:
#             filter_subject_id = Subject.objects.get(subject_en='English').id
#         teachers = Teacher.objects.prefetch_related('teaches').select_related('user__profile').filter(teaches__subject_id=filter_subject_id).filter(user__profile__isTeacher=True)
#         # teacherprofiles = Profile.objects.filter(isTeacher=True).select_related('user__teacher__teaches__subject').filter(user__teacher__teaches__subject__subject='English')#.select_related('user__reviews')
#         #import pdb;pdb.set_trace()
#         teacher_data_list = []
#         for teacher in teachers.iterator():
#             teacher_data = {}
#             teacher_data['first_name'] = teacher.user.first_name
#             teacher_data['last_name'] = teacher.user.last_name
#             teacher_data['teaches'] = []
#             for teacherteaches in teacher.teaches.iterator():
#                 teacher_data['teaches'].append(teacherteaches.subject.subject)
#             teacher_data['description_short'] = teacher.user.profile.description_short
#             teacher_data['videoUrl'] = teacher.videoUrl
#             teacher_data['profilePic'] = teacher.user.profile.profilePic
#             teacher_data['user_id'] = teacher.user.id
#             # reviews = user.reviews.all()
#             # if len(reviews) > 0:
#             #     rating = sum(item.rating for item in reviews) / len(reviews)
#             # else:
#             #     rating = -1
            
#             #star-rating:
#             # teacher_data['rating'] = round(rating*2, 0)/2
#             teacher_data['rating'] = round(4.2*2, 0)/2
#             teacher_data['rating_full_count'] = range(int(teacher_data['rating']))
#             teacher_data['rating_half_bool'] = teacher_data['rating'] % 1 == 0.5

#             teacher_data_list.append(teacher_data)


#         paginator = Paginator(teacher_data_list, 10) # Show 25 contacts per page

#         page = request.GET.get('page')
#         teachers = paginator.get_page(page)

#         return render(request, 'teachers/teacher_list.html', {
#             'subjects' : Subject.objects.order_by('subject').all(),
#             'subjects_selected_id' : filter_subject_id,

#             'teachers' : teachers,
#         })

#     # def post(self, request):

# # import json
# # from django.core import serializers
# # from django.http import HttpResponse
# # class AjaxTeacherListAll(View):
# #     def get(self, request):
# #         oTeachers = Teacher.objects.prefetch_related('teaches').select_related('user__profile').all()
# #         return HttpResponse(serializers.serialize('json', oTeachers), content_type='application/json')


# class TeacherProfileInclude:
#     def __init__(self, request):
#         self.request = request
#         self.teacher_form = None
#         self.teacher_teaches_formset = None

#     def appendFormData(self, form_data):
#         if self.request.method == 'GET':
#             if(hasattr(self.request.user, 'teacher')):
#                 teacher_form = TeacherForm(initial={'isTeacher' : self.request.user.profile.isTeacher},instance=self.request.user.teacher)
#             else:
#                 teacher_form = TeacherForm()
#             teacher_teaches_formset = TeacherTeachesFormSet(
#                 initial=[{'subject': teacher_teaches.subject} for teacher_teaches in TeacherTeaches.objects.filter(teacher_id=self.request.user.id)],
#                 prefix='teacher_teaches_formset',
#             )

#         elif self.request.method == 'POST':
#             teacher_form = self.teacher_form
#             teacher_teaches_formset = self.teacher_teaches_formset
#             teacher_teaches_formset.forms = [form for form in self.teacher_teaches_formset.forms if form.cleaned_data.get('subject') != None]
#             # for form in teacher_teaches_formset.forms:
#             #     if form.cleaned_data['subject'] == None:
#             #         form.remove()

    
#         teacher_form.prefix = 'teacher_form'
#         form_data['teacher_form'] = teacher_form
#         form_data['teacher_teaches_formset'] = teacher_teaches_formset
        
#     @transaction.atomic
#     def saveFormData(self):
#         self.is_valid()

#         #Teacher-Profil speichern
#         teacher_data = self.teacher_form.cleaned_data
#         Teacher.objects.update_or_create(
#             user = self.request.user,
#             defaults = {
#                 'user' : self.request.user,
#                 'pricePerHour' : teacher_data['pricePerHour'],
#                 'videoUrl' : teacher_data['videoUrl'],
#             }
#         )

#         #Teacher-Unterrichtsfächer speichern
#         TeacherTeaches.objects.filter(teacher_id=self.request.user.id).delete()
#         oBulkTeacherTeaches = []
#         for teacher_teaches_form in self.teacher_teaches_formset:
#             if teacher_teaches_form.is_valid():
#                 oSubject = teacher_teaches_form.cleaned_data.get('subject')
#                 if oSubject != None: 
#                     oBulkTeacherTeaches.append(TeacherTeaches(
#                         teacher_id=self.request.user.id,
#                         subject=oSubject
#                     ))
#         if (len(oBulkTeacherTeaches) > 0):
#             TeacherTeaches.objects.bulk_create(oBulkTeacherTeaches)

#     def is_valid(self):
#         if self.teacher_form is None:
#             self.teacher_form = TeacherForm(self.request.POST, prefix='teacher_form')
#         if self.teacher_teaches_formset is None:
#             self.teacher_teaches_formset = TeacherTeachesFormSet(self.request.POST, prefix='teacher_teaches_formset')
#         bTeacherFormValid = self.teacher_form.is_valid()
#         bTeacherTeachesFormSetValid = self.teacher_teaches_formset.is_valid()
#         return bTeacherFormValid and bTeacherTeachesFormSetValid

#     def getIsTeacher(self):
#         return self.teacher_form.cleaned_data['isTeacher']
