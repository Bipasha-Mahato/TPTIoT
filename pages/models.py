from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.TextField(blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'


class node_details(models.Model):
    node_id = models.AutoField(primary_key=True)
    board = models.TextField(blank = True)
    has_camera = models.BooleanField()
    last_active = models.DateTimeField(null=True, blank=True)


class sensor_data(models.Model):
    id = models.AutoField(primary_key=True)
    node_id = models.ForeignKey(node_details, on_delete=models.CASCADE)
    humidity = models.FloatField()
    temperature = models.FloatField()
    date_inserted = models.DateTimeField(auto_now=True)
