from django.db import models
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import Http404

class Category(models.Model):
	name = models.CharField(max_length=250)
	installation_cost = MoneyField(max_digits=10, decimal_places=2, default_currency='KES', null=True)


	def __str__(self):
		return self.name


	
# class Services(models.Model):
# 	class ServiceTypes(models.TextChoices):
# 		DESIGN = 'DS', _('Design')
# 		INSTALLATION = 'IT', _('Installation')
# 		DESIGN_INSTALLATION = 'DI', _('Design & Installation')

# 	Service_type = models.CharField(
#         max_length=3,
#         choices=ServiceTypes.choices,
#         default=ServiceTypes.DESIGN_INSTALLATION
#     )
        

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
 
    
    def __str__(self):
        return self.name


   

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
        installation_cost = self.category.installation_cost.amount 
        return product_cost + installation_cost
      


# @receiver(pre_save, sender=Product)
# def set_installation_cost(sender, instance, **kwargs):
#     if instance.category and not instance.installation_cost:
#         instance.installation_cost = instance.category.installation_cost



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
    products = models.ManyToManyField(Product, through='OrderItem')
    service = models.CharField(max_length=255, choices=SERVICE_CHOICES)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    @property
    def total_price(self):
        product_prices = [item.product.price.amount for item in self.orderitem_set.all()]
        product_price = sum(product_prices)
        installation_cost = self.service_cost.amount
        total_cost = installation_cost + product_price
        return total_cost

    @property
    def service_cost(self):
        category = Category.objects.get(name=self.service)
        return category.installation_cost

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    @property
    def subtotal(self):
        return self.product.price.amount * self.quantity

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)



def get_installation_cost(category_name):
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    
    return category.installation_cost.amount if category.installation_cost else 0
