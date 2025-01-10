from django.contrib import admin
from .models import Event
from .models import Customer, Slider, Event,Booking

admin.site.register(Customer)
admin.site.register(Event)
admin.site.register(Slider)
admin.site.register(Booking)






