# Generated by Django 4.1.6 on 2023-02-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('CM', 'Customer'), ('FM', 'Finance Manager'), ('IT', 'Inventory Manager'), ('DS', 'Designer'), ('SP', 'Supply'), ('DR', 'Driver'), ('AD', 'Admin')], default='AD', max_length=3, verbose_name='User Type'),
        ),
    ]