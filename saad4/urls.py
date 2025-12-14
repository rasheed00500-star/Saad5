"""
URL configuration for saad4 project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Project Apps
    path('accounts/', include('accounts.urls')),
    path('store/', include('commerce.urls')),
    path('control/', include('control.urls')),
]
