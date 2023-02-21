from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class TimeStamp(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    class UserTypes(models.TextChoices):
        CUSTOMER = 'CM', _('Customer')
        FINANCE = 'FM', _('Finance Manager')
        INVENTORY = 'IT', _('Inventory Manager')
        DESIGNER = 'DS', _('Designer')
        DRIVER = 'DR', _('Driver')
        ADMIN = 'AD', _('Admin')

    name = models.CharField(max_length=250, null=True)
    user_type = models.CharField(
        _('User Type'),
        max_length=3,
        choices=UserTypes.choices,
        default=UserTypes.ADMIN,
    )
    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)





class Profile(TimeStamp):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(upload_to='profiles/%Y/%m/', default="profiles/default.png")
    phone_number = PhoneNumberField(blank=True, null=True)
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=Gender.FEMALE,
    )


class Message(TimeStamp):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    name = models.CharField(_('Sender Name'), max_length=255)
    email = models.EmailField(_('Sender Email'))
    is_read = models.BooleanField(default=False)


class Driver(User):
    pass

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

class Customer(User):
    pass

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'