from django.db import models
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import Http404
from django.utils import timezone
from inventory.models import Order, Product


# Create your models here.
class OrderPayment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='KES')
    transaction_id = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):
    class PaymentStatus(models.TextChoices):
        PAID = 'PA', _('Paid')
        PENDING = 'PD', _('Pending')

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=255, unique=True, verbose_name='invoice number')
    total_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='KES', verbose_name='total amount')
    date = models.DateField(default=timezone.now)
    payment_status = models.CharField(max_length=3, choices=PaymentStatus.choices,
                                     default=PaymentStatus.PENDING, verbose_name=_('payment status'))
    order_payment = models.ForeignKey(OrderPayment, on_delete=models.SET_NULL,
                                       null=True, blank=True, verbose_name='order payment')

        

   
    