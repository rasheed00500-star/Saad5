from django.db import models
from accounts.models import Account


# =========================
# Store Settings Model
# =========================
class StoreSettings(models.Model):
    """
    إعدادات عامة للمتجر (No-Code Friendly)
    """
    store_name = models.CharField(
        max_length=150,
        verbose_name="اسم المتجر"
    )
    currency = models.CharField(
        max_length=10,
        default='SAR',
        verbose_name="العملة"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )

    class Meta:
        verbose_name = "إعدادات المتجر"
        verbose_name_plural = "إعدادات المتجر"

    def __str__(self):
        return self.store_name


# =========================
# System Config Model
# =========================
class SystemConfig(models.Model):
    """
    إعدادات تشغيلية عامة
    """
    key = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="المفتاح"
    )
    value = models.TextField(
        verbose_name="القيمة"
    )

    class Meta:
        verbose_name = "إعداد نظام"
        verbose_name_plural = "إعدادات النظام"

    def __str__(self):
        return self.key


# =========================
# Audit Log Model
# =========================
class AuditLog(models.Model):
    """
    تتبع العمليات (مهم جدًا للوحة التحكم)
    """
    actor = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="المنفذ"
    )
    action = models.CharField(
        max_length=255,
        verbose_name="الإجراء"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ التنفيذ"
    )

    class Meta:
        verbose_name = "سجل العمليات"
        verbose_name_plural = "سجلات العمليات"
        ordering = ['-created_at']

    def __str__(self):
        return self.action
