from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.TeacherList.as_view(), name='searchteacher'),
    # path('all/', views.AjaxTeacherListAll.as_view(), name='getteachers_ajax'),
]
