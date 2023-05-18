from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "АДМИНИСТРАТОР"


class LocationUser(admin.ModelAdmin):
    list_display = ("id", "username", "password", "role")
    list_display_links = ("id", "username", "password", "role")
    search_fields = ("id", "username", "password", "role")
    list_filter = ("username", "role")


class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "city", "description")
    list_display_links = ("id", "country", "city", "description")
    search_fields = ("id", "country", "city")
    list_filter = ("country", "city")


# admin.site.register(User, LocationUser)
admin.site.register(Location, LocationAdmin)
admin.site.register(News)


class MyAdminSite(AdminSite):
    logout_url = "/autorization/login/"

class CustomUserCreationForm(UserCreationForm):
    role = forms.CharField(label='Роль (Сотрудник-0, Hr-1)')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')
        labels = {
            'username': _('Имя пользователя'),
            'password1': _('Пароль'),
            'password2': _('Подтверждение пароля'),
            'role': _('Роль'),
        }

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

admin.site.register(User, CustomUserAdmin)
