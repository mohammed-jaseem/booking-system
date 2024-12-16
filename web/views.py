from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/login')
def index(request):
    sliders = Slider.objects.all()

    context = {
       'sliders': sliders
    }
    return render(request, 'web/index.html', context=context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password') 

        user = authenticate(request, email=email, password=password,) 

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))
        else:
            context = {
                'error':True,
                'message':'Invalid email or password'
            }
            return render(request, 'web/login.html', context=context)
    else:
        return render(request, 'web/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            first_name=first_name, 
            last_name=last_name,
            email=email,
            password=password,
            is_customer=True
        )
        user.save()
        customer = Customer.objects.create(
            user=user
        )
        customer.save()
        return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')
    
def logout(request):
    user = request.user
    auth_logout(request)

    return HttpResponseRedirect(reverse('web:login'))

def events(request):
    events = [
        {
            "name": "Tech Conference",
            "description": "A conference about the latest in technology.",
            "timeDate": "2024-12-25 10:00",
            "place": "Convention Center, City",
            "maxAttendees": 300,
            "actualAmount": 1500,
            "offerAmount": 1200,
        },
        {
            "name": "Music Festival",
            "description": "Join us for an evening of music and fun.",
            "timeDate": "2024-12-31 18:00",
            "place": "Open Grounds, Downtown",
            "maxAttendees": 500,
            "actualAmount": 2000,
            "offerAmount": 1800,
        },
    ]
    return render(request, 'web/create-form.html', {"events": events})





