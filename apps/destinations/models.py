from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.home.models import AbstractDateFieldMix
# Create your models here.

class Destination(AbstractDateFieldMix):
    main_destination_image =  models.FileField(_('Main Destination Name'), blank=True, null=True)
    main_destination_city = models.CharField(_('Main Destination City'), max_length=255, blank=True, null=True)
    main_destination_state = models.CharField(_('Main Destination State'), max_length=255, blank=True, null=True)
    main_destination_country = models.CharField(_('Main Destination Country'), max_length=255, blank=True, null=True)
    main_destination_heading = models.CharField(_('Main Destination Heading'), max_length=255, blank=True, null=True)
    main_destination_description = models.TextField(_('Main Destination Description'), blank=True, null=True)
    destination_highlight_description = models.TextField(_('Destination highlight-description'), blank=True, null=True)
    latitude = models.DecimalField(_('Latitude'), max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(_('Longitude'), max_digits=9, decimal_places=6, blank=True, null=True)
    map_link = models.URLField(_('Map link'), blank=True, null=True)
    highlight_image = models.FileField(_('highlight Main Image'), blank=True, null=True)
    highlight_heading = models.CharField(_('highlight Main Heading'), max_length=255, blank=True, null=True)
    highlight_description = models.TextField(_('highlight Main Description'), blank=True, null=True)
    best_visit_time = models.TextField(_('Best time to visit'), blank=True, null=True)
    avg_cost = models.DecimalField(_('Average cost'), max_digits=10, decimal_places=2, blank=True, null=True)
    activities = models.TextField(_('Activities'), blank=True, null=True)
    travel_guide = models.TextField(_('Travel Guide'), blank=True, null=True)


    class Meta:
        verbose_name          = "Destination"
        verbose_name_plural   = "Destinations"
