from django.db import models
from accounts.models import Account


class StoreSettings(models.Model):
    """
    إعدادات عامة للمتجر (No-Code Friendly)
    """
    store_name = models.CharField(max_length=150)
    currency = models.CharField(max_length=10, default='SAR')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.store_name


class SystemConfig(models.Model):
    """
    إعدادات تشغيلية عامة
    """
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key


class AuditLog(models.Model):
    """
    تتبع العمليات (مهم جدًا للوحة التحكم)
    """
    actor = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action
