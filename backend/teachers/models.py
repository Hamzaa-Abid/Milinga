from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from subjects.models import Subject
User = get_user_model()
from djmoney.models.fields import MoneyField

#Teacher-Model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(max_length=1500, blank=True)
    videoUrl = models.URLField(blank=False, null=False)
    pricePerHour = MoneyField(max_digits=19, decimal_places=2, null=False, blank=False, default_currency='USD')
    acceptsBitcoins = models.BooleanField(default=False)
    acceptsFiat = models.BooleanField(default=True)

    objects=models.Manager()

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class TeacherTeaches(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='teaches', on_delete=models.CASCADE, blank=False, null=False, db_index=True,)
    subject = models.ForeignKey(Subject, related_name='teacher', on_delete=models.CASCADE, blank=False, null=False, db_index=True,)

    objects=models.Manager()
    def __str__(self):
        return self.subject.subject

    class Meta:
        unique_together = (('teacher', 'subject'))
