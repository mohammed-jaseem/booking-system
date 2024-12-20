from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='/login')
def index(request):
    events = Event.objects.filter(is_approved=True)
    sliders = Slider.objects.all()

    context = {
       'sliders': sliders,
        'events': events
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


def create_event(request):
    events = Event.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        max_attendees = request.POST.get('max_attendees')
        time_date = request.POST.get('time_date')
        place = request.POST.get('place')
        guests = request.POST.get('guests')
        actual_amount = request.POST.get('actual_amount')
        offer_amount = request.POST.get('offer_amount')
        enquiry_number = request.POST.get('enquiry_number')

        event = Event.objects.create(
            name=name,
            description=description,
            image=image,
            max_attendees=max_attendees,
            time_date=time_date,
            place=place,
            guests=guests,
            actual_amount=actual_amount,
            offer_amount=offer_amount,
            enquiry_number=enquiry_number,
        )
        event.save()

        return redirect('web:index')
    
    context = {
        events
    }

    return render(request, 'web/create-form.html', context=context)

def detailes(request, id):
    event = Event.objects.get(id=id)

    context = {
        'event': event
    }

    return render(request, 'web/detailes.html', context=context)

def booking(request):
    return render(request, 'web/booking.html',)







