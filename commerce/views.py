from django.shortcuts import render


def home(request):
    """
    الصفحة الرئيسية للمتجر
    """
    return render(request, 'commerce/home.html')
