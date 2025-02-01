from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
]

from .settings import SERVER_DEBUG, MEDIA_URL, MEDIA_ROOT

if SERVER_DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
