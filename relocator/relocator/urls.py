"""
URL configuration for relocator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from relocator import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home),
    #  path('/autorisation/', autorisation),

    
    path('user/application/', userApplication, name = 'userApplication'),
    path('user/profile/', userProfile, name = 'userProfile'),
    path('user/relocatedEmployees/', userRelocatedEmployees, name = 'userRelocatedEmployees'),

    path('hr/', hr),
    path('hr/applications/', hrApplications, name = 'hrApplications'),
    #Возможно нужно изменить отображение по id (тип int) -- урок 3 5:00
    path('hr/employeeProfile/<int:appid>/', hrEmployeeProfile),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
