# Generated by Django 5.0.6 on 2024-06-07 18:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="cart",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="product",
        ),
        migrations.DeleteModel(
            name="Cart",
        ),
        migrations.DeleteModel(
            name="CartItem",
        ),
    ]
