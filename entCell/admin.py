from django.contrib import admin

# Register your models here.
from embed_video.admin import AdminVideoMixin
from .models import entVideo, entNews

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(entVideo, MyModelAdmin)
admin.site.register(entNews)