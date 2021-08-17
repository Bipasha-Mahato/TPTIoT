from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField

class entVideo(models.Model):
    title = models.TextField(max_length=100)
    video = EmbedVideoField()  # same like models.URLField()

    def __str__(self):
        return self.title

class entNews(models.Model):
    title = models.TextField(max_length=280)
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title