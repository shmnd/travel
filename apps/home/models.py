from django.db import models
from django.utils.translation import gettext_lazy as _



class AbstractDateFieldMix(models.Model):
    created_date              = models.DateTimeField(_('created_date'), auto_now_add=True, editable=False, blank=True, null=True)
    modified_date             = models.DateTimeField(_('modified_date'), auto_now=True, editable=False, blank=True, null=True)

    class Meta:
        abstract = True


class Hotels(AbstractDateFieldMix):
    hotel_name    = models.CharField(_('Hotel Name'),max_length=255,blank=True, null=True)
    hotel_place = models.TextField(_('Hotel Place'),max_length=255,blank=True, null=True)
    hotel_price = models.IntegerField(_('Hotel Price'),blank=True, null=True)

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'