from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Credits(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, db_index=True,related_name='hasCredits',)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, db_index=True,related_name='owesCredits',)
    credits = models.IntegerField(blank=False, null=False)
    date = models.DateTimeField()

    # class Meta:
    #     unique_together = (('userReviewer', 'userReviewed'))
