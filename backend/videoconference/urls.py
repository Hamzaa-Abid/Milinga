from django.urls import path, include
from . import views

urlpatterns = [
    path('f/<video_id>/', views.VideoConferenceRedirectView.as_view(), name='start_video_conference'),
]