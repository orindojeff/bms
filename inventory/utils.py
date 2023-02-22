# inventory/utils.py

from inventory.models import Order, Cart

def get_or_create_order(user):
    order, created = Order.objects.get_or_create(user=user)
    return order

def get_or_create_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart


def get_or_create_order_id(id):
    order_id, created = Order.objects.get_or_create(id=id)
    return order_id
