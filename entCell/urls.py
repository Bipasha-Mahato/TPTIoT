from django.urls import path
from . import views

urlpatterns = [
    path('', views.entHome, name='ent-home')
    ]