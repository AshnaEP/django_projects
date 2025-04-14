from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField
from cars.models import Car

# Create your models here.
class CarBooking(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=35)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    pick_up_location=models.CharField(max_length=200,default="Unknown Location")
    pick_up_date=models.DateField()
    pick_up_time=models.TimeField()
    num_of_days=IntegerField()
    drop_off_location=models.CharField(max_length=200,default="Unknown Location")
    drop_off_date=models.DateField()
    drop_off_time=models.TimeField()
    booking_id = models.CharField(max_length=30,default=123)
    deposit_status = models.CharField(max_length=30, default="Pending")
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_id

    def totalAmount(self):
        return self.car.rent*self.num_of_days

    def balanceAmount(self):
        payment = Payment.objects.filter(order_id=self.booking_id).first()
        if payment:
            return self.totalAmount() - payment.amount
        return None

    def paidAmount(self):
        payment = Payment.objects.filter(order_id=self.booking_id).first()
        if payment:
            return payment.amount
        return 0




class Payment(models.Model):
    name = models.CharField(max_length=30)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=30)
    razorpay_payment_id = models.CharField(max_length=30,blank=True)
    paid = models.BooleanField(default=False)
    def __str__(self):
        return self.order_id
