from django.shortcuts import render
from .models import Product


def home(request):
    """
    الصفحة الرئيسية للموقع
    """
    products = Product.objects.filter(is_active=True)

    return render(
        request,
        'home.html',
        {
            'products': products
        }
    )


def products_view(request):
    """
    صفحة عرض المنتجات
    """
    products = Product.objects.filter(is_active=True)

    return render(
        request,
        'commerce-te/products.html',
        {
            'products': products
        }
    )
