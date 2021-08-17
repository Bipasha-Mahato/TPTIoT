from django.db import models

# Create your models here.
from django.utils import timezone

class voiceQuery(models.Model):
    audio = models.FileField(upload_to='voice-queries/')
    date_posted = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return f'New query on {self.date_posted}'

class vQuery(models.Model):
    complainant_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    complaint = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.complainant_name} - {self.date_posted}'