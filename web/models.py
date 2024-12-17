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

    class Meta:
        db_table = "event"
        verbose_name = "event"
        verbose_name_plural = "events"
        ordering = ["-id"]

    def __str__(self):
        return self.name

    
