from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.home.models import AbstractDateFieldMix

# Create your models here.
class Vehicles(AbstractDateFieldMix):
    vehicle_name = models.CharField(_('Vehicle Name'),max_length=255, blank=True, null=True)
