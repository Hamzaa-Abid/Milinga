from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

class WorkingTime(models.Model):
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='working_times',
        db_index=True,
    )

    working_from = models.DateTimeField(db_index=True)
    working_till = models.DateTimeField(db_index=True)

    objects=models.Manager()


class Lesson(models.Model):
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cal_events_got_booked',
        db_index=True,
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cal_events_has_booked',
        db_index=True,
    )

    title = models.TextField()
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    studentConfirmed = models.BooleanField()
    teacherConfirmed = models.BooleanField()
    videoConferenceId = models.CharField(null=False, blank=False, unique=True, max_length=50)
    
    objects=models.Manager()