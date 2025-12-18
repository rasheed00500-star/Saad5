from django.shortcuts import render
from django.shortcuts import render


def home(request):
    """
    الصفحة الرئيسية للموقع
    """
    return render(request, 'home.html')


def products_view(request):
    """
    صفحة عرض المنتجات
    """
    return render(request, 'commerce-te/products.html')
