from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import login,logout


def handle_login(request):
    if request.method == "GET":
        print("Logged in : ",request.user.username)
        return render(request,"ifit_main/auth/login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")

    # Get user
    try:
        user  = User.objects.get(username=username)
        password_correct = check_password(password,user.password)
        print("User:",user,password_correct)
        if not password_correct:
            return HttpResponse("wrong credentials !")
        login(request,user)
        return HttpResponse(f"Loggedin successful as {user.username}")
    except:
        return HttpResponse("No records found")


def handle_register(request):
    if request.method == "GET":
        print("Logged in : ",request.user.username)
        return render(request,"ifit_main/auth/register.html")

    username = request.POST.get("username")
    password = request.POST.get("password")
    password_confirm = request.POST.get("password-confirm")

    if passsword != password_confirm:
        return HttpResponse("Passwords are not thesame !")

    try:
        new_user = User(username=username,password = make_password(password))
        new_user.save()
        print("New user:",new_user)
        login(new_user)
        return HttpResponse("Registration successful")
    except:
        return HttpResponse("User already exists")


def handle_logout(request):
    logout(request)
    return HttpResponse("Logged out successfully")