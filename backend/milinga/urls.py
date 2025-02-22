"""milinga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from . import views

# from .views import TestAuthView, LogoutViewEx
# from rest_auth.views import LoginView
# from rest_auth.registration.views import RegisterView
  
urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('test_auth/', TestAuthView.as_view(), name='test_auth', ),
    # path('rest-auth/logout/', LogoutViewEx.as_view(), name='rest_logout', ),
    # path('rest-auth/login/', LoginView.as_view(), name='rest_login', ),
    re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(template_name='index.html'),
        name='account_confirm_email'),
    path('password-reset/<uidb64>/<token>/', TemplateView.as_view(template_name='index.html'), name='password_reset_confirm'),
    path('rest-auth/resend-verification-email/', views.ResendEmailVerification.as_view(), name='rest_resend_verification_email'),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls'), ),

    # path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    # path('updateProfilePic/', profilesViews.UpdateProfilePic.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.append(path('<path:resource>', TemplateView.as_view(template_name='index.html')))