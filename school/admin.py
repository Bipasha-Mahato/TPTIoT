from django.contrib import admin
from .models import Class, Subject, Quiz, Assignment

# Register your models here.
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Assignment)