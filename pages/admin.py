from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import sensor_data
from .models import node_details

admin.site.register(Profile)
admin.site.register(sensor_data)
admin.site.register(node_details)
