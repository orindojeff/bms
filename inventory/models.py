from django.db import models
from decimal import Decimal
from djmoney.models.fields import MoneyField

# Create your models here.
class Order(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	item = models.CharField(max_length=280)
	quantity = models.IntegerField(verbose_name='Qty')
	cost = MoneyField(max_digits=10, decimal_places=2, default_currency='KES')
	
	def total_cost(self):
		return self.cost * self.quantity


class Sales(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    daily_sales = MoneyField(max_digits=10, decimal_places=2, default_currency='KES')


    def get_80(self):
    	return self.daily_sales * 0.8
    
    def get_20(self):
    	return self.daily_sales * 0.2
  


class Payment(models.Model):
	invoice_number = models.CharField(max_length=10, default="")
	date = models.DateTimeField(auto_now_add=True)
	amount =  MoneyField(max_digits=10, decimal_places=2, default_currency='KES')
	invoice_balance =  MoneyField(max_digits=10, decimal_places=2, default_currency='KES')

	def get_balance(self):
		return self.invoice_balance - self.amount
