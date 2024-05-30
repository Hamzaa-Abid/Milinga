# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import DetailView, FormView, UpdateView
# from django.views import View

# from django.db import transaction

# from .models import Profile

# from django.db import models
# from .forms import UserForm, ProfileForm, ProfilePicForm
# from django.http import HttpResponse, Http404, JsonResponse

# from django.contrib.auth.mixins import LoginRequiredMixin

# from teachers.views import TeacherProfileInclude
# from teachers.forms import TeacherForm

# # class ProfileView(LoginRequiredMixin, FormView):
# #     # model = Profile
# #     template_name = 'profiles/profile.html'
# #     # form_class = ProfileForm
# #     # success_url = reverse_lazy('profile')

# #     def get(self, request, *args, **kwargs):
# #         user_form = UserForm(instance=request.user)
# #         user_form.prefix = 'user_form'
# #         profile_form = ProfileForm(instance=request.user.profile)
# #         profile_form.prefix = 'profile_form'

# #         form_data = {
# #             'user_form': user_form,
# #             'profile_form': profile_form,
# #             'profile_pic' : request.user.profile.profilePic,
# #         }
# #         TeacherProfileInclude(request).appendFormData(form_data)

# #         return render(request, 'profiles/profile.html', form_data)


# #     @transaction.atomic
# #     def post(self, request, *args, **kwargs):
# #         user_form = UserForm(self.request.POST, prefix='user_form')
# #         profile_form = ProfileForm(self.request.POST, prefix='profile_form')
# #         teacher_profile_include = TeacherProfileInclude(request)
        
# #         bFormDataSaved = False
# #         bFormDataError = True
# #         if user_form.is_valid() and profile_form.is_valid() and teacher_profile_include.is_valid():
# #             #get cleaned data
# #             user_data = user_form.cleaned_data
# #             profile_data = profile_form.cleaned_data

# #             #Speichere User
# #             user = self.request.user
# #             user.first_name = user_data['first_name']
# #             user.last_name = user_data['last_name']
# #             user.save()

# #             #Speichere Profil
# #             user.profile.description_short = profile_data['description_short']
# #             user.profile.description = profile_data['description']
# #             user.profile.isTeacher = teacher_profile_include.getIsTeacher()
# #             user.profile.save()

# #             #Speichere Teacher
# #             teacher_profile_include.saveFormData()
# #             bFormDataSaved = True
# #             bFormDataError = False

# #         form_data = {
# #             'user_form': user_form,
# #             'profile_form': profile_form,
# #             'profile_pic' : request.user.profile.profilePic,
# #             'form_data_saved': bFormDataSaved,
# #             'form_data_error': bFormDataError,
# #         }
# #         teacher_profile_include.appendFormData(form_data)

# #         return render(request, 'profiles/profile.html', form_data)

# # class UpdateProfilePic(LoginRequiredMixin, View):
# #     def post(self, request):
# #         form = ProfilePicForm(self.request.POST, self.request.FILES)
# #         if form.is_valid():
# #             request.user.profile.profilePic = form.cleaned_data['profilePic']
# #             request.user.profile.save()
# #             return JsonResponse({
# #                 'image_url' : request.user.profile.profilePic.url
# #             })
# #         else:
# #             raise Http404(form.errors)

# from milinga.Auth import tokenLogin
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator

# # @method_decorator(csrf_exempt, name='dispatch')
# class UpdateProfilePic(View):
#     def post(self, request):
#         user = tokenLogin(request.POST['token'])
#         user.profile.profilePic = request.POST['profilePic']
#         user.profile.profilePic.save()
#         return JsonResponse({
#             'image_url' : request.user.profile.profilePic.url
#         })
