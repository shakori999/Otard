import uuid
from django.db import models
from django.contrib.auth import get_user_model
from ecommerce.inventory.models import Product, ProductInventory
from ecommerce.checkout.models import *
from django.urls import reverse
# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price
    
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()
    
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField() 
    ordered = models.BooleanField(default=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    address_2 = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_order'),
        ]


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total 
