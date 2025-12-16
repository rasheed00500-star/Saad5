from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Account


# =========================
# إنشاء حساب
# =========================
def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("register")

        if Account.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم بالفعل")
            return redirect("register")

        user = Account.objects.create_user(
            email=email,
            password=password1,
            full_name=full_name
        )

        login(request, user)
        return redirect("login")

    return render(request, "accounts-te/register.html")


# =========================
# تسجيل الدخول
# =========================
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("login")
        else:
            messages.error(request, "بيانات الدخول غير صحيحة")
            return redirect("login")

    return render(request, "accounts-te/login.html")
