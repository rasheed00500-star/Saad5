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

        # التحقق من تطابق كلمات المرور
        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("register")

        # التحقق من البريد
        if Account.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم مسبقًا")
            return redirect("register")

        # إنشاء المستخدم
        user = Account.objects.create_user(
            email=email,
            password=password1,
            full_name=full_name
        )

        messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول")
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
            return redirect("home")  # غيّرها حسب مشروعك
        else:
            messages.error(request, "البريد الإلكتروني أو كلمة المرور غير صحيحة")
            return redirect("login")

    return render(request, "accounts-te/login.html")
