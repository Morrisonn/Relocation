from django.urls import path, include
from relocator import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)