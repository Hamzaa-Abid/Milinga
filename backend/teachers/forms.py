from django import forms
from .models import Teacher
from django.utils.translation import gettext_lazy as _
from django.forms import formset_factory
from .models import TeacherTeaches as TeacherTeachesModel
from subjects.models import Subject
from djmoney.forms.fields import MoneyField

class TeacherForm(forms.ModelForm):
    isTeacher = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'isTeacherCheckbox'}), label=_('I am a Teacher'))
    pricePerHour = MoneyField(required=False, label=_('Price per lesson'))
    videoUrl = forms.URLField(required=False, label=_('Video URL'))
    
    class Meta:
        model = Teacher
        fields = ('pricePerHour', 'videoUrl',)

    def clean(self):
        cleaned_data = super().clean()
        isTeacher = cleaned_data.get('isTeacher')
        videoUrl = cleaned_data.get('videoUrl')
        pricePerHour = cleaned_data.get('pricePerHour')

        if isTeacher:
            if videoUrl.strip() == '':
                self.add_error('videoUrl', _('A Video URL is required, if you are a teacher!'))
            if pricePerHour == None:
                self.add_error('pricePerHour', _('Please enter a price!'))

class TeacherTeachesForm(forms.ModelForm):
    subject = forms.ModelChoiceField(Subject.objects.all(), empty_label=_('Choose a subject you teach!'), required=False)

    class Meta:
        model = TeacherTeachesModel
        fields = ('subject',)

TeacherTeachesFormSet = formset_factory(TeacherTeachesForm, extra=0)