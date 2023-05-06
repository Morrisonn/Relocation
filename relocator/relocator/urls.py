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
from django.urls import path, include
from main.views import *
from main.admin import MyAdminSite

my_admin_site = MyAdminSite(name='myadmin')

urlpatterns = [
    path('myadmin/', my_admin_site.urls),
    path('admin/', admin.site.urls, name='admin'),

    path('', begin, name = 'begin'),
    #  path('/autorisation/', autorisation),

    path('autorization/', include('main.urls')),
    path('autorization/logout', logout_view, name = "logout_view"),

    path('user/', user, name='user'),
    path('user/application/', userApplication, name = 'userApplication'),
    path('user/application/new', newUserApplication, name = 'newUserApplication'),
    path('user/profile/', userProfile, name = 'userProfile'),
    path('user/relocatedEmployees/', userRelocatedEmployees, name = 'userRelocatedEmployees'),
    path('user/news/', userNews, name = 'userNews'),

    path('hr/', hr, name='hr'),
    path('hr/applications/', hrApplications, name = 'hrApplications'),
    #Возможно нужно изменить отображение по id (тип int) -- урок 3 5:00
    path('hr/employeeProfile/<int:appid>/', hrEmployeeProfile),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
