from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Account


# =========================
# إنشاء حساب
# =========================
def register_view(request):
    # إذا كان المستخدم مسجّل، لا يدخل صفحة التسجيل
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # التحقق من الحقول
        if not full_name or not email or not password1 or not password2:
            messages.error(request, "جميع الحقول مطلوبة")
            return redirect("register")

        # تطابق كلمات المرور
        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين")
            return redirect("register")

        # البريد مستخدم
        if Account.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم مسبقًا")
            return redirect("register")

        # إنشاء المستخدم
        Account.objects.create_user(
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
    # إذا كان المستخدم مسجّل، لا يدخل صفحة الدخول
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password")

        # التحقق من وجود المستخدم
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            messages.error(request, "البريد الإلكتروني أو كلمة المرور غير صحيحة")
            return redirect("login")

        # التحقق من كلمة المرور
        if not user.check_password(password):
            messages.error(request, "البريد الإلكتروني أو كلمة المرور غير صحيحة")
            return redirect("login")

        # التحقق من تفعيل الحساب
        if not user.is_active:
            messages.error(request, "هذا الحساب غير نشط")
            return redirect("login")

        # تسجيل الدخول
        login(request, user)

        # الانتقال للصفحة الرئيسية
        return redirect("/")

    return render(request, "accounts-te/login.html")


# =========================
# تسجيل الخروج
# =========================
@require_POST
def logout_view(request):
    logout(request)
    return redirect("/")
