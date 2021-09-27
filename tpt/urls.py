"""tpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
admin.autodiscover()

from django.urls import path, include

from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('', views.home_view, name='home'),
    path('home', views.home_view, name='home'),
    path('login', views.login_view, name='login'),
    path('profile', views.profile, name='profile'),
    path('report', views.report, name='Report-View'),
    path('report_all', views.report_all, name='report-all'),
    path('editProfile', views.editProfile, name='edit-profile'),
    path('register', views.register_view, name='register'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('devices', views.devices, name='devices'),
    path('<int:node_id>/', views.device_details, name='device_details'),
    path('logout', views.logout_view, name='logout'),
    path('api/data', views.get_data, name='api-data'),
    #path('api/chart/data', views.ChartData.as_view(), name='api-chart-data'),
    #path('api/chart/data1', views.ChartData1.as_view(), name='api-chart-data'),
    path('api/chart/temperature/<int:node_id>/', views.ChartData.as_view(), name='api-chart-data'),
    path('api/chart/humidity/<int:node_id>/', views.ChartData1.as_view(), name='api-chart-data'),

]
