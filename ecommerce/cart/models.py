from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def subtotal(self):
        return self.quantity*self.product.price


class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    address = models.TextField()
    phone = models.BigIntegerField()
    pin = models.IntegerField()
    order_id = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=30,default="Pending")
    delivery_status = models.CharField(max_length=30,default="Pending")
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_id

class Payment(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=30)
    razorpay_payment_id = models.CharField(max_length=30,blank=True)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.order_id