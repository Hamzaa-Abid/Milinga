from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')

class ProfileForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':10}), label=_('Long description'))
    class Meta:
        model = Profile
        exclude = ('user', 'profilePic', 'isTeacher')

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilePic',)
