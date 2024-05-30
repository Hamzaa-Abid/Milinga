from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.WorkingTime.as_view(), name='working_time'),
    path('Teacher/<int:pk>/', views.BookLesson.as_view(), name='book_lesson'),
]
