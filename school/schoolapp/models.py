from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=15)
    principal = models.CharField(max_length=15)
    location = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.name



# class User(models.Model):
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=15)
#     email = models.CharField(max_length=15)
#     address = models.CharField(max_length=15)
#     firstname = models.CharField(max_length=15)
#     lastname = models.CharField(max_length=15)
#
#     def __str__(self):
#         return self.username
