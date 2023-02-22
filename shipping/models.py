from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import Driver, Customer, User
from inventory.models import Order


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PickUpStation(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserPickUpStation(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    station = models.ForeignKey(PickUpStation, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.station}"

   
class Shipping(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PD', _('Pending')
        OUT_FOR_DELIVERY = 'OFD', _('Out For Delivery')
        DELIVERED = 'DL', _('Delivered')

    order = models.ForeignKey(Order, default=None, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(auto_now=True, verbose_name='shipped_date')
    station = models.ForeignKey(UserPickUpStation, default=None, on_delete=models.CASCADE)
    status = models.CharField(_('status'), max_length=3, choices=Status.choices, default=Status.PENDING, )
    driver = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
