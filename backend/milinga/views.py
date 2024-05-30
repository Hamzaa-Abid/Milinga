from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from dj_rest_auth.views import LogoutView
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.permissions import (AllowAny)
from dj_rest_auth.registration.serializers import VerifyEmailSerializer
from allauth.account.models import EmailAddress
from django.utils.translation import templatize, ugettext_lazy as _


# class TestAuthView(APIView):
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request, format=None):
#         return Response("Hello {0}!".format(request.user))


# class LogoutViewEx(LogoutView):
#     authentication_classes = (authentication.TokenAuthentication,)

# from django.http import HttpResponse
# def empty_view(request):
#     return HttpResponse('')


class ResendEmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
class ResendEmailVerification(GenericAPIView):
    serializer_class = ResendEmailVerificationSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        try:
            email_address = EmailAddress.objects.get(email__exact=email, verified=False)
            email_address.send_confirmation(self.request, True)
        except EmailAddress.DoesNotExist:
            pass

        return Response({'detail': _('Verification e-mail sent.')})