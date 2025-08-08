from django.db import models
from django.conf import settings
from apps.home.models import Cab,Hotels
from apps.destinations.models import Destination
from apps.home.models import AbstractDateTimeFieldBaseModel

# Create your models here.

class Webinar(AbstractDateTimeFieldBaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    facilities = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    recording_url = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    # Razorpay fields
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="created_webinars")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="modified_webinars")




# class Webinar(AbstractDateTimeFieldBaseModel):
#     cab = models.ForeignKey(Cab,on_delete=models.SET_NULL,blank=True, null=True,related_name='trip_cab')
#     hotel = models.ForeignKey(Hotels,on_delete=models.SET_NULL,blank=True, null=True,related_name='trip_hotel')
#     destination = models.ForeignKey(Destination,on_delete=models.SET_NULL,blank=True, null=True,related_name='trip_destination_and_activities')

#     title = models.CharField(max_length=200,blank=True, null=True)
#     slug = models.SlugField(unique=True, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     date = models.DateTimeField(blank=True, null=True)
   
#     price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
#     link = models.URLField(blank=True, null=True)
#     image = models.ImageField(upload_to='webinars/', blank=True, null=True)
#     duration_minutes = models.PositiveIntegerField(blank=True, null=True)
#     capacity = models.PositiveIntegerField(blank=True, null=True)
#     registration_deadline = models.DateTimeField(blank=True, null=True)
#     recording_url = models.URLField(blank=True, null=True)
#     language = models.CharField(max_length=50, blank=True)
#     tags = models.CharField(max_length=200, blank=True)  
#     is_active = models.BooleanField(default=True)


#     def __str__(self):
#         return self.title



# class WebinarBooking(AbstractDateTimeFieldBaseModel):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     webinar = models.ForeignKey('Webinar', on_delete=models.CASCADE)
#     razorpay_order_id = models.CharField(max_length=100,unique=True, blank=True, null=True)
#     razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
#     razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
#     is_paid = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     attended = models.BooleanField(default=False)


# class Payment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#     Webinar = models.ForeignKey(Webinar, on_delete=models.SET_NULL, null=True, blank=True)
#     order_id = models.CharField(max_length=100, unique=True)
#     payment_id = models.CharField(max_length=100, blank=True, null=True)
#     razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
#     amount = models.PositiveIntegerField(help_text="Amount in paise")
#     currency = models.CharField(max_length=10, default='INR')
    
#     STATUS_CHOICES = (
#         ('created', 'Created'),
#         ('paid', 'Paid'),
#         ('failed', 'Failed'),
#     )
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created')

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Payment: {self.order_id} | Status: {self.status}"