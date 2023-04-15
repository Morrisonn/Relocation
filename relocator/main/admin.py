from django.contrib import admin
from .models import *

admin.site.site_header = "АДМИНИСТРАТОР"

class LocationUser(admin.ModelAdmin):
    list_display = ('id', 'login','password', 'role')
    list_display_links = ('id', 'login','password', 'role')
    search_fields = ('id', 'login','password', 'role')
    list_filter = ('login', 'role')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'country','city', 'description')
    list_display_links = ('id', 'country','city', 'description')
    search_fields = ('id', 'country','city')
    list_filter = ('country','city')

admin.site.register(User, LocationUser)
admin.site.register(Location, LocationAdmin)

