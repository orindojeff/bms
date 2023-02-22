# Generated by Django 4.1.6 on 2023-02-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_alter_cartitem_order_alter_cartitem_quantity_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='carts', through='inventory.CartItem', to='inventory.product'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]