from django import forms
from .models import Order, Sales, Payment
from djmoney.forms.fields import MoneyField


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
        fields = ['invoice_number', 'amount', 'invoice_balance']
