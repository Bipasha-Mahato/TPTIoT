from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='tribeguru-home'),
    path('testpage/', views.testpage, name='testpage'),
    path('meet/', views.meet, name='tg-meet')
    ]