"""
URL configuration for saad4 project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Project Apps
    path('accounts/', include('accounts.urls')),
    path('store/', include('commerce.urls')),
    path('control/', include('control.urls')),
]


# =========================
# Media files (Development only)
# =========================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
