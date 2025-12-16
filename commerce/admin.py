from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Order, OrderItem


# =========================
# Category Admin
# =========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


# =========================
# Product Admin
# =========================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active', 'product_image')
    list_filter = ('is_active', 'category')
    search_fields = ('name',)
    ordering = ('name',)

    # ترتيب الحقول داخل صفحة الإضافة / التعديل
    fieldsets = (
        ('معلومات المنتج', {
            'fields': ('name', 'category', 'description', 'price')
        }),
        ('صورة المنتج', {
            'fields': ('image',)
        }),
        ('الحالة', {
            'fields': ('is_active',)
        }),
    )

    # عرض الصورة داخل الجدول
    def product_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 6px;" />',
                obj.image.url
            )
        return "—"

    product_image.short_description = "الصورة"


# =========================
# Order Item Inline
# =========================
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


# =========================
# Order Admin
# =========================
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'customer__email')
    inlines = [OrderItemInline]
