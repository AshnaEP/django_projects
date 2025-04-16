from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField


# Create your models here.
class Car(models.Model):
    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'

    CAR_TYPE_CHOICES = [
        (MANUAL, 'Manual'),
        (AUTOMATIC, 'Automatic'),
    ]
    car_type=models.CharField(max_length=10, choices=CAR_TYPE_CHOICES, default=MANUAL)
    name=models.CharField(max_length=50)
    color=models.CharField(max_length=30)
    description = models.TextField(default="cars")
    rent=models.IntegerField(default=0)
    image=models.ImageField(upload_to='image',blank=True,null=True)
    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name



class Reviews(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    review=models.TextField(default="CarBook makes car rentals super easy with a smooth booking process and great user experience!")
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

# class CarBooking(models.Model):
#     car=models.ForeignKey(Car,on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     name=models.CharField(max_length=35)
#     email=models.CharField(max_length=50)
#     phone=models.IntegerField()
#     pick_up_location=models.CharField(max_length=200,default="Unknown Location")
#     pick_up_date=models.DateField()
#     pick_up_time=models.TimeField()
#     num_of_days=IntegerField()
#     drop_off_location=models.CharField(max_length=200,default="Unknown Location")
#     drop_off_date=models.DateField()
#     drop_off_time=models.TimeField()
#     booking_date = models.DateTimeField(auto_now_add=True)
