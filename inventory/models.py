from django.db import models
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import Http404
from moneyed import Money
from django.db.models import CASCADE
from django.db.models import Sum

# cart
from django.db import models
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import Http404
from moneyed import Money


class Category(models.Model):
	name = models.CharField(max_length=250)
	installation_cost = MoneyField(max_digits=10, decimal_places=2, default_currency='KES', null=True)


	def __str__(self):
		return self.name


class Service(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=255)



   

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='KES')
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
	
    
    def __str__(self):
        return self.name

    @property
    def total_cost(self):
        product_cost = self.price.amount
        installation_cost = self.category.installation_cost.amount if self.category.installation_cost else 0
        return product_cost + installation_cost

      


@receiver(pre_save, sender=Product)
def set_installation_cost(sender, instance, **kwargs):
    if instance.category and not instance.installation_cost:
        instance.installation_cost = instance.category.installation_cost


class Order(models.Model):
    INSTALLATION_ONLY = 'Installation Only'
    DESIGN_AND_INSTALLATION = 'Design and Installation'
    DESIGN_ONLY = 'Design Only'
    SERVICE_CHOICES = [
        (INSTALLATION_ONLY, 'Installation Only'),
        (DESIGN_AND_INSTALLATION, 'Design and Installation'),
        (DESIGN_ONLY, 'Design Only'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    service = models.CharField(max_length=255, choices=SERVICE_CHOICES)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    transaction_id =models.CharField(max_length=10, default='Pending Payment', verbose_name='order')

    # @property
    def order_quantity(self, obj):
        return obj.orderitem.quantity

  
    @property
    def service_cost(self):
        if self.service == Order.DESIGN_AND_INSTALLATION:
            product_prices = [item.product.price for item in self.cartitem_set.all() if item.product.price is not None]
            product_price = sum(product_prices)
            installation_cost = sum([item.product.category.installation_cost for item in self.cartitem_set.all() if item.product.category and item.product.category.installation_cost])
            return product_price + installation_cost

        elif self.service == Order.DESIGN_ONLY:
            product_prices = [item.product.price for item in self.cartitem_set.all() if item.product.price is not None]
            product_price = sum(product_prices)
            return product_price

        else:
            installation_cost = sum([item.product.category.installation_cost for item in self.cartitem_set.all() if item.product.category and item.product.category.installation_cost])
            return installation_cost


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Product, through='CartItem', related_name='carts')

    def __str__(self):
        return f"{self.user.username}'s Cart"

from django.db import models
from inventory.models import Order, Product

class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=CASCADE)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = get_or_create_order_id(self.order.user)
        super().save(*args, **kwargs)

    @property
    def subtotal(self):
        return self.product.price.amount * self.quantity


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


def get_installation_cost(category_name):
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    
    return category.installation_cost.amount if category.installation_cost else 0


# cart

def get_or_create_order_id(id):
    order_id, created = Order.objects.get_or_create(id=id, ordered=False)
    return order_id



