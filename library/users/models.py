from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.IntegerField(default=0)
    address = models.TextField(default="")

    def __Str__(self):
        return self.username
