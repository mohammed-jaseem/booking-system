from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url='/login')
def index(request):
    return render(request, 'web/index.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "register.html")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already taken!")
            return render(request, "register.html")

        user = User.objects.create_user(username=email, password=password, first_name=name, email=email)
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, "register.html")

