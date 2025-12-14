from django.contrib import admin
from .models import StoreSettings, SystemConfig, AuditLog


@admin.register(StoreSettings)
class StoreSettingsAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'currency', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('store_name',)


@admin.register(SystemConfig)
class SystemConfigAdmin(admin.ModelAdmin):
    list_display = ('key',)
    search_fields = ('key',)


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('actor', 'action', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('action', 'actor__email')
    ordering = ('-created_at',)
