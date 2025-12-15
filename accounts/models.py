from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone


# =========================
# Managers
# =========================
class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("يجب إدخال البريد الإلكتروني")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("يجب أن يكون المشرف موظفًا")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("يجب أن يكون المشرف بصلاحيات كاملة")

        return self.create_user(email, password, **extra_fields)


# =========================
# Role Model
# =========================
class Role(models.Model):
    """
    يحدد نوع الحساب (عميل – تاجر – مشرف – فريق)
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="اسم الدور"
    )
    description = models.TextField(
        blank=True,
        verbose_name="الوصف"
    )

    class Meta:
        verbose_name = "دور"
        verbose_name_plural = "الأدوار"

    def __str__(self):
        return self.name


# =========================
# Account Model (Custom User)
# =========================
class Account(AbstractBaseUser, PermissionsMixin):
    """
    نموذج الحساب الأساسي (بديل User)
    """
    email = models.EmailField(
        unique=True,
        verbose_name="البريد الإلكتروني"
    )
    full_name = models.CharField(
        max_length=150,
        verbose_name="الاسم الكامل"
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="الدور"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="موظف"
    )

    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name="تاريخ التسجيل"
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts',
        blank=True,
        verbose_name="المجموعات"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts',
        blank=True,
        verbose_name="الصلاحيات"
    )

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = "حساب"
        verbose_name_plural = "الحسابات"

    def __str__(self):
        return self.email


# =========================
# Profile Model
# =========================
class Profile(models.Model):
    """
    بيانات إضافية للحساب
    """
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="الحساب"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="رقم الهاتف"
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name="الصورة الشخصية"
    )

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

    def __str__(self):
        return f"الملف الشخصي - {self.account.email}"
