from django import forms
from .models import Category, Service, Product, Order, OrderItem, Payment


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'installation_cost')
        labels = {
            'name': 'Category Name',
            'installation_cost': 'Installation Cost'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'installation_cost': forms.TextInput(attrs={'class': 'form-control'})
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'description')
        labels = {
            'name': 'Service Name',
            'description': 'Service Description'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'category')
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'image': 'Product Image',
            'category': 'Product Category'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('service', )
        labels = {
            'service': 'Service Type'
        }
        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'})
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')
        labels = {
            'product': 'Product',
            'quantity': 'Quantity'
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1})
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount',]

        labels = {
            'amount': 'Amount',
        }
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }
