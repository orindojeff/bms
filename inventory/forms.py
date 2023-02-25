from django import forms
from djmoney.forms.fields import MoneyField
from .models import Order, Sales, Payment

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['item', 'quantity', 'cost']

class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['daily_sales']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'invoice_balance']
