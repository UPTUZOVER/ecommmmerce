from django.db import models
from decimal import Decimal
from products.models import Product

class Cart(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        total = Decimal(0)
        for item in self.cartitem_set.all():
            total += item.get_total_price()
        return total

    def get_total_items(self):
        return self.cartitem_set.count()

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_total_price(self):
        return self.product.price * self.quantity


    def get_cart_items(self):
        return self.cartitem_set.all()

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"