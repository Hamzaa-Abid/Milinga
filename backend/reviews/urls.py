from django.urls import path#, include
#from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('<int:pk>/', views.ReviewView.as_view(), name='rate_user'),
]
