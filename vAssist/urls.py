from django.urls import path
from . import views

urlpatterns = [
    path('', views.assistHome, name='assist-home'),
    path('upload/', views.assistHome, name='assist-upload')
    ]