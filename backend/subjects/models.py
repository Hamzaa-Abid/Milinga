from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=50, db_index=True, null=True, blank=False, unique=True)

    objects=models.Manager()
    
    def __str__(self):
        return self.subject
