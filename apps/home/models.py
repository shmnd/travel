from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel
from django.conf import settings

class AbstractDateFieldMix(models.Model):
    created_date              = models.DateTimeField(_('created_date'), auto_now_add=True, editable=False, blank=True, null=True)
    modified_date             = models.DateTimeField(_('modified_date'), auto_now=True, editable=False, blank=True, null=True)

    class Meta:
        abstract = True


class AbstractDateTimeFieldBaseModel(SafeDeleteModel, AbstractDateFieldMix):
    _safedelete_policy = SOFT_DELETE_CASCADE
    
    created_by    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='%(class)s_created', null=True, blank=True)
    modified_by   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='%(class)s_modified', null=True, blank=True)
    is_active     = models.BooleanField(default=True)
    
    class Meta:
        abstract = True


class Hotels(AbstractDateFieldMix):
    hotel_name    = models.CharField(_('Hotel Name'),max_length=255,blank=True, null=True)
    hotel_place = models.TextField(_('Hotel Place'),max_length=255,blank=True, null=True)
    hotel_price = models.IntegerField(_('Hotel Price'),blank=True, null=True)

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


##CAB##

# Category of the cab (e.g., SUV, Sedan, etc.)
class CabCategory(AbstractDateTimeFieldBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, default='Default description')
    icon = models.CharField(max_length=50, blank=True)  # For admin/UI
    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# Vehicle model
class Vehicle(AbstractDateTimeFieldBaseModel):

    class FuelType(models.TextChoices):
        petrol    = 'Petrol'
        deisel  = 'Deisel'
        electric   = 'Electric'
        cng = "CNG"

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50, unique=True)
    seating_capacity = models.PositiveIntegerField()
    vehicle_image = models.ImageField(upload_to='home/vehicle_image/', blank=True, null=True)
    vehicle_type = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    insurance_number = models.CharField(max_length=100, blank=True)
    insurance_expiry = models.DateField(blank=True, null=True)
    rc_document = models.FileField(upload_to='home/rc/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    fuel = models.CharField(choices=FuelType.choices, blank=True, null=True)
    features = models.TextField(blank=True, null=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.registration_number})"

# Vehicle Image model (inline to Vehicle)
class VehicleImage(AbstractDateTimeFieldBaseModel):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vehicles/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.vehicle}"

# Driver model
class Driver(AbstractDateTimeFieldBaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=100, unique=True)
    license_expiry = models.DateField(blank=True, null=True)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='home/drivers/', blank=True, null=True)
    aadhar_number = models.CharField(max_length=20, blank=True)
    aadhar_document = models.FileField(upload_to='home/aadhar/', blank=True, null=True)
    police_verification = models.FileField(upload_to='home/police/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    total_rides = models.PositiveIntegerField(default=0)

    # rating = models.FloatField(default=0.0)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Driver image model (inline to Driver)
class DriverImage(AbstractDateTimeFieldBaseModel):
    driver = models.ForeignKey(Driver, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='drivers/gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.driver}"

# Cab model
class Cab(AbstractDateTimeFieldBaseModel):
    category = models.ForeignKey(CabCategory, on_delete=models.SET_NULL, null=True)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    base_fare = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)
    total_trips = models.PositiveIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cab - {self.vehicle} with Driver - {self.driver}"
    
