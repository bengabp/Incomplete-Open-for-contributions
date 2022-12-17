from django.core.files.storage import FileSystemStorage
from django.db.models import ImageField
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.db.utils import IntegrityError
from django.contrib.auth import login, logout, get_user

from .models import DevhubAccount


def handle_login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'devhubmain/auth/login.html')

    email = request.POST.get("email")
    password = request.POST.get("password")

    # try:
    user = DevhubAccount.objects.filter(email=email).first()
    if user:
        print(user, user.email)
        if not check_password(password, user.password):
            messages.error(request, "Incorrect Password!")
            return redirect('login')
        login(request, user)
        messages.success(request, f"Logged in successfully as {user.username}")
        return redirect('home')
    else:
        messages.error(request, "User does not exist!")
        return redirect('login')


def handle_user_registration(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'devhubmain/auth/register.html')

    username = request.POST.get("username")
    email = request.POST.get("email")
    password1 = request.POST.get("password-1")
    password2 = request.POST.get("password-2")
    profile_picture = request.FILES.get("profile-picture")

    if len(username) < 5:
        messages.error(request, "Username is too short")
        return redirect('register')
    elif len(password1) < 8:
        messages.error(request, "Passwords must be more than 7 characters")
        return redirect('register')
    elif password1 != password2:
        messages.error(request, "Passwords did not match")
        return redirect('register')
    elif not profile_picture:
        messages.error(request, "Invalid profile picture")
        return redirect('register')
    elif DevhubAccount.objects.filter(username=username).first():
        messages.error(request, "Username already taken")
        return redirect("register")
    elif DevhubAccount.objects.filter(email=email).first():
        messages.error(request, "Account already exists , please login")
        return redirect("register")

    # fss = ImageField()
    # file = fss.save(profile_picture.name, profile_picture)
    # file_url = fss.url(file)
    # print(file_url)
    new_devhub_account = DevhubAccount(username=username, email=email, password=make_password(password1),
                                       profile_pic=profile_picture,
                                       profile_picture_web_path="", github_profile_url="",
                                       linkedin_profile_url="")
    new_devhub_account.save()
    return redirect('login')


def handle_logout(request):
    if request.method == "POST":
        password = request.POST.get("password-confirm")
        if request.user:
            if check_password(password, request.user.password):
                logout(request)
                messages.success(request, "Successfully logged out!")
                return redirect("home")
            messages.error(request, "Incorrect Password !")
            return redirect("logout")
        messages.error(request, "Logout Error, Invalid User")
        return redirect("logout")
    return render(request, "devhubmain/auth/confirm-logout.html")


def handle_user_verification(request):
    if request.method == "GET":
        return HttpResponse("Verification Page")
    return HttpResponse("Process post request")
