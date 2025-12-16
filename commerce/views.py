from django.shortcuts import render


def home(request):
    """
    الصفحة الرئيسية للموقع
    """
    return render(request, 'home.html')
