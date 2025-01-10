from django.db import models
from users.models import User
from django.utils.timezone import now


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "customer_customer"
        verbose_name = "customer"
        verbose_name_plural = "customers"
        ordering = ["-id"]

    def __str__(self):
        return self.user.email
    

class Slider(models.Model):
    image = models.ImageField(upload_to='slider_image')
    title = models.CharField(max_length=255)
    short_description = models.TextField()

    class Meta:
        db_table = "slider"
        verbose_name = "slider"
        verbose_name_plural = "sliders"
        ordering = ["-id"]

    def __str__(self):
        return self.title
    


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images')
    max_attendees = models.PositiveIntegerField()
    time_date = models.DateTimeField()
    place = models.CharField(max_length=255)
    guests = models.TextField()
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Actual Ticket Amount")
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Offer Ticket Amount")
    enquiry_number = models.CharField()
    is_approved = models.BooleanField(default=False)
    is_actived = models.BooleanField(default=True)

    class Meta:
        db_table = "event"
        verbose_name = "event"
        verbose_name_plural = "events"
        ordering = ["-id"]

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    place = models.CharField(max_length=255)

    class Meta:
        db_table = "booking"
        verbose_name = "booking"
        verbose_name_plural = "bookings"
        ordering = ["-id"]

    def __str__(self):
        return self.event.name
    

    
