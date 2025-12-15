from django.db import models
from accounts.models import Account


# =========================
# Category Model
# =========================
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="اسم التصنيف"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


# =========================
# Product Model
# =========================
class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="اسم المنتج"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="التصنيف"
    )
    description = models.TextField(
        blank=True,
        verbose_name="الوصف"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


# =========================
# Order Model
# =========================
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('paid', 'مدفوع'),
        ('shipped', 'تم الشحن'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]

    customer = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="العميل"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name="حالة الطلب"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id}"


# =========================
# Order Item Model
# =========================
class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name="الطلب"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="سعر الوحدة"
    )

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.product} × {self.quantity}"
