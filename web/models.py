from django.db import models
from users.models import User


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
    name = models.CharField(max_length=255, verbose_name="Event Name")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='event_images/', blank=True, null=True, verbose_name="Event Image")
    max_attendees = models.PositiveIntegerField(verbose_name="Max Attendees")
    time_date = models.DateTimeField(verbose_name="Event Date & Time")
    place = models.CharField(max_length=255, verbose_name="Event Place")
    guests = models.TextField(blank=True, null=True, verbose_name="Guest Names (Comma-separated)")
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Actual Ticket Amount")
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Offer Ticket Amount")
    enquiry_number = models.CharField(max_length=15, verbose_name="Enquiry Number")


    class Meta:
        db_table = "event"
        verbose_name = "event"
        verbose_name_plural = "events"
        ordering = ["-id"]


    def __str__(self):
        return self.name

    
