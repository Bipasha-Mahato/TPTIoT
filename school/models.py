from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Class(models.Model):
    title = models.CharField(max_length=15)
    objects = models.Manager()

    def __str__(self):
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=30)
    course = models.ForeignKey(Class, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title

#####

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    file = models.FileField(upload_to='quiz-files', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quiz-detail', kwargs={'pk': self.pk})

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    file = models.FileField(upload_to='assignment-files', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assignment-detail', kwargs={'pk': self.pk})