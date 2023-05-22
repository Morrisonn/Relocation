from relocator import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import *
from main.admin import MyAdminSite

my_admin_site = MyAdminSite(name="myadmin")

urlpatterns = [
    path("myadmin/", my_admin_site.urls),
    path("admin/", admin.site.urls, name="admin"),
    path("", begin, name="begin"),
    #  path('/autorisation/', autorisation),
    path("autorization/", include("main.urls")),
    path("autorization/logout", logout_view, name="logout_view"),
    path("user/", user, name="user"),
    path("user/application/", userApplication, name="userApplication"),
    path("user/application/new", newUserApplication, name="newUserApplication"),
    path("user/profile/", userProfile, name="userProfile"),
    path("user/account/", userAccount, name="userAccount"),
    path(
        "user/relocatedEmployees/",
        userRelocatedEmployees,
        name="userRelocatedEmployees",
    ),
    path("user/news/", userNews, name="userNews"),
    path("hr/", hr, name="hr"),
    path("hr/applications/", hrApplications, name="hrApplications"),
    path("hr/applications/userPage/<int:userId>/", hr_userPage, name="hr_userPage"),
    path("hr/news/", hrNews, name="hrNews"),
    path("hr/applications/userPage/<int:userId>/profile/", hr_userProfile, name="hr_userProfile"),
    # Возможно нужно изменить отображение по id (тип int) -- урок 3 5:00
    # path("hr/employeeProfile/<int:appid>/", hrEmployeeProfile),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
